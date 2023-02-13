import json
import openai

# Initialize the OpenAI API
openai.api_key = "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"

# Define the model and the prompt
model_engine = "text-davinci-003"
prompt = "In the year 2050, the world population is projected to reach"

# Call the OpenAI Completion API
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the generated text
message = completions.choices[0].text
print(message)
