import asyncio
import logging
import sys
from os import getenv
import re

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from bot.service_layer.services import APIClient

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message and message.from_user and message.from_user.username:
        client = APIClient()
        await client.create_user(
            user_id=message.from_user.id, telegram_nickname=message.from_user.username
        )
        await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')


data_regex = re.compile(
    r'^[^\d]*(\d{2,3})(?:[^\d]+(\d{2,3}))(?:[^\d]+(\d{2,3}))?\s*[^\d]*$', re.MULTILINE
)


def process_text(s: str) -> list[tuple[str, ...]]:
    return data_regex.findall(s)


@dp.message()
async def echo_handler(message: Message) -> None:
    if not message.text or not message.from_user:
        return
    try:
        if results := process_text(message.text):
            print(results)
            client = APIClient()
            measurements = [
                {'up': r[0], 'down': r[1], 'pulse': r[2] if len(r) > 1 + 1 else 0}
                for r in results
            ]
            print(measurements)
            await client.create_pressure_measurements_for_user(
                message.from_user.id, measurements
            )
            await message.answer(f'{results}')
            return
        await message.answer('no result sorry!')

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer('Nice try!')


async def main() -> None:
    load_dotenv()
    # Bot token can be obtained via https://t.me/BotFather
    token = getenv('BOT_TOKEN', None)
    if not token:
        print('set a token $BOT_TOKEN')
        sys.exit(1)
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
