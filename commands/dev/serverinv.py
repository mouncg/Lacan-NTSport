from discord.utils import get
import discord
from discord.ext import commands
class Command(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def serverinv(self, ctx, channel: discord.channel = None):
      permitted = [
        #Try2Win4Glory
          505338178287173642,
        #adl212
          396075607420567552
      ]
      if ctx.author.id not in permitted:
        return await ctx.send('Ure no dev bro')
      else:
        channel = 821719720867659786
        print(discord.channel)
        discord.channel = channel
        print(discord.channel)
        if channel is None:  
          # No channel tagged, create invite for current channel
          invitelink = await ctx.channel.create_invite(max_age=300, max_uses=100)
        else:
          invchannel = get(self.client.get_all_channels(), id=channel)
          invitelink = await invchannel.create_invite(max_age=300, max_uses=100)
          #invitelink = await invchannel.create_invite(max_age=300, max_uses=100)
        await ctx.send(invitelink)
    '''async def serverinv(self, ctx):
      permitted = [505338178287173642, 396075607420567552]
      if ctx.author.id not in permitted:
        print('not permitted')
        return
      else:
        send_channel = get(self.client.get_all_channels(), id=829828396695420949)
        for guild in self.client.guilds:
          channel = 803938544175284244 #guild.channels[0]
          try:
           invite = await channel.create_invite(max_age=300, max_uses=1000)
          except:
            await ctx.send('error')
            break
          else:
            await send_channel.send(invite.url)'''
def setup(client):
    client.add_cog(Command(client))