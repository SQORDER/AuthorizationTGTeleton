import asyncio
from telethon import TelegramClient, events
api_id = 22276461
api_hash = 'eda5f52cdb6c7a1ba62719c016774dcd'
session_name = './sessions/org' #Session name.
async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        me = await client.get_me()
        phone_number = me.phone
        print('Phone : +'+phone_number)
        print('Waiting Code . . .')
        @client.on(events.NewMessage(from_users=777000))
        async def handle_message(event):
            print("Telegram :")
            print(event.message.text)
        await client.run_until_disconnected()
if __name__ == '__main__':
    asyncio.run(main())

