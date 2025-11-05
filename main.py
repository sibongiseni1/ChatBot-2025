import openai

openai.api_key = "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"

def chat_with_Chatbot(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in  ["quit", "exit", "bye"]:
            break
        
        response  = chat_with_Chatbot(user_input)
        print("Chatbot: ", response)