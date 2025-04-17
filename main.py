from bot_instance import bot
from command_controller import load_commands

@bot.event
async def on_ready():
    user = bot.me
    print("✅ Bot is online!")
    print("🔹 Bot Information:")
    print(f"   🪪 ID: {user.id}")
    print(f"   🤖 Name: {user.name}")
    print(f"   📅 Created At: {user.created_at}")

    print("\n🔸 Connected Guilds:")
    for guild in bot.guilds:
        print(f"   • {guild.name} (ID: {guild.id})")

load_commands()
print("🚀 Script running. Starting bot...")
bot.start()
