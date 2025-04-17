# Discord Slash Command Bot Template (discord-py-interactions)

A quickstart template for building a modular Discord bot using slash commands with [`discord-py-interactions`](https://github.com/goverfl0w/discord-interactions).

## ✨ Features

- Slash command support via interactions API
- Modular command structure
- Environment variable configuration with `.env` file
- Clean, extendable architecture

## 📦 Dependencies

- [`discord-py-interactions`](https://pypi.org/project/discord-py-interactions/) (v4.4.0)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install with:

```bash
pip install discord-py-interactions==4.4.0 python-dotenv
```

## 📁 Project Structure

```
discord_bot_template/
├── commands/                # Folder for modular command files
│   ├── ping.py              # Example command
│   └── ...                  # Your custom commands!
├── .gitignore               # Excludes specified files in Git
├── .env                     # Environment variables (e.g., token)
├── bot_instance.py          # Loads bot token and other secrets from .env
├── command_controller.py    # Loads all commands from the 'commands' folder
├── main.py                  # Main entry point for the bot
└── README.md                # You are here!
```

## 🛠 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/dfigueroaw/discord-bot-template
   cd discord-bot-template
   ```

2. **Install dependencies**  
   ```bash
   pip install discord-py-interactions==4.4.0 python-dotenv
   ```

3. **Create a `.env` file**  
   Add your bot token and other sensitive values:
   ```
   BOT_TOKEN=your-bot-token-here
   DEFAULT_SCOPE=your-server-id
   ```

4. **Run the bot**  
   ```bash
   python main.py
   ```

## 📌 Notes
- Make sure your bot has the correct permissions and is registered with a slash command application.
- A simple `/ping` command can be found in `commands/ping.py`. It responds with "Pong!" and shows the bot's latency to verify that everything is working.
- This template includes a `dev_mode` flag located in `bot_instance.py`.
  - By default, `dev_mode` is set to `True`. This means:
    - Slash commands will only be registered to a specific test server.
    - You must define the `DEFAULT_SCOPE` variable in your `.env` file with the ID of your development server.
    - Command registration will be nearly instant (ideal for testing).
  - If you set `dev_mode = False`:
    - The `DEFAULT_SCOPE` is no longer required in your `.env`.
    - Commands will be registered globally and available to all servers where the bot is added.
    - However, global command registration can take up to an hour to fully propagate on Discord's end.
