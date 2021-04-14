from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler

updater = Updater( "1651834967:AAH7MNyXOr628fYAWA4LHBYCHuYCQZETCuU",use_context = True )

def start(updater,context):

 updater.message.reply_text('''hi  iam saro welcome messanger bot 

 Add me to your group 

 

 Made with Love ❤️ by@cosmici

 

 

  ''')

 

def add_group(update: Update, context: CallbackContext):

    for member in update.message.new_chat_members:

        update.message.reply_text(f" Hello {member.full_name}  ")

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)

dp =updater.dispatcher.add_handler

dp(CommandHandler('start',start))

dp.add_handler(add_group_handle)

updater.start_polling()

updater.idle()
