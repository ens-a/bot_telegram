import telebot 
TOKEN = '1532232120:AAHlYKwWNkRj4Ht4LR02Yzl4c5GK4hy7xuY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])


def handle_text_messages(message):
    print('1')
    if message.text == "������":
        bot.send_message(message.from_user.id, "������")
    elif message.text == "��� ��?":
        bot.send_message(message.from_user.id, "� �������� ������ ��� �������� �������.")
    elif message.text == "��� ���� �����?":
        bot.send_message(message.from_user.id, "���� ����� MyFirstTestBot.")
    elif message.text == "��� �� ������?":
        bot.send_message(message.from_user.id, "� ���� �������� �� ��������� ������� �������� - ��� �, ��� ���� ����� � ��� � ���� ������.")
    else:
        bot.send_message(message.from_user.id, "� ���� �� �������. ������ ���-�� ������.")

bot.polling(none_stop=True, interval=0)