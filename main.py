import discord
from discord.ext import commands
import math
import os


prefix = "$"  # Set your desired prefix here
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True, self_bot=True)
bot.remove_command("help")




@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")
    await bot.process_commands(message)  # Process commands alongside message events

@bot.command()
async def math(ctx, *args):
    if len(args) == 0:
        await ctx.send("Please provide an expression to evaluate.")
        return
    
    expression = " ".join(args)
    
    try:
        result = eval(expression)
        await ctx.send(f"Result: {result}")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def customhelp(ctx):
    # Customize the help message here
    help_message = "$math -calculates simple equations\n$shutdown -shutdowns bot you need a special permission to do that\n$report -writes report to the creator of the bot"
    await ctx.send(help_message)

bot.owner_id= owner_id=584365630791090192

@bot.command()
async def shutdown(ctx):
    if ctx.author.id != owner_id:
        await ctx.send("You are not authorized to use this command.")
    else:
        await ctx.send("Shutting down...")
        await bot.close()

@bot.command()
async def report(ctx, *, message: str):
    owner = await bot.fetch_user(owner_id)
    if owner is None:
        await ctx.send("Failed to send the report. Please try again later.")
        return

    await owner.send(f"Report from {ctx.author} (ID: {ctx.author.id}):\n{message}")
    await ctx.send("Your report has been sent to the bot owner.")
@bot.event
async def on_ready():
      print(f"Bot is online and ready. Bot owner: {bot.owner_id}")

bot.run('MTExNDgyMzYxNjg1NzY0OTE5Mg.G2f7yx._v00_D3FehztBCbmEpz49X1Dr5YD3IpecIPJYE',reconnect=True)