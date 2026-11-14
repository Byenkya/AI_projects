"""
Write a function called generate_questions that does the following:

Takes two parameters: topic and num_questions
Generates num_questions thought-provoking questions about the provided topic as a numbered list
Prints the generated questions
For example, calling generate_questions(topic="free will", num_questions=3) could result in the following output:

To what extent do our decisions and actions truly originate from our own free will, rather than being shaped by factors beyond our control, such as our genes, upbringing, and societal influences?
If our decisions are ultimately the result of a complex interplay of biological, psychological, and environmental factors, does that mean we lack the ability to make authentic, autonomous choices, or is free will compatible with determinism?
What are the ethical and philosophical implications of embracing or rejecting the concept of free will? How might our views on free will impact our notions of moral responsibility, punishment, and the nature of the human condition?
In your implementation, please make use of the following parameters:

max_tokens to limit the response to under 1000 tokens
system to provide a system prompt telling the model it is an expert on the particular topic and should generate a numbered list.
stop_sequences to ensure the model stops after generating the correct number of questions. (If we ask for 3 questions, we want to make sure the model stops as soon as it generates "4." If we ask for 5 questions, we want to make sure the model stops as soon as it generates "6.")

"""

from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

def generate_questions(topic, num_questions=3):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        system=f"You are an expert on {topic}. Generate thought-provoking questions about this topic.",
        messages=[
            {"role": "user", "content": f"Generate {num_questions} questions about {topic} as a numbered list."}
        ],
        stop_sequences=[f"{num_questions+1}."]
    )
    print(response.content[0].text)

generate_questions(topic="free will", num_questions=3)


