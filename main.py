try:
    import discord
    import aiohttp
    import json
    import asyncio
    from discord.ext import tasks, commands
    from discord.ext.tasks import loop
    cache = {}

    bot = commands.Bot(command_prefix='spb!')
    @loop(seconds=10)
    async def server_timer():
        await bot.wait_until_ready()
        global cache
        async with aiohttp.ClientSession() as session:
            async with session.post('https://YOURAPIHERE/YOURENDPOINTHERE', data='{"token":"<token here>"}', headers={'Content-Type': 'application/json'}
                if r.status == 200:
                    js = await r.json()
                    print(js)
                    chanel = bot.get_channel(CHANNEL ID HERE)
                    if js == cache:
                       print('Cached result, ignoring.')
                    else:
                        cache = js
                        print("Cached and continuing")
                        if "response" in js:
                            if js["response"] == "Invalid token.":
                                  print('INVALID TOKEN!')
                            else: 
                                  print('No data.')
                        else:
                            msg = "<@&ROLE ID HERE> SYRSA has released a new video/started streaming! Watch ** " + js['videoTitle'] + " ** at " + js['videoUrl']
                            await chanel.send(msg)
    if __name__ == '__main__':
        server_timer.start()
        print('Bot running.')
        bot.run("<Token here>")
except KeyboardInterrupt:
    print('Keyboard Interrupt detected!')
    print('Bot exited!')
