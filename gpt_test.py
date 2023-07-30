import openai

api_key = "apii" #write api

# API anahtarını ayarlayın
openai.api_key = api_key

def gpt3_chat(prompt):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1000
    )
    return response['choices'][0]['text'].strip()

def main():
    print("GPT-3 Chat")

    while True:
        user_input = input("I: ")
        if user_input.lower() == 'exit':
            print("bay şekerim yine bekleriz ")
            break

        prompt = f"ben: {user_input}\nAI: "
        response = gpt3_chat(prompt)
        print("AI:", response)

if __name__ == "__main__":
    main()
