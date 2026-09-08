import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running!"


@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "🔓 UNLOCK FILE",
            callback_data="unlock"
        )
    )

    bot.send_message(
        message.chat.id,
        "🔒 FILE LOCKED\n\n"
        "✨ Your file is ready!\n"
        "🎬 Watch a short ad to unlock it.\n\n"
        "👇 Tap below to unlock",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "unlock")
def unlock(call):
    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        "⏳ Ad verification system will be connected here."
    )


def run_bot():
    print("Bot started...")
    bot.infinity_polling()


threading.Thread(target=run_bot, daemon=True).start()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
