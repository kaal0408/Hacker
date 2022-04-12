import glob
from System.__init__ import bot
from sys import argv
from telethon import TelegramClient
from System.Config import Var
from System.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from System import CMD_HNDLR


LOAD_MYBOT = Var.LOAD_MYBOT




if len(argv) not in (1, 3, 4):
    bot.disconnect()
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        print("Startup Completed")
    else:
        bot.start()

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Hacker has been deployed! ")

print("Setting up TGBot")
path = "plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Userbot X ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @Murat_30_God !!
                    ᴢʏᴘʜᴇʀ ᴠᴇʀ: V1.0
                    ©Team Shivansh
                ----------------------------------------------------------------------
"""
)
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
#now ok
