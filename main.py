import discord
from discord.ext import commands
import math
import os
from my_token import token


prefix = "$"  # Set your desired prefix here
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True, self_bot=True)
bot.remove_command("help")




@bot.event
async def on_message(message):
     
    print(f"Message from {message.author}: {message.content}")
    await bot.process_commands(message)  # Process commands alongside message events

@bot.event
async def on_message(message):
    target_channel_id = 1114845892923633684  # Replace with the actual target channel ID
    target_channel = bot.get_channel(target_channel_id)

    if message.channel == target_channel:
        return  # Skip processing for the target channel

    # Process commands for other channels
    await bot.process_commands(message)

    # Send messages to the target channel
    if target_channel:
        msg_content = f"Message from {message.author}: {message.content}"
        await target_channel.send(msg_content)



@bot.event
async def on_voice_state_update(member, before, after):
    channel_id = 1114845892923633684  # Replace with the actual channel ID
    channel = bot.get_channel(channel_id)

    if channel:
        if before.channel != after.channel:
            if after.channel is not None:
                # Member connected to a voice channel
                message = f"{member.name} connected to {after.channel.name}"
                await channel.send(message)
            elif before.channel is not None:
                # Member disconnected from a voice channel
                message = f"{member.name} disconnected from {before.channel.name}"
                await channel.send(message)
        elif before.channel == after.channel and before.channel is not None and after.channel is not None:
            # Member was kicked from a voice channel
            message = f"{member.name} was kicked from {before.channel.name}"
            await channel.send(message)
    else:
        print("The specified channel was not found.")




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

bot.run(token,reconnect=True)
