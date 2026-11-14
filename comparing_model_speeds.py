import time
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def compare_model_speeds():
    models = ["claude-3-5-sonnet-20240620","claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    task = "Explain the concept of photosynthesis in a concise paragraph."

    for model in models:
        start_time = time.time()

        response = client.messages.create(
            model=model,
            max_tokens=500,
            messages=[{"role": "user", "content": task}]
        )

        end_time = time.time()
        execution_time = end_time - start_time
        tokens = response.usage.output_tokens
        time_per_token = execution_time/tokens

        print(f"Model: {model}")
        print(f"Response: {response.content[0].text}")
        print(f"Generated Tokens: {tokens}")
        print(f"Execution Time: {execution_time:.2f} seconds")
        print(f"Time Per Token: {time_per_token:.2f} seconds\n")