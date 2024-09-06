import pprint
import subprocess
from multiprocessing import Pool, Manager
import time

import ollama
import pandas as pd
from ollama import ResponseError

import prompts

MODELS = [
    "llama3.1:8b-instruct-q8_0",
    "llama3.1:70b-instruct-q8_0",
    "gemma2:27b-instruct-q8_0",
]

PROCESSES = 1


def extract_metrics(response):
    return {
        "duration_total": response["total_duration"] / 1e9,
        "duration_load": response["load_duration"] / 1e9,
        "duration_prompt_eval": response["prompt_eval_duration"] / 1e9,
        "duration_eval": response["eval_duration"] / 1e9,
        "token_input": response["prompt_eval_count"],
        "token_output": response["eval_count"],
        "token_input_rate": response["prompt_eval_count"] / (response["prompt_eval_duration"] / 1e9),
        "token_output_rate": response["eval_count"] / (response["eval_duration"] / 1e9),
    }


def pull_model(model_name):
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to pull model {model_name}: {e}")
        
def query_model_with_prompts(prompts, model, index):
    time.sleep(index * 1)
    for i, prompt in enumerate(prompts):
        start_time = time.time()
        response = ollama.chat(model, messages=prompt)
        end_time = time.time()
        
        print(f"Prompt {i + 1}")

        # pretty print json response
        pprint.pp(response)

        print("\nMetrics:")
        metrics = extract_metrics(response)
        metrics["model"] = model
        metrics["client_duration"] = end_time - start_time
        pprint.pp(metrics)

        print("-------")

        all_metrics.append(metrics)



print("Pull all required models")
for model in MODELS:
    try:
        ollama.show(model)
    except ResponseError as e:
        print(f"Pulling model {model}...")
        # Launch CLI with "ollama pull <model>" to pull the model
        pull_model(model)


all_metrics = Manager().list()
for model in MODELS:
    print(f"\n\n~~~~~~~~~~~~~~~\n")
    print(f"EVALUATING MODEL: {model} with {PROCESSES} processes")
    
    # Launch multiple threads
    with Pool(PROCESSES) as pool:
        parameters = [(prompts.prompts, model, idx) for idx in range(0, PROCESSES)]
        pool.starmap(query_model_with_prompts, parameters)    

metrics_df = pd.DataFrame(list(all_metrics))

# Compile mean and stddev for each model
mean_df = metrics_df.groupby("model").mean().reset_index()
mean_df.insert(1, "stat", "mean")
stddev_df = metrics_df.groupby("model").std().reset_index()
stddev_df.insert(1, "stat", "stddev")
combined_df = pd.concat([mean_df, stddev_df], axis=0).sort_values(by=["model", "stat"])

print(combined_df.head())
combined_df.to_csv(f"metrics_{PROCESSES}p.csv")
