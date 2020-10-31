import discord
from discord.ext import commands
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
import random
import re


class SkillCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def s(self, ctx, skill: str, mod=0):
        await ctx.message.delete()
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        document_id = '1nMwDuZCXIvx8BDdx1dRIpBn5VDQ6WUwvPS_yv46SwqI'
        sample_range_name = str(ctx.message.author.display_name)+'!A9:E189'
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=document_id, range=sample_range_name).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
        for row in values:
            if row[0] == skill:
                d100 = random.randint(1, 100)
                d00 = int(d100/10)
                target = int(int(row[4])+mod)
                lvl = int(target/10)-d00
                embed = discord.Embed(
                    title=str(ctx.message.author.display_name),
                    description='Würfelt auf ' + skill,
                    colour=discord.Colour.red()
                )
                embed.add_field(name="Werte", value=row[4] + " + " + str(mod), inline=True)
                if target > d100:
                    embed.set_image(url='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.iemoji.com%2Fview%2Femoji%2F56%2Fsmileys-people%2Fthumbs-up&psig=AOvVaw0NzGeQtHHcjs_OUMQFj0CL&ust=1604264161074000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMiMmfPb3-wCFQAAAAAdAAAAABAE')
                    if d100 % 10 == d00 % 10:
                        embed.add_field(name=str(d100), value="Kritischer Erfolg! " + str(lvl) + " Erfolgsgrade", inline=True)
                    else:
                        embed.add_field(name=str(d100), value=str(lvl) + " Erfolgsgrade", inline=True)
                else:
                    if d100 % 10 == d00 % 10:
                        embed.set_image(url='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.iemoji.com%2Fview%2Femoji%2F57%2Fsmileys-people%2Fthumbs-down&psig=AOvVaw3T_RU0uu2GCW6Yg4cl_4oT&ust=1604264282870000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODzz6jc3-wCFQAAAAAdAAAAABAD')
                        embed.add_field(name=str(d100), value="Fataler Patzer! " + str(-1*lvl) + " Misserfolgsgrade", inline=True)
                    else:
                        embed.set_image(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F11%2F29%2Fe1%2F1129e10cb40dd19f12bb3b33e6ef1c2c.png&imgrefurl=https%3A%2F%2Ftr.pinterest.com%2Fpin%2F667447607256690610%2F&tbnid=r5i3w7KBL06ElM&vet=10CA8QxiAoCGoXChMIiPDnxNzf7AIVAAAAAB0AAAAAEAc..i&docid=dt12Sd5wAkjdrM&w=255&h=480&itg=1&q=thumbs%20up&ved=0CA8QxiAoCGoXChMIiPDnxNzf7AIVAAAAAB0AAAAAEAc')
                        embed.add_field(name=str(d100), value=str(-1*lvl) + " Misserfolgsgrade", inline=True)
                await ctx.message.channel.send(embed=embed)
                return

    @commands.command(pass_context=True)
    async def cs(self, ctx, skill: str, mod=0, val=11):
        await ctx.message.delete()
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        document_id = '1nMwDuZCXIvx8BDdx1dRIpBn5VDQ6WUwvPS_yv46SwqI'
        sample_range_name = str(ctx.message.author.display_name)+'!A9:E189'
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=document_id, range=sample_range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        for row in values:
            if row[0] == skill:
                d100 = val
                d00 = int(d100/10)
                target = int(int(row[4])+mod)
                lvl = int(target/10)-d00
                embed = discord.Embed(
                    title=str(ctx.message.author.display_name),
                    description='Würfelt auf ' + skill,
                    colour=discord.Colour.red()
                )
                embed.add_field(name="Werte", value=row[4] + " + " + str(mod), inline=True)
                if target > d100:
                    embed.set_image(url='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.iemoji.com%2Fview%2Femoji%2F56%2Fsmileys-people%2Fthumbs-up&psig=AOvVaw0NzGeQtHHcjs_OUMQFj0CL&ust=1604264161074000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMiMmfPb3-wCFQAAAAAdAAAAABAE')
                    if d100 % 10 == d00 % 10:
                        embed.add_field(name=str(d100), value="Kritischer Erfolg! " + str(lvl) + " Erfolgsgrade", inline=True)
                    else:
                        embed.add_field(name=str(d100), value=str(lvl) + " Erfolgsgrade", inline=True)
                else:
                    if d100 % 10 == d00 % 10:
                        embed.set_image(url='https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.iemoji.com%2Fview%2Femoji%2F57%2Fsmileys-people%2Fthumbs-down&psig=AOvVaw3T_RU0uu2GCW6Yg4cl_4oT&ust=1604264282870000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODzz6jc3-wCFQAAAAAdAAAAABAD')
                        embed.add_field(name=str(d100), value="Fataler Patzer! " + str(-1*lvl) + " Misserfolgsgrade", inline=True)
                    else:
                        embed.set_image(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F11%2F29%2Fe1%2F1129e10cb40dd19f12bb3b33e6ef1c2c.png&imgrefurl=https%3A%2F%2Ftr.pinterest.com%2Fpin%2F667447607256690610%2F&tbnid=r5i3w7KBL06ElM&vet=10CA8QxiAoCGoXChMIiPDnxNzf7AIVAAAAAB0AAAAAEAc..i&docid=dt12Sd5wAkjdrM&w=255&h=480&itg=1&q=thumbs%20up&ved=0CA8QxiAoCGoXChMIiPDnxNzf7AIVAAAAAB0AAAAAEAc')
                        embed.add_field(name=str(d100), value=str(-1*lvl) + " Misserfolgsgrade", inline=True)
                await ctx.message.channel.send(embed=embed)
                return


def setup(bot):
    bot.add_cog(SkillCheck(bot))
