import os, asyncio, telethon, argparse
from telethon import TelegramClient, events
from colorama import Fore, init

parser = argparse.ArgumentParser(description="Scrape messages from a specific user in a Telegram group.")
parser.add_argument("-u", "--user_id", type=int, required=True, help="User ID of the person whose messages you want to scrape.")
parser.add_argument("-o", "--output", type=str, default="user_replies.txt", help="Output file name for the scraped messages.")
args = parser.parse_args()
init()

api_id = ''
api_hash = ''
phone_number = '+' # put the number related to your telegram account in international format

client = TelegramClient('anon', api_id, api_hash, system_version='11', device_model='samsungSM-A715F', lang_code='hi-in')

async def get_user_username(user_id):
    user = await client.get_entity(user_id)
    return user.username

async def scrape_messages(group_id, specific_user_id):
    user_username = await get_user_username(specific_user_id)
    message_count = 0
    user_messages = []

    async for message in client.iter_messages(group_id, reverse=True):
        if isinstance(message.from_id, telethon.tl.types.PeerUser) and message.from_id.user_id == specific_user_id:
            user_messages.append(f"{message.text}\n")
            user_messages.append("------------------\n")
            message_count += 1

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(f"Total number of messages from {user_username}: {message_count}\n\n")
        f.writelines(user_messages)

    print(f'{Fore.CYAN}Scraping completed!')
    os._exit(0)

@client.on(events.NewMessage(pattern='/scrape'))
async def on_scrape_command(event):
    group_id = event.chat_id
    await scrape_messages(group_id, args.user_id)

with client.start(phone=phone_number):
    print(f"{Fore.GREEN}Signed in successfully!")
    client.run_until_disconnected()
