from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Define a function to chat with the bot
def chat_with_bot():
    print("Bot: Hello! How can I assist you today? (Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)

# Start a chat with the bot
if __name__ == "__main__":
    chat_with_bot()
