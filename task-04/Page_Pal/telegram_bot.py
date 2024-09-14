from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN: Final = '7225463307:AAGfqgWQBuIXGjLKQb-BZMVwm5-zQ0eLCPo'
BOT_USERNAME: Final = '@book_recom_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am PagePal your one stop for the best book recommendations.")

async def _command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am PagePal your one stop for the best book recommendations.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can control me by sending these commands: \n /start - Returns a welcome message. \n /book - Returns a CSV file with different book names and their details in the given genre. \n /preview - Get a preview link of the given book. \n /list - Returns a message to execute /reading_list command. \n /reading_list displays three buttons, \n Add a book: Press this button to add a new book to the reading list \n Delete a book: Press this button to remove a book from the reading list \n View Reading List: Press this button to return the reading list (docx) \n /help returns the list of commands with their description")

def handle_responses(text: str) ->  str:
    processed: str = text.lower()
    if "hello" in processed or "hey" in processed:
        return "Hey there! How can I help you?"
    if "how are you??" in processed:
        return "I'm good. What about you??"
    else:
        return "I'm sorry, I don't understand what you mean..."
    
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses( text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context}')
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_messages))
    app.run_polling(poll_interval=3)