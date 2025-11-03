# --- ここを追加 ---
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run).start()
# --- ここまで追加 ---

# 以下は今までのBotのコード
import discord
from discord import app_commands
import random
import os

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

HIRAGANA = [chr(i) for i in range(ord('あ'), ord('ん') + 1)] + ['ー', 'っ', 'ゃ', 'ゅ', 'ょ', 'ゎ', '!', '?']
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['!', '?']

@bot.event
async def on_ready():
    await tree.sync()
    print(f"ログインしました: {bot.user}")

@tree.command(name="ひらがな3", description="ランダムなひらがな3文字を送信します")
async def hiragana3(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(3))
    await interaction.response.send_message(result)

@tree.command(name="ひらがな4", description="ランダムなひらがな4文字を送信します")
async def hiragana4(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(4))
    await interaction.response.send_message(result)

@tree.command(name="abc3", description="ランダムなアルファベット3文字を送信します")
async def abc3(interaction: discord.Interaction):
    result = ''.join(random.choice(ALPHABETS) for _ in range(3))
    await interaction.response.send_message(result)

@tree.command(name="abc4", description="ランダムなアルファベット4文字を送信します")
async def abc4(interaction: discord.Interaction):
    result = ''.join(random.choice(ALPHABETS) for _ in range(4))
    await interaction.response.send_message(result)

bot.run(os.environ["DISCORD_TOKEN"])