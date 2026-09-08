import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔒 FILE LOCKED\n\n"
        "Your file is ready!\n"
        "🔓 Unlock the file to continue.",
        reply_markup=unlock_button()
    )

def unlock_button():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(
            "🔓 UNLOCK FILE",
            callback_data="unlock"
        )
    )
    return markup

@bot.callback_query_handler(func=lambda call: call.data == "unlock")
def unlock(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⏳ Ad/verification system abhi setup hona baaki hai."
    )

print("Bot is running...")
bot.infinity_polling()
