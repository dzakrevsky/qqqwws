from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_courier = KeyboardButton("Я - кур'єр")
btn_admin = KeyboardButton('Я – адміністратор')
btn_restaurant = KeyboardButton('Я – ресторан')

btn_addRestaurant = KeyboardButton('Додати ресторан')
btn_addAdmin = KeyboardButton('Додати адміністратора')
btn_checkOrder = KeyboardButton('Перегляд активних замовлень')
btn_on_delivery = KeyboardButton('Включити/Вимкнути роботу доставки')
btn_archive = KeyboardButton('Перегляд архіву')

btn_newOrder = KeyboardButton('Створити замовлення')
btn_showOrders = KeyboardButton('Перегляд замовлень')

btn_view_courier_orders = KeyboardButton("Переглянути мої замовлення")

kb_courier = ReplyKeyboardMarkup(
    [[btn_view_courier_orders]],
    resize_keyboard=True
)

kb_restaurant = ReplyKeyboardMarkup([
    [btn_newOrder, btn_showOrders]
], resize_keyboard=True)


kb_admin = ReplyKeyboardMarkup([
    [btn_addRestaurant, btn_addAdmin],
    [btn_checkOrder, btn_archive],
    [btn_on_delivery]
], resize_keyboard=True)


def worker_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton("Принять заказ"), KeyboardButton("Отказаться от заказа")]
    ], resize_keyboard=True)


kb_main = ReplyKeyboardMarkup([
    [btn_courier, btn_admin, btn_restaurant]
], resize_keyboard=True)
