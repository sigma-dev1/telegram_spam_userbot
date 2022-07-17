# Telegram spam bot
Telegram userbot for sending to all your contacts on your behalf. The [Pyrogram](https://github.com/pyrogram/pyrogram) module was used to write the bot.

# Quick start

For a quick start, first of all, you need to fill in all the data in [.env](https://github.com/neluckoff/telegram_spam_userbot/blob/master/.env).
I'll tell you what it is: `API_ID` and `API_HASH` are the individual data of the telegram account from which the mailing will be made - you can get them from this [link](https://my.telegram.org/auth); 
`PHONE` is your phone number to which the account is linked.

After filling in the basic information, let's move on to the `spam_files` folder. It stores the main content of your newsletter message, namely text and image. The text is in the `text.md` file - after all, 
telegram supports Markdown markup for beautiful text output (if you don't want beautiful text, you can just create a `text.txt` file). A photo can also be absolutely any - the main rules are the format 
.png/.jpg/.jpeg and the name image (example: `image.png`).


If the files are not named properly (text.md/text.txt and image.png/image.jpg/image.jpeg), then the message will be sent without it.

# Commands

Commands are best used in a chat with yourself, or as it is called in telegram - Favorites.


* **/help** - help command output
* **/start** - start mailing
* **/check** - see what the message looks like before sending
