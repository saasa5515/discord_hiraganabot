import discord
from discord import app_commands
import random
import os

# Intents設定
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# ひらがな一覧
HIRAGANA = [chr(i) for i in range(ord('あ'), ord('ん') + 1)] + ['ー', 'っ', 'ゃ', 'ゅ', 'ょ']

# 英小文字一覧
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z') + 1)]

@bot.event
async def on_ready():
    await tree.sync()
    print(f"ログインしました: {bot.user}")

# ひらがな3文字
@tree.command(name="ひらがな", description="ランダムなひらがな3文字を送信します")
async def hiragana3(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(3))
    await interaction.response.send_message(result)

# ひらがな4文字
@tree.command(name="ひらがな4", description="ランダムなひらがな4文字を送信します")
async def hiragana4(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(4))
    await interaction.response.send_message(result)

# アルファベット3文字
@tree.command(name="abc3", description="ランダムな英小文字3文字を送信します")
async def abc3(interaction: discord.Interaction):
    result = ''.join(random.choice(ALPHABETS) for _ in range(3))
    await interaction.response.send_message(result)

# アルファベット4文字
@tree.command(name="abc4", description="ランダムな英小文字4文字を送信します")
async def abc4(interaction: discord.Interaction):
    result = ''.join(random.choice(ALPHABETS) for _ in range(4))
    await interaction.response.send_message(result)

# Bot起動
bot.run(os.environ["DISCORD_TOKEN"])