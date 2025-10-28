# set TELEGRAM_TOKEN=тут_твій_токен
# python bot/bot.py

import os
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("Set TELEGRAM_TOKEN env variable")

TASK_FILE = "tasks/exam_task.txt"
NOTEBOOK_FILE = "notebooks/module5_pytorch.ipynb"

WELCOME = (
    "Привіт! Я навчальний бот для Exam — Модуль 5: PyTorch.\n\n"
    "Команди:\n"
    "/start - привітання\n"
    "/help - допомога\n"
    "/task - отримати завдання\n"
    "/notebook - скачати Jupyter Notebook з прикладами\n"
    "/hint - підказка для PyTorch\n"
    "/quiz - короткий тест\n"
    "/submit - інструкція як здавати відповіді (а також можна прислати файл прямо сюди)\n"
)

HINT_TEXT = (
    "Підказка: у PyTorch основні кроки — визначити модель (nn.Module), "
    "створити loss і optimizer, виконати training loop: forward -> loss -> backward -> optimizer.step().\n"
    "Не забувай викликати model.train() для тренування і model.eval() для інференсу.\n"
)

QUIZ_QUESTIONS = [
    ("Яка базова одиниця даних у PyTorch для обчислень?", "tensor"),
    ("Яка функція в PyTorch обчислює похідні для всіх параметрів? (англ.)", "backward"),
    ("Як викликати режим оцінювання у моделі?", "model.eval"),
    ("Який модуль містить готові шари (Dense/Conv) у PyTorch?", "torch.nn"),
    ("Що виконує optimizer.step()? (коротко)", "оновлення ваг"),
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text(WELCOME)

def help_cmd(update: Update, context: CallbackContext):
    update.message.reply_text(WELCOME)

def task_cmd(update: Update, context: CallbackContext):
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            txt = f.read()
        update.message.reply_text(txt)
    else:
        update.message.reply_text("Завдання тимчасово недоступне. Перевірте файлову структуру.")

def notebook_cmd(update: Update, context: CallbackContext):
    if os.path.exists(NOTEBOOK_FILE):
        update.message.reply_document(document=open(NOTEBOOK_FILE, "rb"))
    else:
        update.message.reply_text("Ноутбук не знайдено. Скопіюйте notebooks/module5_pytorch.ipynb")

def hint_cmd(update: Update, context: CallbackContext):
    update.message.reply_text(HINT_TEXT)

def submit_cmd(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Щоб здати завдання, надішліть файл (.py або .ipynb) як документ у відповіді боту. "
        "Викладач зможе зібрати файли в папці submissions або перевірити вручну.\n"
        "Або скористайтесь /help для інструкцій."
    )

def quiz_cmd(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.user_data['quiz_index'] = 0
    q, _ = QUIZ_QUESTIONS[0]
    update.message.reply_text(f"Питання 1/5:\n{q}")

def answer_handler(update: Update, context: CallbackContext):
    text = update.message.text or ""
    if 'quiz_index' in context.user_data:
        i = context.user_data['quiz_index']
        correct = QUIZ_QUESTIONS[i][1].lower()
        if correct in text.lower():
            update.message.reply_text("Правильно! ✅")
        else:
            update.message.reply_text(f"Можливо, не зовсім. Правильна відповідь: {correct}")
        i += 1
        if i < len(QUIZ_QUESTIONS):
            context.user_data['quiz_index'] = i
            q, _ = QUIZ_QUESTIONS[i]
            update.message.reply_text(f"Питання {i+1}/{len(QUIZ_QUESTIONS)}:\n{q}")
        else:
            update.message.reply_text("Квіз завершено! Дякую. 🎓")
            context.user_data.pop('quiz_index')
        return

    if update.message.document:
        file = update.message.document
        fname = file.file_name
        submissions_dir = "submissions"
        os.makedirs(submissions_dir, exist_ok=True)
        fpath = os.path.join(submissions_dir, fname)
        file.get_file().download(custom_path=fpath)
        update.message.reply_text(f"Файл збережено: {fpath}")
        return

    update.message.reply_text("Не зрозумів. Скористайтесь /help або надішліть файл як документ для здачі.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(CommandHandler("task", task_cmd))
    dp.add_handler(CommandHandler("notebook", notebook_cmd))
    dp.add_handler(CommandHandler("hint", hint_cmd))
    dp.add_handler(CommandHandler("submit", submit_cmd))
    dp.add_handler(CommandHandler("quiz", quiz_cmd))
    dp.add_handler(MessageHandler(Filters.document | Filters.text & ~Filters.command, answer_handler))

    print("Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()