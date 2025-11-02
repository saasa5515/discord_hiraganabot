import discord
from discord import app_commands
import random


intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

HIRAGANA = [chr(i) for i in range(ord('あ'), ord('ん') + 1)] + ['?', '!']

@bot.event
async def on_ready():
    await tree.sync()  # スラッシュコマンドをサーバーに同期
    print(f"ログインしました: {bot.user}")

@tree.command(name="ひらがな", description="ランダムなひらがな3文字を送信します")
async def hiragana(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(3))
    await interaction.response.send_message(result)

import os
bot.run(os.environ["DISCORD_TOKEN"])