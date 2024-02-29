import os

API_ID = int(os.environ.get("API_ID", "9344337"))
API_HASH = os.environ.get("API_HASH", "7e55bf98380e416d5de1c4c567395a32")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6173125896:AAGYNgQVJgcZEGL91fGdkgum1D5FigKutTk")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001964234310")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "6040965491"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001931683544')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
