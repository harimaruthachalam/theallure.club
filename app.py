import os
from dotenv import *
from discord import Intents, Client, Message
import requests

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
        payload = {'text' : user_message}
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post('http://13.60.173.92:8001/', json=payload, headers=headers)
        print(response.json()['message'])
        # response = get_response(user_input=user_message)
        response = f'Hi {username}, \n \
**Disclaimer:** I am using ben1t0/tiny-llm:latest (5.7MB model) and my language model is rudimentry.\n\n \
My response is {response.json()["message"]}'
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
