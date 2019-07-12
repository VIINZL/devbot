#lets hope this turns out great
import discord
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '.')
question = ('none')
@client.event
async def on_ready():
    print('Bot now ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms.')
    print(f'{ctx.author} has used ping command.')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    if question is 'none':
        await ctx.send('Sorry you need to add a question for me to answer!')
        return
    else:
        responses = ['ja', 'nö', 'werweiß', 'morgen evt...', 'nattülliiiich']
        #answer = choice(responses)
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('NTk5MDUxNzU1MTU3OTc5MTU2.XSfkcA.jA0MjlICbSvLJg5Bs1yNWtI1qZA')
