##BlitzKrieg v.1.1
#Copyright Maya Pharis 2017

#GENERAL BOT STUFF

#Imports and Bot Command definition
import asyncio
import discord
import logging
import math
import os
import random
import sys
from discord import utils
from discord.ext.commands import Bot
logging.basicConfig(level = logging.INFO)

#Definition of BlitzKrieg's prefix.
my_bot = Bot(command_prefix = "%")


#Bot Startup
@my_bot.event
async def on_read():
    print("Deleting C:\\Windows\\System32\\...")
    #I have a feeling I'm gonna get straight up slugged for this.


#COMMANDS

#Command: Hello
@my_bot.command()
async def hello(*args):
	return await my_bot.say("Qu'est-ce que sup, my dude?")

#Command: Ping
@my_bot.command()
async def ping(*args):
    return await my_bot.say("A game released in 1972 by Atari.")


#RAINBOW SIX SIEGE
#Command: Random Operator (Rainbow Six Siege) - Attack
@my_bot.command()
async def attack():
    attk = random.choice(open("data/attackers.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing as " + attk)
#Command: Random Operator (Rainbow Six Siege) - Defense
@my_bot.command()
async def defense():
    defen = random.choice(open("data/defenders.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing as " + defen)


#OVERWATCH
'''
#Command: Overwatch Team Comp
@my_bot.command()
async def comp():
    if message.content.startswith('%comp'):
        await my_bot.send_message(message.channel, 'How many offense heroes do you want?')
        i == 1
		if i == 1:
            msg = await my_bot.wait_for_message(author=message.author)
			offen = msg
			i = i + 1
            await my_bot.send_message(message.channel, "How many defense heroes do you want?")
		if i == 2:
			msg = await my_bot.wait_for_message(author=message.author)
			defen = msg
			i = i + 1
			await my_bot.send_message(message.channel, "How many tanks do you want?")
		if i == 3:
			msg = await my_bot.wait_for_message(author=message.author)
			tan = msg
			i = i + 1
			await my_bot.send_message(message.channel, "How many supports do you want?")
		if i == 4:
			msg = await my_bot.wait_for_message(author=message.author)
			supp = msg
		offense = ["Genji", "McCree", "Soldier: 76", "Reaper", "Sombra", "Tracer"]
		defense = ["Bastion", "Hanzo", "Junkrat", "Widowmaker", "Mei", "Torb"]
		tank = ["D.Va", "Orisa", "Roadhog", "Reinhardt", "Winston", "Zarya"]
		support = ["Mercy", "Lucio", "Ana", "Symmetra", "Zenyatta"]
		random.shuffle(offense)
		random.shuffle(defense)
		random.shuffle(tank)
		random.shuffle(support)
		await my_bot.send_message(message.channel, "Offense Heroes: " + offense[0:(int(offen))])
'''
#Overwatch Random: DPS
@my_bot.command()
async def herodps():
    dps = random.choice(open("data/dps.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing " + dps)

#Overwatch Random: Tank
@my_bot.command()
async def herotank():
    tank = random.choice(open("data/tank.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing " + tank)

#Overwatch Random: Healer
@my_bot.command()
async def heroheal():
    heal = random.choice(open("data/healer.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing " + heal)

#Overwatch Random: Defense
@my_bot.command()
async def herodef():
    herodef = random.choice(open("data/def.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing " + herodef)

#Comp Points Rewards checker
@my_bot.command()
async def comppoints():
    await my_bot.say("Please specify a rank. Use %bronze, %silver, %gold, %platinum, %master, %grandmaster or %top500.")
async def bronze():
    await my_bot.say("You will recieve 100 competitive points at the end of the season. Try harder next season.")
@my_bot.command()
async def silver():
    await my_bot.say("You will recieve 200 competitive points at the end of the season. A decent rank, but you can do better.")
@my_bot.command()
async def gold():
    await my_bot.say("You will recieve 400 competitive points at the end of the season. Respectable rank. Can you do better?")
@my_bot.command()
async def platinum():
    await my_bot.say("You will recieve 800 competitive points at the end of the season. You're probably here because of decay, aren't you?")
@my_bot.command()
async def diamond():
    await my_bot.say("You will recieve 1200 competitive points at the end of the season. Impressive. Get to Master. I dare you.")
@my_bot.command()
async def master():
    await my_bot.say("You will recieve 2000 competitive points at the end of the season. One step away from glory. Do it.")
@my_bot.command()
async def grandmaster():
    await my_bot.say("You will recieve 3000 competitive points at the end of the season. You've done it. I saulte you, you no-life nerd.")
@my_bot.command()
async def top500():
    await my_bot.say("Hats off to you, my good man. You truly are a respectable Overwatch player.")

#Command: Random Hero (Overwatch)
@my_bot.command()
async def hero():
    hero = random.choice(open("data/heroes.txt",encoding='UTF-8').readlines())
    await my_bot.say("You will be playing " + hero)


#IN A NUTSHELL QUOTES
#Command Set: In a Nutshell quotes
@my_bot.command()
#Blake
@my_bot.command()
async def blake():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Blake.txt",encoding='UTF-8').readlines()))

#Brandon
@my_bot.command()
async def brandon():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Brandon.txt",encoding='UTF-8').readlines()))

#Josh
@my_bot.command()
async def josh():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Josh.txt",encoding='UTF-8').readlines()))

#Jake
@my_bot.command()
async def jake():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Jake.txt",encoding='UTF-8').readlines()))

#Maya
@my_bot.command()
async def maya():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Maya.txt",encoding='UTF-8').readlines()))

#Gui
@my_bot.command()
async def ray():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Gui.txt",encoding='UTF-8').readlines()))

#Xavier
@my_bot.command()
async def xavier():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Xavier.txt",encoding='UTF-8').readlines()))

#Leah
@my_bot.command()
async def leah():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Leah.txt",encoding='UTF-8').readlines()))

#Max
@my_bot.command()
async def max():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Max.txt",encoding='UTF-8').readlines()))

#Laura
@my_bot.command()
async def laura():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Laura.txt",encoding='UTF-8').readlines()))

#British Josh
@my_bot.command()
async def britjosh():
    await my_bot.say(random.choice(open("data/nutshell_quotes/British_Josh.txt",encoding='UTF-8').readlines()))

#Nelson
@my_bot.command()
async def nelson():
    await my_bot.say(random.choice(open("data/nutshell_quotes/Laura.txt",encoding='UTF-8').readlines()))

#MISC
#Command: Magic 8-Ball
@my_bot.command()
async def eightball():
    ball = random.choice(open("data/8ball.txt",encoding='UTF-8').readlines())
    await my_bot.say(ball)

#Command: Game Selector
#Sometimes I just can't decide what game to play. Hopefully, this will help with that.
@my_bot.command()
async def game():
    game = random.choice(open('data/games.txt',encoding='UTF-8').readlines())
    await my_bot.say("You should play " + game)

#Command: Dad Joke
#Yes, I did.
@my_bot.command()
async def dad():
    joke = random.choice(open("data/dadjokes.txt",encoding='UTF-8').readlines())
    await my_bot.say(joke)
#Info
@my_bot.command()
async def info():
    await my_bot.say("Welcome to BlitzKrieg's informational menu. For info on specific commands, type any of the following.")
    await my_bot.say("```%info_rainbow\n%info_overwatch\n%info_nutshell\n%info_misc```")

#Info: Rainbow Six
@my_bot.command()
async def info_rainbow():
    await my_bot.say("Commands for Rainbow Six Siege.")
    await my_bot.say("```%attack = Chooses a random operator on the attacking side for you to play.\n%defense - Chooses a random operator from the defending side for you to play.```")

#Info: Overwatch
@my_bot.command()
async def info_overwatch():
    await my_bot.say("Commands for Overwatch.")
    await my_bot.say("```%hero - Chooses a random hero for you to play.\n%herodps - Chooses a random DPS hero for you to play.\n%herotank - Chooses a random tank for you to play.\n%heroheal - Chooses a random healer for you to play.\n%herodef - Chooses a random defnese hero for you to play.\n%(rank) - Tells you how many competitive points you will recieve as an end-of-season reward.```")

#Info: In-A-Nutshell
@my_bot.command()
async def info_nutshell():
    await my_bot.say("Available \"In a Nutshell\" commands.")
    await my_bot.say("```%maya\t%josh\n%blake\t%brandon\n%jake\t%gui\n%xavier\t%leah\n%max\t%laura\n%britjosh\t%gui```")

#Info: Misc
@my_bot.command()
async def info_misc():
    await my_bot.say("Available misc. commands.")
    await my_bot.say("```%eightball - Gives you a Magic Eight Ball response to a question.\n%game = Game Selector. Gives you a random game to play.```")

my_bot.run(token)
