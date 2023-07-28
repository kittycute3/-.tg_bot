from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging




math = {'Афанасьева' : 'математика: 5',
        'Воробьев' : 'математика: 4',
        'Иванов' : 'математика: 4',
        'Крылова' : 'математика: 3',
        'Васин' : 'математика: 5',
        'Григорьев' : 'математика: 2',

        'Фролова' : 'математика: 5',
        'Жуков' : 'математика: 3',
        'Антонова' : 'математика: 4',
        'Чурилкина' : 'математика: 2',
        'Бондаренко' : 'математика: 5',
        'Сергеев' : 'математика: 3'}

rus = {'Афанасьева' : 'русский: 5',
       'Воробьев': 'русский: 2',
       'Иванов': 'русский: 4',
       'Крылова': 'русский: 5',
       'Васин': 'русский: 3',
       'Григорьев': 'русский: 4',

       'Фролова': 'русский: 3',
       'Жуков': 'русский: 4',
       'Антонова': 'русский: 5',
       'Чурилкина': 'русский: 3',
       'Бондаренко': 'русский: 4',
       'Сергеев': 'русский: 5'}

inf = {'Афанасьева' : 'информатика: 5',
       'Воробьев': 'информатика: 5',
       'Иванов': 'информатика: 5',
       'Крылова': 'информатика: 4',
       'Васин': 'информатика: 5',
       'Григорьев': 'информатика: 4',

       'Фролова': 'информатика: 5',
       'Жуков': 'информатика: 4',
       'Антонова': 'информатика: 5',
       'Чурилкина': 'информатика: 4',
       'Бондаренко': 'информатика: 5',
       'Сергеев': 'информатика: 5'}

A9 = {'/1 Афанасьева' : 1,
      '/2 Воробьев' : 1,
      '/3 Иванов' : 1,
      '/4 Крылова' : 1,
      '/5 Васин' : 1,
      '/6 Григорьев' : 1}

B9 = {'/7 Фролова': 1,
      '/8 Жуков' : 1,
      '/9 Антонова' : 1,
      '/10 Чурилкина' : 1,
      '/11 Бондаренко' : 1,
      '/12 Сергеев' : 1,}


API = '6525277596:AAGbl0wSYl1CymNXhc6ZxsMpbL2Q-g_XJAQ'

#класс который описывает состояние пользователя
class Student(StatesGroup):
    STUDENT = State()
    USER_INPUT = State()
class Subject(StatesGroup):
    SUBJECT = State()



#переменная памяти для храненипя состояния
storage = MemoryStorage()

bot = Bot(token=API)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['remand'])
async def remand(message: types.Message):
    await Student.USER_INPUT.set()
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text='введите фамилию ученика:')

@dp.message_handler(state=Student.USER_INPUT)
async def input(message: types.Message, state: FSMContext):
    user_text = message.text
    chat_id = message.chat.id
    if user_text == 'Афанасьева':
        math.pop('Афанасьева')
        rus.pop('Афанасьева')
        inf.pop('Афанасьева')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Воробьев':
        math.pop('Воробьев')
        rus.pop('Воробьев')
        inf.pop('Воробьев')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Иванов':
        math.pop('Иванов')
        rus.pop('Иванов')
        inf.pop('Иванов')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Крылова':
        math.pop('Крылова')
        rus.pop('Крылова')
        inf.pop('Крылова')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Васин':
        math.pop('Васин')
        rus.pop('Васин')
        inf.pop('Васин')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Григорьев':
        math.pop('Григорьев')
        rus.pop('Григорьев')
        inf.pop('Григорьев')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')

    elif user_text == 'Фролова':
        math.pop('Фролова')
        rus.pop('Фролова')
        inf.pop('Фролова')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Жуков':
        math.pop('Жуков')
        rus.pop('Жуков')
        inf.pop('Жуков')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Антонова':
        math.pop('Антонова')
        rus.pop('Антонова')
        inf.pop('Антонова')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Чурилкина':
        math.pop('Чурилкина')
        rus.pop('Чурилкина')
        inf.pop('Чурилкина')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Бондаренко':
        math.pop('Бондаренко')
        rus.pop('Бондаренко')
        inf.pop('Бондаренко')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')
    elif user_text == 'Сергеев':
        math.pop('Сергеев')
        rus.pop('Сергеев')
        inf.pop('Сергеев')
        await state.finish()
        await bot.send_message(chat_id, text='ученик отчислен, и вы больше не можете взаимодействовать с ним')

    else:
        await bot.send_message(chat_id, text='такого ученика нет в списках')


