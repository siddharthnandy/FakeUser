# FakeUser
Code for FakeUser Discord bot

The following code is used to replace every text by a user with a bot. The warrant for this was when someone changed his username to match that of another user. The bot was nicknamed to the user's actual name, such that when the bot replaced his texts, the texts matched his name instead of his username (i.e. the second user's name), thus not confusing other users.

The bot retrieves the discriminator of every message author and compares it to that of the user of interest (the "troll"). It then deletes the troll's message and resends it as the bot. For this bot to work optimally, the bot should be nicknamed to the troll's actual name.

To get started, replace 'USER DISCRIMINATOR' with the troll's discriminator and 'BOT TOKEN' with your bot's token. Then simply run FakeUser.py in IDLE or any other Python environment.
