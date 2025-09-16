# Lumi-Bot

Lumi-Bot is a simple, rule-based chatbot built in Python. This project demonstrates the basics of natural language processing by matching user input to predefined patterns to generate responses. The bot can handle basic conversations, tell you the current time, and even perform simple math calculations.

## 🚀 Features

* **Rule-Based Responses**: The bot uses a customizable `knowledge_base.json` file to match patterns and provide relevant answers.
* **Simple Math**: It can solve basic math problems like addition, subtraction, multiplication, and division.
* **Time Teller**: The bot can tell you the current time.
* **Contextual Conversation**: It can remember your name and use it in the conversation.
* **Modular Design**: The project is split into separate files (`main.py`, `bot_logic.py`, `knowledge_base.json`) for easy maintenance and scalability.

## ⚙️ Setup

To get Lumi-Bot running, follow these simple steps.

1.  **Clone the Repository (or create the files):**
    If you're using Git, you can clone the project. Otherwise, just make sure you have the three files in the same directory: `main.py`, `bot_logic.py`, and `knowledge_base.json`.

2.  **Install Python:**
    Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

3.  **Run the Bot:**
    Open your terminal or command prompt, navigate to the project directory, and run the following command:

    ```bash
    python main.py
    ```

    If that doesn't work, try using `python3`:

    ```bash
    python3 main.py
    ```

## 🤖 Usage

Once the bot is running, you can start chatting! Here are a few things you can try:

* **Greetings**: `hello`, `hi`, `what's up`
* **Math**: `what is 5 + 3`, `calculate 100 / 2`, `2 * 8`
* **Time**: `what time is it`, `current time`
* **Your Name**: `my name is Alex`
* **Exit**: Type `quit` to end the chat.

## 📂 Project Structure
