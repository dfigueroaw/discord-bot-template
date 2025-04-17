from interactions import CommandContext
from bot_instance import bot

@bot.command(
    name="ping",
    description="Check the bot's latency",
)
async def ping(ctx: CommandContext):
    latency = round(bot.latency)
    await ctx.send(f"🏓 Pong! Latency: `{latency}ms`")
