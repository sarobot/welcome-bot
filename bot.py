from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler

updater = Updater( "1651834967:AAH7MNyXOr628fYAWA4LHBYCHuYCQZETCuU",use_context = True )

def start(updater,context):
 updater.message.reply_text('''hi saro iam welcome messanger bot 
 Add me to your group 
 
 வணக்கம் நண்பர்களே நான் உங்களை என் குழுவில் வரவேற்பதற்கு மிகவும் மகிழ்ச்சி அடைகிறேன்😍😍

 
 
  ''')
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f" Hello {member.full_name} வணக்கம் நண்பர்களே நான் உங்களை என் குழுவில் வரவேற்பதற்கு மிகவும் மகிழ்ச்சி அடைகிறேன்😍😍❤️")

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp.add_handler(add_group_handle)

that's a complete code, what else you need?