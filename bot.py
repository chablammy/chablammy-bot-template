# ================================
# Chablammy's Discord Bot Template
# ================================
import discord.ext.commands
import os
import datetime

# ===========
# Global Vars
# ===========
bot = discord.ext.commands.Bot(command_prefix=os.environ['BOT_SYMBOL'])


# ==========
# Bot Events
# ==========

# --------------------------------------------------------
# on_ready: will be run when the bot starts up
# --------------------------------------------------------
@bot.event
async def on_ready():
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Bot is [UP] @ {now}")


# --------------------------------------------------------
# on_message: all messages will hit on_message when sent
# --------------------------------------------------------
@bot.event
async def on_message(message):
    await bot.process_commands(message)


# ============
# Bot Commands
# ============


# --------------------------------------------------------
# $report sends a message showing how many members your
# server has
# --------------------------------------------------------
@bot.command(help="Shows the number of members online")
async def report(ctx):
    await ctx.send(f"```{ctx.guild} has {len(ctx.guild.members)} members```")


# =======
# Run Bot
# =======
bot.run(os.environ['DISCORD_TOKEN'])
