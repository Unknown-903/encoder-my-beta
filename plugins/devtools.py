from pyrogram import Client as bp , filters , enums
import sys
from config import Config
import os 
import io
import re
import traceback
import time 
import asyncio
import urllib.parse as url_lib
from asyncio import create_subprocess_exec, gather

@bp.on_message(filters.command(['shell']) & filters.user([Config.ADMIN]))
async def shell(app,message):
        msg=await message.reply_text("<b>Pʀᴏᴄᴇssɪɴɢ...</b>",reply_to_message_id=message.id)
        command=message.text.split(maxsplit=1)
        if not len(command) > 1:
            await message.reply_text(f"<b>Gɪᴠᴇ Sʜᴇʟʟ Cᴏᴍᴍᴀɴᴅ...</b>",reply_to_message_id=message.id)
            await msg.delete()
            return
        cmd=command[1]
        stdout, stderr = await bash(cmd, run_code=1)
        err, out = "", ""
        if stderr: err = stderr
        if stdout: out=stdout
        if not stderr and not stdout: out="Success"
        out=err+out
        mg='''<b>• Sʜᴇʟʟ :-
<code>{}</code>

• Oᴜᴛᴘᴜᴛ :- 
<code>{}</code></b>'''.format(cmd , out)
        if len(mg) > 4096:
            f=open('shell.txt','w')
            f.write(mg)
            f.close()
            await message.reply_document('shell.txt',caption='<b>Sʜᴇʟʟ Lᴏɢ</b>',reply_to_message_id=message.id)
            await msg.delete()
            os.remove('shell.txt')
        else: 
            await message.reply_text(mg,reply_to_message_id=message.id)
            await msg.delete()

@bp.on_message(filters.command(['eval']) & filters.user([Config.ADMIN]) )
async def eval_(app,message):
        msg=await message.reply_text("<b>Pʀᴏᴄᴇssɪɴɢ...</b>",reply_to_message_id=message.id)
        command=message.text.split(maxsplit=1)
        if not len(command) > 1:
            await message.reply_text(f"<b>Gɪᴠᴇ Sᴏᴍᴇ Pʏᴛʜᴏɴ Cᴏᴅᴇ</b>",reply_to_message_id=message.id)
            await msg.delete()
            return
        cmd=command[1]
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        try:
            await aexec(cmd,app,message)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        mg='''<b>• Eᴠᴀʟ :-
<code>{}</code>

• Rᴇsᴜʟᴛ :- 
<code>{}</code></b>'''.format(cmd , evaluation)
        if len(mg) > 4096:
            f=open('eval.txt','w')
            f.write(mg)
            f.close()
            await message.reply_document('eval.txt',caption='<b>Eᴠᴀʟ Lᴏɢ</b>',reply_to_message_id=message.id)
            await msg.delete()
            os.remove('eval.txt')
        else: 
            await message.reply_text(mg,reply_to_message_id=message.id)
            await msg.delete()
        db.sync_changes()

async def aexec(code,app,message):
    exec(("async def __aexec(app,message): " + "".join(f"\n {l}" for l in code.split("\n"))))
    return await locals()["__aexec"](app,message)

async def bash(cmd,run_code=0):
    process = await asyncio.create_subprocess_shell(cmd,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip() or None
    out = stdout.decode().strip()
    if not run_code and err:
        if match := re.match("\/bin\/sh: (.*): ?(\w+): not found", err): return out, f"{match.group(2).upper()}_NOT_FOUND"
    return out, err