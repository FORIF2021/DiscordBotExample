import discord
import asyncio

class Timer(discord.Client):
    async def on_ready(self):
        print(f'Logged in as { self.user } (ID: { self.user.id })')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!timer '):
            time = int(message.content[ 7: ])

            if time < 0:
                await message.add_reaction('😡')
                return

            nmsg = await message.channel.send(str(time))

            for t in range(time - 1, 0, -1):
                await nmsg.edit(content = str(t))
                await asyncio.sleep(1.0)

            await nmsg.edit(content = 'Time\'s up!', delete_after = 1.0)
            await message.delete()

if __name__ == '__main__':
    token_file = open('token', 'r')
    token      = token_file.read()
    token_file.close()
    client     = Timer()
    client.run(token)