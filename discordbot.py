import discord
from pprint import pprint
from dotenv import load_dotenv
from os import getenv
from time import sleep 
from discord.ext import commands

client = discord.Client()

load_dotenv()
TOKEN = getenv('TOKEN')

intents = discord.Intents.default() 
intents.message_content = True 

bot = commands.Bot(command_prefix='$', intents=intents)


@client.event 
async def on_ready():
  sleep(4)
  channel = client.get_channel(channel_id)
  await channel.send("Pidoras")
 
async def na_gotove():
  for guild in client.guilds:
    if guild.name == GUILD:
      break

      print(f'{client.user} заспавнился нахуй!')
      
      members = '\n '.join([member.name for member in guild.members ]) 
      print(f'Участники: {members}'')           

async def member_join(member):
   await member.create_dm()
   await member.dm_channel.send(
   f'Whassup {member}''
   )

async def prefix(guild_id):
      file = open("prefix.txt", "w")
      for line in line.readlines():
            line = line.split(",")
            if (line[0] == str(guild_id)):
              return line[1]
      return '!'
            
            
@client.event
async def on_message(message):
      get_prefix = prefix(message.guild.id)

      command = message.content.split((' ')[0].replace(get_prefix, ''))
      if (message.content.startswith(get_prefix)):
         if (command == 'vvedi imya commandi plz'):
            pass

         if (command == 'prefix'):
            with open('prefix.txt', 'w') as f:
                newfile = ''
                for line in line.readlines():
                   lineSplit = line.split(',')
                   if (lineSplit[0] == message.guild.id):
                     newfile = str(message.guild.id) + ',' + message.content.split(' ')[1]
                   else:
                     newfile += line
                     f.write(newfile)
                     await message.channel.send('The prefix is now:  `' + message.content.split(' ')[1] + '`')

client.loop.create_task(count())          


if __name__ == "__main__":
  client.run(TOKEN)
