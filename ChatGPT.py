import openai
import datetime

# Set up OpenAI API key and prompt
openai.api_key = "your api key"
prompt = "Hello, I'm ChatGPT! What can I help you with today?"

# Define a dictionary to store chat histories by title
chat_histories = {}

# Define a function to save chat history to a file with a specified title
def save_chat_history(title, message):
    if title not in chat_histories:
        chat_histories[title] = ""
    now = datetime.datetime.now()
    chat_histories[title] += f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n"
    with open(f"chat_history_{title}.txt", "w") as f:
        f.write(chat_histories[title])

# Get chat title from user
chat_title = input("Enter a title for your chat: ")

# Begin interactive loop
while True:
    # Get user input
    user_input = input("You: ")

    # Add user input to prompt
    new_prompt = prompt + "\n\nUser: " + user_input.strip()

    # Generate response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=new_prompt,
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        timeout=15,
    )

    # Extract response message and print to console
    message = response.choices[0].text.strip()
    print("ChatGPT:", message)

    # Save chat history to file with specified title
    save_chat_history(chat_title, f"User: {user_input}\nChatGPT: {message}")
