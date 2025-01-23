from telegram.ext import Updater,CommandHandler, CallbackContext, MessageHandler,Filters
import os
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton

TOKEN = os.getenv('TOKEN')

def salom(update:Update, context:CallbackContext):
    keyboard=[
        ["Mercadens-Benz"],
        ["BMW"],
        ["TOYOTA"]]
    replay_markup=ReplyKeyboardMarkup(keyboard)

    foydalanuvchi_ismi=update.message.from_user.first_name
    update.message.reply_text(f'{foydalanuvchi_ismi} Welcome to the Famous car bot. Please choose which brand do you want to know',reply_markup=replay_markup)
def message_handler(update,context):
    if update.message.text=="BMW":
        tugma_suv_uchun=[
                         ['BMW SUV'],
                        ['BMW Sedan']
        ]
        replay_suv=ReplyKeyboardMarkup(tugma_suv_uchun)
        update.message.reply_text(f' Which type of model do you want',reply_markup=replay_suv)
    if update.message.text=='BMW SUV':
        update.message.reply_photo(open('image_2025-01-23_20-25-14.png','rb'))
        update.message.reply_text(f'{suv_x6}')
    if update.message.text=='BMW Sedan':
        update.message.reply_photo(open('2022_bmw_m5_cs_4k_8k-1920x1080.jpg','rb'))
        update.message.reply_text(f'{sedan_m5}')
    if update.message.text=="Mercadens-Benz":
        tugma_suv_uchun=[
                         ['Mercadens-Benz SUV'],
                        ['Mercadens-Benz Sedan']
        ]
        replay_suv=ReplyKeyboardMarkup(tugma_suv_uchun)
        update.message.reply_text(f' Which type of model do you want',reply_markup=replay_suv)
    if update.message.text=='Mercadens-Benz SUV':
        update.message.reply_photo(open('image_2025-01-23_22-14-33.png','rb'))
        update.message.reply_text(f'{suv_gle}')
    if update.message.text=='Mercadens-Benz Sedan':
        update.message.reply_text(f'{sedan_clc}')
def ortga(update,context):
        keyboard=[
            ["Back"],
            ]
        replay_markup=ReplyKeyboardMarkup(keyboard)
suv_x6='The boldness of the 2025 BMW X6 is unmistakable. \nFrom the coupe-like roofline to the chiseled profile, this luxury crossover sends a message of power and prestige. Dominant. Great power lives in the wide stance, horizontal contours, and impressive air intakes and exhaust finishers.'
sedan_m5='What makes the BMW M5 CS so special? \nBeing a CS, it is naturally lighter than the M5 Competition model, being leaner by 70kg along with having 10bhp more. A 10bhp increase does not sound much, but coupled with a 70kg weight reduction, the BMW M5 CS takes just 3.0-seconds to get from 0 to 62mph.'
suv_gle="The Mercedes-Benz GLE 450 is a luxury SUV with a 3.0-liter inline-6 turbo engine and mild hybrid drive.\nIt has a 9-speed automatic transmission and can seat five people, with an optional seventh seat.\nFeatures:\nEngine: 3.0-liter inline-6 turbo with mild hybrid drive\nTransmission: 9-speed automatic\nCargo capacity: 630–2,055 L\nAcceleration: 0–100 km/h in 5.6 seconds\nFuel economy: 12.5 L/100 km in the city and 9.6 L/100 km on the highway\nDimensions: 4,924 mm long, 1,797 mm high, and 2,157 mm wide with mirrors\nCurb weight: 2,310 kg"
sedan_clc='Mercedes-Benz CLS-Class models. \nThe 2023 Mercedes-Benz CLS is a four-door sedan with a coupe-like roofline and seating for five. \nIt has a turbocharged 3.0-liter six-cylinder engine (362 horsepower, 369 lb-ft of torque) \nthat is paired with a nine-speed automatic transmission sending power to all four wheels.'


update=Updater(token=TOKEN,use_context=True)

dispatcher=update.dispatcher

dispatcher.add_handler(CommandHandler('start',salom))
dispatcher.add_handler(MessageHandler(Filters.text,callback=message_handler))
dispatcher.add_handler(CommandHandler('back',ortga))


update.start_polling()
update.idle()
