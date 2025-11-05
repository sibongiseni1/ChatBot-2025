# chatbot.py
import os
from openai import OpenAI

# Option 1: Directly set your API key (for quick testing)
# client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Option 2: Use environment variable (recommended)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat():
    print("💬 Welcome to your Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye! 👋")
            break

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )
            # Print the assistant's reply
            reply = response.choices[0].message.content
            print(f"Chatbot: {reply}\n")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat()
