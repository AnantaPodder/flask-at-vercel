from flask import Flask, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    # my code
    # updater=Updater(token="5146353719:AAGIaZfO11ghjmk9388x8FZ1z3BvNPo3Wi8",use_context=True)
    # dispatcher=updater.dispatcher
    bot = telegram.Bot("5146353719:AAGIaZfO11ghjmk9388x8FZ1z3BvNPo3Wi8")
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        # disp = Dispatcher(bot, update_queue=update)

        # def start(update: Update, context: CallbackContext):
        #     bot.send_message(chat_id=update.effective_chat.id, text="text")

        # disp.add_handler(CommandHandler("start", start))

        chat_id = update.effective_chat.id
        text = update.message.text
        first_name = update.effective_chat.first_name
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
        return "ok"
    return "error"