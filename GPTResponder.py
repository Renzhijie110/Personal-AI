import openai

def get_chatbot_response(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate ChatGPT model
        prompt=input_text,
        max_tokens=100  # Adjust the response length as desired
    )
    return response.choices[0].text.strip()
