import asyncio
import redis
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import BOT_TOKEN

loop = asyncio.get_event_loop_policy()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

users_db = redis.StrictRedis(host='localhost', port=6379, db=0, password=None, socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)

ADMIN_LIST_COMMANDS = ['send_everyone', 'admin', 'backup_users_id', 'bot_stat', 'update_limitation']

TIKTOK_LINK = 'https://vm.tiktok.com/'
TIKTOK_LIST = ['tiktok.com/@', 'https://', 'likee.video', 'funimate.com/p/']
TIKTOK_HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36'}


class AdminSendEveryOne(StatesGroup):
    post = State()
    ask_send = State()


class UpdateLimitation(StatesGroup):
    user_id = State()