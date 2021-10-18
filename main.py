import discord 
from discord.ext import commands 
import asyncio

client = commands.Bot(command_prefix="!", help_command=None) 

@client.event
async def on_ready(): # When the bot is online
    print("Bot Ready !")
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = "se développer !")) # "Listening to Cool Music !" < in


@client.command(pass_context=True,name="help")
async def help(ctx):
    embed=discord.Embed(
        title="Page d'aide 1/1",
        description="Vous trouverez ici toutes les commandes du bot !",
        color=0x1B26FE
    )
    embed.add_field(
        name="Pour afficher cette liste",
        value="Faîtes `!help`",
    )
    embed.add_field(
        name="Pour activer l'antiraid",
        value="Faîtes `!ar`"
    )
    embed.add_field(
        name="Pour inviter le Bot",
        value="Faîtes `!invite`",
    )
    embed.add_field(
        name="Pour afficher le ping de Charly",
        value="Faîtes `!ping`",
    )
    embed.add_field(
        name="Pour expulser un joueur de votre serveur",
        value="Faîtes `!kick`",
    )
    embed.add_field(
        name="Pour expulser un joueur de votre serveur",
        value="Faîtes `!ban`",
    )
    await ctx.send(embed=embed)

@client.command(pass_context=True,name="ar")
async def help(ctx):
    embed=discord.Embed(
        title="🛡 - AntiRaid activé",
        description="```Vous venez d'activer l'AntiRaid !```",
        color=0x0AAB1D
    )
    await ctx.send(embed=embed)

@client.command(pass_context=True,name="invite")
async def invite(ctx):
    embed=discord.Embed(
        title="📊 - Ping de @Charly#5251",
        description="https://discord.com/api/oauth2/authorize?client_id=783779545495896095&permissions=8&scope=bot",
        color=0x1B26FE
    )
    await ctx.send(embed=embed)

@client.command(pass_context=True,name="ping")
async def ping(ctx):
    embed=discord.Embed(
        title="📊 - Ping de @Charly#5251",
        description=f"Pong : {round(client.latency * 1000)}ms",
        color=0x1B26FE
    )
    await ctx.send(embed=embed)

@client.command(pass_context = True, name = "ban", aliases = ["banuser"])
@commands.has_permissions(ban_members = True) # Peut ban des gens (permissions des rôles Discord)
async def ban (ctx, member : discord.Member, jours : int, *, raison=""):
    await member.ban(reason = raison, delete_message_days = jours)
    e = discord.Embed(
        title = f"{ctx.message.author.name} a banni quelqu'un, soit sage pour ne pas connaître le même sort",
        description = f"Raison du bannissement : {raison}",
        color = 0xff0A00
    )
    e.set_author(name = ctx.message.author.name,icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed=e)

@client.command(pass_context = True, name = "kick", aliases = ["kickuser"])
@commands.has_permissions(kick_members=True) # Peut kick des gens (permissions des rôles Discord)
async def kick (ctx,member : discord.Member, *, raison = ""):
    await member.kick(reason=raison)
    e=discord.Embed(
        title = f"{ctx.message.author.name} a kick quelqu'un, soit sage pour ne pas connaître le même sort.",
        description = f"Raison du kick : `{raison}`",
        color = 0xFF0500
    )
    e.set_author(name = ctx.message.author.name,icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed=e)

client.run("NzgzNzc5NTQ1NDk1ODk2MDk1.X8ftlQ.2Bf1wIjtL8QBiAxCTQrrEPbN3FE")
