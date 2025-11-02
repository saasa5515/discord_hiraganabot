import os
import random
import discord
from discord import app_commands
from flask import Flask
import threading

# ==========================
# 🔹 Flask（ダミーWebサーバー）
# ==========================
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running on Render!"

def run():
    port = int(os.getenv("PORT", 8080))  # RenderがPORTを指定してくる
    app.run(host="0.0.0.0", port=port)

# ==========================
# 🔹 Discord Botの設定
# ==========================
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

HIRAGANA = [chr(i) for i in range(ord('あ'), ord('ん') + 1)] + ['?', '!']

@bot.event
async def on_ready():
    await tree.sync()  # スラッシュコマンドをサーバーに同期
    print(f"✅ ログインしました: {bot.user}")

@tree.command(name="ひらがな", description="ランダムなひらがな3文字を送信します")
async def hiragana(interaction: discord.Interaction):
    result = ''.join(random.choice(HIRAGANA) for _ in range(3))
    await interaction.response.send_message(result)

# ==========================
# 🔹 FlaskとBotを同時に起動
# ==========================
if __name__ == "__main__":
    threading.Thread(target=run).start()  # Flaskを別スレッドで起動
    bot.run(os.environ["DISCORD_TOKEN"])