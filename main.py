from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8617945959:AAGhMWZaKK8T26cWDTkUub-ONVS-7CfwTXU"

# 🔥 YOUR PROGRAM CONNECTED HERE
def calculate_result(english, maths, science, physics):
    points = english + maths + science + physics

    if points > 400 or points < 0:
        return "Invalid Marks"

    elif points >= 385:
        grade = "A"
        msg = "Excellent"

    elif points >= 350:
        grade = "B"
        msg = "Good"

    elif points >= 225:
        grade = "C"
        msg = "Nice"

    else:
        grade = "F"
        msg = "Better luck next time"

    percentage = (points / 400) * 100

    return f"""GRADE = {grade}
{msg}
Total = {points}
Percentage = {percentage:.2f}%"""

# 🤖 handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        marks = list(map(int, text.split()))

        if len(marks) != 4:
            await update.message.reply_text("Send 4 numbers like: 80 70 90 85")
            return

        english, maths, science, physics = marks

        result = calculate_result(english, maths, science, physics)

        await update.message.reply_text(result)

    except:
        await update.message.reply_text("Invalid input. Send numbers like: 80 70 90 85")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send marks like: 80 70 90 85")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
