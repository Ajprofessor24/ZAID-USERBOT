import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "14803116")) #optional
API_HASH = getenv("API_HASH", "77ee95a3a666d8ef028a586e5d06ac54") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1923770971", "5505731056").split()))
OWNER_ID = int(getenv("OWNER_ID", "5219332255"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Human:Human@cluster0.ggj8ryn.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5849049902:AAHQiyDZNXZAD1Oso_mBpU8EM-FJArLUI6I")
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/bbd543de5173d4b7583db.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "Baap aa gye wapas")
PM_LOGGER = getenv("PM_LOGGER", "1001779659736")
LOG_GROUP = getenv("LOG_GROUP", "1001885932510")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAJBXFTmPPIY5byk1twMpaRJ28v0wf1Km1tfJsEv3WBWEXWBewt_r4U4qH-FIVtY7X0dEDcJah534W9J17mAQC6nT0LoC_iJmryDHJRuU3Tr_cDjn0CT2BapTmOZhn9Nn0QoAGQpdJSz0cIeh5tprTNuwU5dp5r_G-CYVmNxt2dRLg2bvDLC2xutxWdmOTNgwxJ0q9OsgVu_bJXpztOtRQnQmSQUkho1PI7NUGp_bsjyEPdSyjkOR9IX2WfpMVhzXaWm9Vvhxf9SvzVvdwzRQabd57ShhtBHFk4e3hlzMNIuafJrVgMeMeOgUke3QAttedjIf-ZkDgcfL3wDDDfJGFygAAAAE3GLCfAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
