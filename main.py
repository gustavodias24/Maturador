from colorama import Fore, Style
from alright import WhatsApp
from random import shuffle
from time import sleep
from random import randint
from undetected_chromedriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import json
from SenderNewClientes import BotStart


class MatureBot:
    def __init__(self):
        # Tempo de espera
        self.TEMPO_MAX = 9
        self.TEMPO_MIN = 2

        self.list_profiles = os.listdir(os.path.join(
            os.getcwd(), 'profiles'
        ))

        shuffle(self.list_profiles)

        self.list_receptor = os.listdir(os.path.join(
            os.getcwd(), 'profiles'
        ))

        with open(os.path.join(os.getcwd(), 'conversas.json')) as file:
            self.all_conversas = json.loads(file.read())
            file.close()

        self.responseAI = ""
        self.falaAmigo1 = []
        self.falaAmigo2 = []

        self.navAmigo1 = None
        self.navAmigo2 = None
        self.nuAmigo1 = None
        self.nuAmigo2 = None

        self.whatsAmigo1 = None
        self.whatsAmigo2 = None

    """
        utils
    """

    def findXpath(self, xpath, nav, time=False, seconds=2):

        tempo = seconds

        while True:
            try:
                return nav.find_element(By.XPATH, xpath)
            except NoSuchElementException or StaleElementReferenceException:
                if time:
                    if tempo <= 0:
                        return False
                    tempo -= 1
                    sleep(2)

    def getNumero(self, nav):
        while True:
            try:
                elm = self.findXpath('//*[@id="app"]/div/div/div[3]/header/div[1]/div/img', nav)
                sleep(1.3)
                elm.click()
                sleep(2.3)

                numero = ""

                while numero == "":
                    numero = self.findXpath(
                        '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[3]/div[3]/div[2]/div/div[1]',
                        nav).text
                return numero
            except:
                sleep(5)

    def amigo1(self):
        for fala in self.falaAmigo1:

            falaReal = fala.replace("\n", "")
            print(Fore.YELLOW + "amigo1:" + falaReal)

            self.whatsAmigo1.send_message(falaReal)

            if len(self.falaAmigo1) > 0:
                self.falaAmigo1.pop(0)

            sleep(randint(self.TEMPO_MIN, self.TEMPO_MAX))
            self.amigo2()

    def amigo2(self):
        for fala in self.falaAmigo2:

            falaReal = fala.replace("\n", "")
            print("amigo2:" + falaReal)

            self.whatsAmigo2.send_message(falaReal)

            if len(self.falaAmigo2) > 0:
                self.falaAmigo2.pop(0)
            else:
                break
            sleep(randint(self.TEMPO_MIN, self.TEMPO_MAX))

            self.amigo1()

    def formatar_number(self, n):
        formatacao_n = n
        for sy in ["+", " "]:
            formatacao_n = formatacao_n.replace(sy, "")
        print(Fore.BLUE + "Número: " + formatacao_n)
        return formatacao_n

    def instanciarDriver(self, amigo, path):
        options = ChromeOptions()
        options.add_argument("--user-data-dir={}".format(path))

        erro = False
        if amigo == 2:
            try:
                self.navAmigo2 = Chrome(
                    driver_executable_path=ChromeDriverManager().install(),
                    options=options
                )
            except:
                erro = True
        else:
            try:
                self.navAmigo1 = Chrome(
                    driver_executable_path=ChromeDriverManager().install(),
                    options=options
                )
            except:
                erro = True

        if erro:
            return False

    """
        iniciarConversa
        Retorna nada, ...
    """

    def iniciarConversa(self):
        while True:

            shuffle(self.list_profiles)

            for amigo1 in self.list_profiles:

                print(Style.BRIGHT + Fore.MAGENTA + amigo1)

                self.instanciarDriver(1, os.path.join(
                    os.getcwd(),
                    "profiles",
                    amigo1,
                    "wpp"
                ))
                if self.navAmigo1:

                    self.whatsAmigo1 = WhatsApp(browser=self.navAmigo1)

                    self.navAmigo1.get("https://web.whatsapp.com/")
                    self.nuAmigo1 = self.formatar_number(self.getNumero(self.navAmigo1))

                    limit = 0
                    shuffle(self.list_receptor)
                    for amigo2 in self.list_receptor:
                        if amigo2 != amigo1:
                            print(Style.BRIGHT + Fore.MAGENTA + amigo2)
                            self.instanciarDriver(2, os.path.join(
                                os.getcwd(),
                                "profiles",
                                amigo2,
                                "wpp"
                            ))

                            if self.navAmigo2:

                                self.whatsAmigo2 = WhatsApp(browser=self.navAmigo2)

                                shuffle(self.all_conversas)

                                conversa_completa = self.all_conversas[0]

                                self.falaAmigo1 = conversa_completa["Amigo1"]
                                self.falaAmigo2 = conversa_completa["Amigo2"]

                                self.navAmigo2.get("https://web.whatsapp.com/")
                                self.nuAmigo2 = self.formatar_number(self.getNumero(self.navAmigo2))

                                print(self.falaAmigo1)
                                print(self.falaAmigo2)

                                self.whatsAmigo2.find_user(self.nuAmigo1)
                                self.whatsAmigo1.find_user(self.nuAmigo2)

                                self.amigo1()

                                self.navAmigo2.close()

                                # enviar mensagem para um outro cliente
                                RANGE = 2

                                with open(os.path.join(os.getcwd(), 'contatos.txt')) as file:

                                    allLines = file.read().split("\n")

                                    try:
                                        allLines.remove('')
                                    except ValueError:
                                        continue

                                    if allLines:
                                        numeros = allLines[0:RANGE]

                                        with open(os.path.join(os.getcwd(), 'contatos.txt'), "w") as fileUpdate:
                                            fileUpdate.writelines([l + "\n" for l in allLines[RANGE:]])

                                        for numero in numeros:
                                            BotStart(self.navAmigo1).senderMsg(numero)
                                    else:
                                        print(Fore.CYAN + "NÃO EXISTE MAIS NOVOS CONTATOS PARA ENVIAR!")

                                limit += 1
                                if limit >= 3:
                                    break

                self.navAmigo1.close()

    def criarProfile(self, nProfile):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profiles", "profile{}".format(nProfile), "wpp")
        opt = ChromeOptions()
        opt.add_argument(
            r"--user-data-dir={}".format(profile))

        nav = Chrome(driver_executable_path=ChromeDriverManager().install(), options=opt)
        input(Fore.GREEN + "Profile criado!")
        nav.close()


if __name__ == "__main__":
    while True:
        try:
            menu = int(input(
                """
                    Maturador de números
                [ 1 ] Criar profile
                [ 2 ] Iniciar maturação
                
                R =
                """)
            )
        except:
            print(Fore.RED + "error")
            break

        if menu == 2:
            MatureBot().iniciarConversa()
        else:
            MatureBot().criarProfile(input(Fore.CYAN + "alias: "))
