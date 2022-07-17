from pyrogram import Client, filters
from asyncio import sleep
from random import randint
from art import tprint
from pathlib import Path
from config import api_id, api_hash, phone_number

app = Client("my_account", api_id=api_id,
             api_hash=api_hash, phone_number=phone_number)


def spam_message():
    if Path('./spam_files/text.md').is_file():
        md_str = ''
        with open(r"./spam_files/text.md", "r") as file:
            for line in file:
                md_str += line
        return md_str
    elif Path('./spam_files/text.txt').is_file():
        txt_str = ''
        with open(r"./spam_files/text.txt", "r") as file:
            for line in file:
                txt_str += line
        return txt_str
    else:
        print('[ERROR] Text file not found!')


def check_image():
    path = './spam_files/image.png'
    if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                 or Path(path).suffix == ".jpeg"):
        return True
    else:
        return False


@app.on_message(filters.command('start', prefixes='/') & filters.me)
async def start_spamming(client, message):
    # Получение всех пользователей и чатов
    spam_msg = spam_message()
    chats = []
    async for dialog in app.get_dialogs():
        chats.append({'dialog': dialog.chat.first_name or dialog.chat.title, 'id': dialog.chat.id})

    # Проход по всем пользователям и отправка спам сообщения
    if not check_image():
        print('[+] Start spam mailing without image')
        for chat in chats:
            await app.send_message(chat['id'], spam_msg)
            chat_name = chat['dialog']
            print(f'[+] {chat_name} received spam')
            await sleep(randint(1, 3))  # Кулдаун на отправку сообщений
    else:
        print('[+] Start spam mailing with image')
        for chat in chats:
            await app.send_photo(chat['id'], "./spam_files/image.png", caption=spam_msg)
            chat_name = chat['dialog']
            print(f'[+] {chat_name} received spam')
            await sleep(randint(1, 3))  # Кулдаун на отправку сообщений


@app.on_message(filters.command('check', prefixes='/') & filters.me)
async def check_msg(client, message):
    spam_msg = spam_message()
    if not check_image():
        await message.reply(spam_msg)
    else:
        await message.reply_photo("./spam_files/image.png", caption=spam_msg)


@app.on_message(filters.command('help', prefixes='/') & filters.me)
async def help_msg(client, message):
    text = f"**[1]** Telegram принимает сообщения в разметке Markdown, поэтому если Вы хотите красивое" \
           f" спам-сообщение, в папке spam_files создайте файл text.md и заполните его текстом. Если Вы" \
           f" не хотите делать его красивым, создайте text.txt.\n" \
           f"**[2]** Для отправки рассылки с фотографией в папку spam_files добавьте любое фото форматов .png " \
           f".jpg .jpeg и назовите его image.\n" \
           f"**[3]** Для проверки Вашего сообщения перед отправкой пользователям имеется команда " \
           f"**/check**, которая выведет Вам ваше сообщение."
    await message.reply(text)


if __name__ == '__main__':
    tprint("TG-Spammer")
    app.run()
