import os, aiohttp, random, tasksio, asyncio
from colorama import Fore, Style



class Client:

    def __init__(self):
        self.Clear = lambda: os.system('cls & mode 80,23')
        self.Clear()
        self.Token, self.Guild = input(f'{Fore.CYAN}{Style.BRIGHT}Insert Token;{Fore.RESET} '), input(f'{Fore.CYAN}{Style.BRIGHT}Insert Guild;{Fore.RESET} ')
        self.Tasks = int(input(f'{Fore.CYAN}{Style.BRIGHT}Enter Amount Of Tasks;{Fore.RESET} '))
        self.Headers = {'Authorization': 'Bot {}'.format(self.Token)}
        self.StatusCodes = [200,201,204]
        self.Api = random.randint(6,9)
        
        

    async def execute(self, members):
        try:
            async with aiohttp.ClientSession(headers=self.Headers) as client:
                async with client.put('https://discord.com/api/v{0}/guilds/{1}/bans/{2}'.format(self.Api, self.Guild, members, )) as response:
                    if response in self.StatusCodes:
                        print('Succesfully Punished User -> {}'.format(members))
                    else:
                        print('Unable To Punish User -> {}'.format(members))
                    return await self.execute(members)
        except Exception:
            print(f'')
            return await self.execute(members)
        


    async def start(self):
        async with tasksio.TaskPool(self.Tasks) as pool:
            while True:
                try:
                    for member in open("data/members.txt").read().splitlines():
                        await pool.put(self.execute(member))
                except Exception:
                    print(f'{Fore.RED}{Style.BRIGHT}There Was An Error, Press -> [Enter] To Exit!')
                    os._exit(1)
        

if __name__ == "__main__":
    client = Client()
    asyncio.get_event_loop().run_until_complete(client.start())
