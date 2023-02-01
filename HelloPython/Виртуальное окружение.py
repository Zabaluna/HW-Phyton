python -m venv new_venv # - создать виртуальное окружение
# source venv/bin/activate - активация ВО для линукс
venv\Scripts\activate # - НЕ ЗАБЫТЬ ПРО ТОЧКУ через TAB(таб показывает, что пропустила) активация в виндоус (обязательно \ - обратный слэш) 
deactivate # - деактивация виртуального окружения
pip freeze # - распечатает установленные пакеты(библиотеки)     (создаёт файл зависимостей)
pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют имя или имена модулей, которые требуется обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
pip install requests lxml # - установка библиотек requests и lxml - если нужно установить несколько библиотек,
# то можно перечислить их через пробел
pip uninstall lxml -y # - удаление библиотеки, в данном случае lxml
pip uninstall -y -r requirements.txt # - удаляет все библиотеки, которые были прописаны в файле requirements.txt
pip freeze > requirements.txt # - создаёт файл с зависимостями (в нём прописываются все библиотеки и версии нашего проекта)
pip install -r requirements.txt # - устанавливаем все библиотеки с зависимостями

cd # - перейти в нужную папку
cd.. # - на уровень выше

Что делать если pycharm не видит библиотеку
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment

pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют имя или имена модулей, которые требуется обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
python.exe -m pip install -U pip setuptools

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  - команда для пауршелла для имени администратора

Set-ExecutionPolicy RemoteSigned - команда для пауршелла для имени администратора


Что делать если pycharm не видит библиотеку
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment

https://bootstrap.pypa.io/get-pip.py

pip install -U pip setuptools

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  команда для пауршелла от имени администратора
Set-ExecutionPolicy RemoteSigned

https://core.telegram.org/bots/samples - ссылка на языки программирования для телеграмм

https://python-telegram-bot.org/
-------------------------------------
from telegram.ext import Filters
MessageHandler(Filters.video, callback_method)
MessageHandler(filters, callback)  - текст для бота
from telegram.ext import Filters, MessageHandler
--------------------------------
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters    


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="It's our new bot from Python course!")


app = ApplicationBuilder().token("5662299299:AAGxOefaqxw144ou_oNXAA3eV0wyGB5nOfA").build()

app.add_handler(CommandHandler("hola", hello))
app.add_handler(CommandHandler("answer", start))

print('start')
app.run_polling()
-------
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext import filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="It's our new bot from Python course!")


app = ApplicationBuilder().token("5662299299:AAGxOefaqxw144ou_oNXAA3eV0wyGB5nOfA").build()

app.add_handler(CommandHandler("hola", hello))
app.add_handler(CommandHandler("answer", start))
app.add_handler(MessageHandler(filters.TEXT, start))

print('start')
app.run_polling()