from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.pol", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       

    await event.edit("π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅")
    await asyncio.sleep(0.5)
    await event.edit("π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄")
    await asyncio.sleep(0.5)
    await event.edit("π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅")
    await asyncio.sleep(0.5)
    await event.edit("`**π¨π¨ΠΠΈΠΊΠΎΠΌΡ Π½ΠΈ Ρ ΠΌΠ΅ΡΡΠ°! ΠΡΠΈΠ±ΡΠ»Π° ΠΏΠΎΠ»ΠΈΡΠΈΡπ¨π¨...ΠΠΎΡΠΎΠ²Ρ Π²Π΅ΡΠΈΡΠΊΠΈ, ΡΡΠ½ΠΎΠΊ.`**")
