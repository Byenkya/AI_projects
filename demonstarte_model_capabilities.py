from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def compare_model_capabilities():
    models = ["claude-3-5-sonnet-20240620", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    task = """
    What is the geometric monthly fecal coliform mean of a distribution system with the following FC
 counts: 24, 15, 7, 16, 31 and 23? The result will be inputted into a NPDES DMR, therefore, round
 to the nearest whole number.  Respond only with a number and nothing else.
    """

    for model in models:
        answers = []
        for attempt in range(7):
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[{"role": "user", "content": task}]
            )
            answers.append(response.content[0].text)

        print(f"Model: {model}")
        print(f"Answers: ", answers)

compare_model_capabilities()