from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '7901632898:AAFF5UShYE8-cEC71ABnJX9gC_zpClwBtZQ'  # Не забудь скрыть токен потом!

ADMIN_USERNAME = '@alfaperson42'

def start(update, context):
    update.message.reply_text("Добро пожаловать! Напишите, какую услугу вы ищете, и мы вам поможем.")

def forward_to_admin(update, context):
    message = update.message
    user_text = f"📩 Новая заявка от @{message.from_user.username or 'без username'}:\n\n{message.text}"
    context.bot.send_message(chat_id=ADMIN_USERNAME, text=user_text)
    message.reply_text("Спасибо! Ваша заявка отправлена мастеру. Он свяжется с вами в Telegram.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_admin))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
