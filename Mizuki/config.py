import json
import os

def get_user_list(config, key):
    with open("{}/Mizuki/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    
    API_ID = 3621722
    API_HASH = "1424ea0f4be038f55137774f9ba81c3d"
    TOKEN = "1931181190:AAFV2z-gZgOmRl5fjjVwv_o9GDrI8NEHew8"
    OWNER_ID = 792109647
    OWNER_USERNAME = "Sawada"
    SUPPORT_CHAT = "AlwaysAngryCat"
    JOIN_LOGGER = (
        -1001535254774
    )
    EVENT_LOGS = (
        -1001535254774
    )
    CASH_API_KEY = (
        "2QNN3MH4J4ZIBFMM"  
    )
    TIME_API_KEY = "UF2KVJK5ALM6"
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
