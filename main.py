from keep_alive import keep_alive
import os
import discord
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

client = discord.Client()




# COINMARKETCAP.COM API TO GET CRYPTO PRICES (FUNCTION)
def price_p():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    my_secretcmc = os.environ['cmcAPI']  # use apifile.env if program running outside replit
    parameters = {

        "symbol": "DOGE",

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': my_secretcmc,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        i = response.json()
        result_format = json.dumps(i, indent=2)
        index1 = result_format.index('price')
        index2 = result_format.index('volume_24h')
        stat = result_format[index1:index2]
        pricelist = []
        pricelist.append(stat)
        for i in pricelist:
            format_a = i.replace(',', '').replace('"', '').replace('price', '').replace(':', '')
        format_float = float(format_a)
        round_price = round(format_float, 3)

        return round_price




    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


@client.event
async def on_ready():
    print('Chicken bot is logged IN --BY SHAHEN--{0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$doge'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="DOGE",
            value=price_p(),
            inline=False,

        )
        await message.channel.send(embed=avc)


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