@dp.message_handler(commands=['start'])

async def start(message: types.Message):
    chat_id = message.chat.id
#создание кнопок
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='9а😜', callback_data='but1')
    button2 = types.InlineKeyboardButton(text='9б🤑', callback_data='but2')
    keyboard.add(button1, button2)
    await bot.send_message(chat_id=chat_id, text='выберете класс:', reply_markup=keyboard)


async def menu1(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    user_text = 'выберете ученика 9a класса:\n'
    for s, j in A9.items():
        a = s.split()
        id_s = a[0]
        s = a[1]
        user_text += id_s + ' ' + s + '\n'

    await bot.send_message(chat_id=chat_id, text=user_text)

async def menu2(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    user_text = 'выберете ученика 9б класса:\n'
    for s, j in B9.items():
        a = s.split()
        id_s = a[0]
        s = a[1]
        user_text += id_s + ' ' + s + '\n'

    await bot.send_message(chat_id=chat_id, text=user_text)


@dp.callback_query_handler()
async def student(callback_data: types.CallbackQuery):
    data = callback_data.data
    if data == 'but1':

        await menu1(callback_data)
        await Student.STUDENT.set()
    elif data == 'but2':

        await menu2(callback_data)
        await Student.STUDENT.set()


@dp.message_handler(state=Student.STUDENT)
async def student(message: types.Message, state: FSMContext):
    number = message.text
    chat_id = message.chat.id
    if number == '/1':
        try:
            num1 = math.get('Афанасьева')
            num2 = rus.get('Афанасьева')
            num3 = inf.get('Афанасьева')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/2':
        try:
            num1 = math.get('Воробьев')
            num2 = rus.get('Воробьев')
            num3 = inf.get('Воробьев')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')


    elif number == '/3':
        try:
            num1 = math.get('Иванов')
            num2 = rus.get('Иванов')
            num3 = inf.get('Иванов')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/4':
        try:
            num1 = math.get('Крылова')
            num2 = rus.get('Крылова')
            num3 = inf.get('Крылова')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/5':
        try:
            num1 = math.get('Васин')
            num2 = rus.get('Васин')
            num3 = inf.get('Васин')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/6':
        try:
            num1 = math.get('Григорьев')
            num2 = rus.get('Григорьев')
            num3 = inf.get('Григорьев')
            await state.finish()
            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/7':
        try:
            num1 = math.get('Фролова')
            num2 = rus.get('Фролова')
            num3 = inf.get('Фролова')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/8':
        try:
            num1 = math.get('Жуков')
            num2 = rus.get('Жуков')
            num3 = inf.get('Жуков')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/9':
        try:
            num1 = math.get('Антонова')
            num2 = rus.get('Антонова')
            num3 = inf.get('Антонова')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/10':
        try:
            num1 = math.get('Чурилкина')
            num2 = rus.get('Чурилкина')
            num3 = inf.get('Чурилкина')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/11':
        try:
            num1 = math.get('Бондаренко')
            num2 = rus.get('Бондаренко')
            num3 = inf.get('Бондаренко')

            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')

    elif number == '/12':
        try:
            num1 = math.get('Сергеев')
            num2 = rus.get('Сергеев')
            num3 = inf.get('Сергеев')
            await state.finish()
            await bot.send_message(chat_id=chat_id, text=num1)
            await bot.send_message(chat_id=chat_id, text=num2)
            await bot.send_message(chat_id=chat_id, text=num3)
        except Exception as Ex:
            await bot.send_message(chat_id=chat_id, text='отчислен')





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
