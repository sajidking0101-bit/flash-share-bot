import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    # /start ke baad file ID/link ka code
    args = message.text.split(maxsplit=1)

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
        "🎬 Watch a short ad to unlock this file.\n\n"
        "👇 Click below to continue.",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "unlock")
def unlock(call):
    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        "⏳ Ad verification system abhi connect karna hai."
    )


print("🤖 Bot started!")
bot.infinity_polling()
