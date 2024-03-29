from .. import loader, utils
import asyncio
import requests
import json

from telethon.tl.types import *
# requires: requests


@loader.tds
class BCheckMod(loader.Module):
    """Bulk chat phone number leakage check"""
    strings = {
        "name": "BCheck",
       'checking': '<b>მოწმდება ჩატი...</b>',
       'check_in_progress': 'მიმდინარეობს შემოწმების პროცესი...',
       'search_header': "ძიების შედეგი: ",
       'not_found': "შედეგი: <code>ვერ მოიძებნა</code>",
       'check_started': 'დაიწყო ჩატის შემოწმება'
    }

    async def bcheckcmd(self, message):
        """შეამოწმე გაჟონილი ნომრები"""
        await utils.answer(message, self.strings('მოწმდება'))

        check_result = self.strings('search_header', message)

        async for user in message.client.iter_participants(message.to_id):
            dt = requests.get(
                'http://api.murix.ru/eye?uid=' + str(user.id)).json()
            dt = dt['data']
            if 'NOT_FOUND' not in dt:
                check_result += "\n    <a href=\"tg://user?id=" + str(user.id) + "}\">" + (str(
                    user.first_name) + " " + str(user.last_name)).replace(' None', "") + "</a>: <code>" + dt + "</code>"
                await message.edit(check_result + '\n\n' + self.strings('check_in_progress'))
            await asyncio.sleep(1)

        if check_result == self.strings('search_header', message):
            check_result = self.strings('not_found', message)

        await message.edit(check_result)

    async def bchecksilentcmd(self, message):
        await message.delete()
        msg = await message.client.send_message('me', self.strings('check_started', message))
        check_result = self.strings('search_header', message)
        async for user in message.client.iter_participants(message.to_id):
            f = open("result.txt", "a", encoding="utf-8")
            dt = requests.get(
                'http://api.murix.ru/eye?v=1.2&uid=' + str(user.id)).json()
            dt = dt['data']
            if 'NOT_FOUND' not in dt:
                f.write("First name: " + (str(user.first_name) + "\nLast name: " + str(user.last_name)).replace(' None', "") + "\nUsername: " + str(user.username) + "\nID: " + str(user.id) + "\nPhone: " + dt + "\n\n")
            f.close()
            await asyncio.sleep(1)
        f = open("result.txt", "a")
        f.write("By Bloodyofc")
        f.close()
