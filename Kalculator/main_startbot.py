import actions_with as act
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import user_input as u
from calcul import calcul2
from logger import log

heap = {
    'count': 0, #состояние калькулятора
    'first': None, 
    'second': None,
    'operator': None
}

async def startcalc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap['count']=1
    await update.message.reply_text('Введите число1')
    await log( "handlers", "startcalc", f"{ heap }: { calcul2 }" )
  

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text('Введите /start -> Введите отдельными первое число, второе число, опернад (+, -, *, /)')    

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if heap['count'] != 0:
        if heap['count'] == 1:
            heap['first'] = update.message.text
            heap['count'] +=1
            await update.message.reply_text('Введите число 2')
        elif heap['count'] == 2:
            heap['second'] = update.message.text
            heap['count'] +=1
            await update.message.reply_text('Напишите математическую операцию знаком: + - * /')
        elif heap['count'] == 3:
            heap['operator'] = update.message.text
            # здесь калькулятор
            a,b = u.inp(heap["first"], heap["second"])
            await update.message.reply_text(f"{a} {heap['operator']} {b} = {calcul2(a,b, heap['operator'])}")
            # await update.message.reply_text(f"{a} {heap['operator']} {b} = {act.action(a,b,heap['operator'])}")
            heap['count'] = 0
            heap['first'] = None
            heap['second'] = None
            heap['operator'] = None
    await log( "handlers", "startcalc", f"{ heap }: { calcul2 }" )        
        





app = ApplicationBuilder().token("5996937605:AAEt3hoHg8xFyp8tSO7f5f8pxxcZsfcutwk").build()
print("Калькулятор запущен")
# app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", startcalc))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))



app.run_polling()