from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your bot token
bot_token = 'Bot Token Here'

# Mapping the source channel to multiple destination channels
source_channel = '@abir_x_official'  # Source channel
destination_channels = ['@abir_x_Official_developer', '@abir_x_official_app_store']  # Destination channels

# Initialize the bot
bot = Bot(token=bot_token)

async def forward_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    # Check if the message is from the source channel
    if message and f"@{message.chat.username}" == source_channel:
        for destination_channel in destination_channels:
            # Forward the message to each destination channel
            await bot.forward_message(
                chat_id=destination_channel,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )

def main():
    application = Application.builder().token(bot_token).build()

    # Set up a message handler for the source channel
    channel_handler = MessageHandler(filters.Chat(username=source_channel), forward_messages)
    application.add_handler(channel_handler)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
