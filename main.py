import os, httpx, aiohttp, asyncio, time, tasksio, random, shutil
from colorama import Fore, Style


class Client:
    def __init__(self):
        self.Clear = lambda: os.system('cls & mode 80,23'); self.Clear()
        self.columns = shutil.get_terminal_size().columns
        self.token = input(f'{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET} Insert Token : {Fore.RESET}')
        self.headers = {'Authorization': "Bot {0}".format(self.token)}
        self.api = random.randint(6, 9)

        response = httpx.get('https://discordapp.com/api/v9/users/@me', headers=self.headers)
        if response.status_code in (200, 201, 204):
            print(f'{Fore.LIGHTMAGENTA_EX}[+]{Fore.RESET} Token Is Validated')
            time.sleep(1.5)
            self.Clear()
        else:
            self.Clear()
            print(f'{Fore.LIGHTRED_EX}{Style.DIM}[–]{Fore.RESET} Token Is Non Invalidated')
            os._exit(2)

        self.titlecard()
        print('')
        self.guild = input(f'        {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}[+]{Fore.RESET} Input Guild ID > {Fore.RESET}')
        self.tasks = int(input(f'        {Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}[+]{Fore.RESET} Enter Amount Of Tasks > {Fore.RESET}'))
        if self.tasks >= 5000: 
            print(f'        {Fore.RED}[–]{Style.BRIGHT}{Fore.RESET} Tasks Cannot Be Over The Range Of 5000 {Fore.RESET}')
            os._exit(1)


    def titlecard(self):
        print(f'''{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}
     ██████╗ ███╗   ███╗███████╗███╗   ██╗
    ██╔═══██╗████╗ ████║██╔════╝████╗  ██║
    ██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║
    ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║
     ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝{Fore.RESET}''')

    async def execute(self, members):
        try:
            async with aiohttp.ClientSession(headers=self.headers) as client:
                async with client.put('https://discord.com/api/v{0}/guilds/{1}/bans/{2}'.format(self.api, self.guild, members)) as response:
                    if response in (200, 201, 204):
                        print(f'{Fore.MAGENTA}{Style.BRIGHT}Succesfully Punished User -> {Fore.RESET}{members}'.center(self.columns))
                    else:
                        print(f'{Fore.MAGENTA}{Style.BRIGHT}Unable To Punish User -> {Fore.RESET}{members}'.center(self.columns))
                    return await self.execute(members)
        except Exception:
            print(f'{Fore.RED}[–]{Style.BRIGHT}Error, Somthing Went Wrong.'.center(self.columns))
            return await self.execute(members)

    async def start(self):
        async with tasksio.TaskPool(self.tasks) as pool:
            while True:
                try:
                    for member in open("data/members.txt").read().splitlines():
                        await pool.put(self.execute(member))
                except Exception:
                    print(f'{Fore.RED}{Style.BRIGHT}There Was An Error, Press -> [Enter] To Exit!'.center(self.columns))
                    os._exit(1)

if __name__ == "__main__":
    client = Client()
    asyncio.get_event_loop().run_until_complete(client.start())
