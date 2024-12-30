import os
from dotenv import *
from discord import Intents, Client, Message

from response import get_response

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message(message, user_message, username):
    if not user_message:
        print('No message')
        return
    
    is_private = user_message[0] == '?'

    if is_private:
        user_message = user_message[1:]

    try:
        response = get_response(user_input=user_message)
        response = f'Hi {username}, thanks for prompt. My response is {response}'
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print(f'{client.event} is running')

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
  
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: {user_message}')
    await send_message(message=message, user_message=user_message, username=username)
    
def main() -> None:
  client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()
