# Discord Slash Command Bot Template (discord-py-interactions)

A minimal and modular Discord bot template using slash commands powered by [`discord-py-interactions`](https://github.com/goverfl0w/discord-interactions). Designed for quick setup, easy development, and clean command organization.

## ✨ Features

- Slash command support via interactions API
- Modular command structure
- Environment variable configuration with `.env` file
- Clean, extendable architecture

---

## 📦 Dependencies

- [`discord-py-interactions`](https://pypi.org/project/discord-py-interactions/) (v4.4.0)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install with:

```bash
pip install discord-py-interactions==4.4.0 python-dotenv
```

---

## 📁 Project Structure

```
discord_bot_template/
├── commands/                # Folder for modular command files
│   ├── ping.py              # Example command
│   └── ...                  # Your custom commands!
├── .gitignore               # Excludes specified files in Git
├── .env                     # Environment variables (e.g., token)
├── bot_instance.py          # Creates bot intance and loads credentials from the .env file
├── command_controller.py    # Loads all commands from the 'commands' folder
├── main.py                  # Main entry point for the bot
└── README.md                # You are here!
```

---

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

---

## ➕ Adding a new Command

To add a new slash command to your bot:

1. Create a new `.py` file in the `commands/` directory. Each file should contain one or more related commands.
2. Import the bot instance from `bot_instance.py`. This is important because it’s the central instance that registers all commands.

## 🏓 Example: `ping.py`

```python
from interactions import CommandContext
from bot_instance import bot

@bot.command(
    name="ping",
    description="Check the bot's latency",
)
async def ping(ctx: CommandContext):
    latency = round(bot.latency)
    await ctx.send(f"🏓 Pong! Latency: `{latency}ms`")
```

### **🧑‍💻 Code Breakdown**

- `from interactions import CommandContext`
  - Imports the `CommandContext` class, which provides information about the command invocation (e.g., user, channel) and allows the bot to send responses using methods like `ctx.send()`.
- `from bot_instance import bot`
  - Imports the bot instance defined at `bot_instance.py`. This instance is used to register commands and interact with Discord’s API.
- `@bot.command(...)`
  - Registers a new slash command with the bot.  
  - `name="ping"` sets the command name to `/ping`.  
  - `description="Check the bot's latency"` sets the command description shown in Discord's interface.
- `async def ping(ctx: CommandContext):`
  - Defines the async function that runs when a user executes `/ping`. It takes in the command context (`ctx`), which allows the bot to access details of the interaction and reply to the user.
- `latency = round(bot.latency)`
  - Retrieves and rounds the bot’s current latency.
- `await ctx.send(...)`
  - Sends a message back to the user with the bot’s current latency.

---

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
