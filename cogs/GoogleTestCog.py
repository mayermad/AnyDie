import discord
from discord.ext import commands
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
DOCUMENT_ID = '1nMwDuZCXIvx8BDdx1dRIpBn5VDQ6WUwvPS_yv46SwqI'
SAMPLE_RANGE_NAME = 'Durak!A9:E189'


class GoogleTestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self, ctx):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=DOCUMENT_ID, range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
        await ctx.message.channel.send('Test um bestimmten skill auszugeben')
        for row in values:
            if row[0] == "Pick Lock":
                await ctx.message.channel.send('%s : %s' % (row[0], row[4]))
        return


def setup(bot):
    bot.add_cog(GoogleTestCog(bot))
