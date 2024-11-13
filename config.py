import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22409622")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "16353e2a4d45ff8be4a2037cca158749") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7057949515:AAHIxldaPMNEMZnNHYlutV6qDHg-y2P0KVs") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002021288035') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Dschut:Divyansh03#@cluster0.iwjda.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","dschut") 

    # Other Configs
    ADMIN = int(os.environ.get("ADMIN", "1119579816 6427494689 6590736993 1785065025 6315792232 1735152469 5574593875 7211073530"))
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002332764222')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e9d1f661f58c7d6aa4370.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
