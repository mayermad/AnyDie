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
                await ctx.message.channel.send(ctx.message.author.mention + ', Du würfelst auf ' + skill + ' gegen die ' + row[4] + " + " + str(mod))
                d100 = random.randint(1, 100)
                d00 = int(d100/10)
                target = int(int(row[4])+mod)
                lvl = int(target/10)-d00
                if target > d100:
                    if d100 % 10 == (d100/10) % 10:
                        await ctx.message.channel.send("Kritischer Erfolg")
                    await ctx.message.channel.send("Du hast eine " + str(d100) + " gewürfelt und damit " + str(lvl) + " Erfolgsgrade")
                else:
                    if d100 % 10 == (d100/10) % 10:
                        await ctx.message.channel.send("Fataler Patzer")
                    await ctx.message.channel.send("Du hast eine " + str(d100) + " gewürfelt und damit " + str(-1*lvl) + " Misserfolgsgrade")
        return


def setup(bot):
    bot.add_cog(SkillCheck(bot))
