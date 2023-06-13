import openai
import SpeechRecognition as sr

openai.api_key = 'API_KEY'

# Set up OpenAI API credentials
def get_chatbot_response(input_text):
    response = openai.Completion.create(
        model='gpt-3.5-turbo-0301',
        message=input_text,
        temperature = 0.0
    )
    return response.choices[0].text.strip()

def main():
    user_input = sr.convert_voice_to_text()
    chatbot_response = get_chatbot_response(user_input)
    print("Chatbot response:", chatbot_response)

if __name__ == "__main__":
    main()