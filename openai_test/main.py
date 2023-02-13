import requests

def generate_response(prompt):
    api_key = "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"
    endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    resp = requests.post(endpoint, headers=headers, json=data)

    if resp.status_code == 200:
        response_json = resp.json()
        return response_json["choices"][0]["text"]
    else:
        return "Error generating response"

if __name__ == "__main__":
    prompt = "What is your favorite color?"
    response = generate_response(prompt)
    print(response)