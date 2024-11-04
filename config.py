import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22724444")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "d88e1dcdd8c5601832784adfc580442d") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6516534850:AAH-uHTGaxFQ06ZXNbH-z2Sqh1TKoSRFREo") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://vps:vps@cluster0.o4ghvi3.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot1") 

    # Other Configs
    ADMIN = int(os.environ.get("ADMIN", "1361989901"))
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002113925075')) # ⚠️ Required
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
