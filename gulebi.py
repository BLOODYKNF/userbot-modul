from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Heart's"}
	@loader.owner
	async def heartscmd(self, message):
		for _ in range(10):
			for heart in ['โค', '๏ธ๐งก', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', 'โฃ๏ธ', '๐', '๐', '๐', '๐ฅฐ', '๐', '๐', '๐ค', '๐', '๐ค']:
				await message.edit(heart)
				await sleep(0.3)
