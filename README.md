# Ollama Discord Chatbot
This straightforward Python script enables you to create your own Discord chat bot using Ollama.

This Python Discord bot integrates with Ollama to provide conversational capabilities. Below are instructions on how to set it up and use it.

(NOTE)
To run the bot, you can also simply open the ollama_disc.py file using [Visual Studio Code](https://code.visualstudio.com/) simply click on the 'Run Python file' button

Setup Instructions
1. Clone the Repository:

git clone https://github.com/bigmrstorm/ollama-discord-chatbot.git
cd ollama-discord-chatbot

2. Install Dependencies:
Ensure you have Python installed. Install the required libraries using:
pip install -r requirements.txt

3. Replace Model Name and Bot Token:
In the main.py file, replace modelname with the name of the Ollama model you intend to use. Also, replace YOUR_BOT_TOKEN with your own Discord bot token.

# Running the Bot
To start the bot, run:
python ollama_disc.py
Ensure your Discord bot is invited to your server and has necessary permissions.

# Bot Functionality
The bot listens for messages that mention it and responds using the specified Ollama model.
Reactions with '🔄' on bot messages trigger a reprocessing of the original message for a new response.

# Example Usage
Once set up, the bot will respond to messages in your Discord server based on interactions with the specified Ollama model.

# Support
For issues or questions, please open an issue on GitHub.
