import discord, os, random, json
from discord.ext import commands
from server import stay_alive

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def ping(ctx):
  await ctx.send('pong')


@bot.command()
async def quote(ctx):
  with open('quotes.json', 'r') as file:
    json_data = json.loads(file.read())
    quote = json_data[random.randint(0, len(json_data) - 1)]

    info = quote.get('i')
    if not info:
      info = ''
    else:
      info = '_(' + info + ')_'

    with open('authors.dat', 'r') as file2:
      authors = file2.readlines()
      author = authors[random.randint(0, len(authors) - 1)]
      info += '\n - ' + author

      embed = discord.Embed(title="Random Quote", description=quote.get('b'))
      embed.add_field(name='"' + quote.get('q') + '"',
                      value=info,
                      inline=False)
      await ctx.send(embed=embed)


bot.run(os.environ['TOKEN'])
stay_alive()
