from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os
from undetected_chromedriver import Chrome, options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoAlertPresentException, \
    ElementClickInterceptedException
from pymongo import MongoClient
from colorama import Fore, Style
from random import randint
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from alright import WhatsApp
from random import shuffle
import pyperclip


class BotStart:
    def __init__(self):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profiles", "profile1", "wpp")
        opt = options.ChromeOptions()
        opt.add_argument(
            r"--user-data-dir={}".format(profile))

        client = MongoClient(host="172.17.0.2", port=27017)

        self.database = client.dbWppBot2

        self.col = self.database.contactsVendasInscritos

        self.nav = Chrome(driver_executable_path=ChromeDriverManager().install(), options=opt)

    def rpc(self, s):
        for sy in ["+", "-", "estádigitando…", " "]:
            s = s.replace(sy, "")
        return s

    def get_hora(self, tempo):
        if 0 <= tempo <= 4:
            buceta = "Boa noite"
        elif 5 <= tempo <= 12:
            buceta = "Bom dia"
        elif 13 <= tempo <= 17:
            buceta = "Boa tarde"
        elif tempo > 17:
            buceta = "Boa noite"
        else:
            buceta = "Olá tudo bem?"
        return buceta

    def findXpath(self, xpath, time=False, seconds=2):

        tempo = seconds

        while True:
            try:
                return self.nav.find_element(By.XPATH, xpath)
            except NoSuchElementException or StaleElementReferenceException:
                if time:
                    if tempo <= 0:
                        return False
                    tempo -= 1
                    sleep(2)

    '''
        Funfando legal,
        pega os contatos salva no db mongo e no arquivo .txt para
        realizar o envio das msg, limitando se necessário!
    '''

    def getContact(self):
        self.switchProfile("profile2")
        self.nav.get("https://web.whatsapp.com/")

        self.findXpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')

        list_add = []
        total = 0
        inseridos = 0
        while True:

            # Xpath dos contatos
            contacts = self.findXpath('//*[@id="main"]/header/div[2]/div[2]/span').get_property("title").split(",")

            for contact in contacts:
                contactClear = self.rpc(contact)
                print(Fore.MAGENTA + contactClear)
                if contactClear != "Você":
                    if "55" in contactClear:
                        if not self.col.find_one({"number": contactClear}):
                            with open(f"{os.path.dirname(__file__)}/datas/contacts.txt", "a+") as file:
                                list_add.append(
                                    {"number": contactClear}
                                )
                                print(Fore.GREEN + f"{contactClear} foi listado.")
                                file.write(contactClear + "\n")
                                file.close()
                        else:
                            print(Fore.RED + f"{contactClear} já foi listado.")
                    else:
                        print(Fore.RED + "Número gringo")
                else:
                    print(Fore.RED + "Sou eu mesmo")

            if len(list_add) > 0:
                inseridos = len(list_add)
                total += len(list_add)
                self.col.insert_many(list_add)
                list_add.clear()
            else:
                print(Fore.RED + "Lista vazia!")

            if input(Fore.CYAN + f"{inseridos} inseridos - {total} no total - next ") == "sair":
                print(Fore.RED + "STOP...")
                break
            inseridos = 0

    def clearDatabase(self):
        print(Fore.RED + "Deletando...")
        self.col.delete_many({})
        print(Fore.GREEN + "Pronto!")

    def selectFala(self):
        tardeOuNoite = self.get_hora(int(str(datetime.now().time()).split(":")[0]))
        # Divulgar venda Inscritos

        text1 = f"""💬 Oi! { tardeOuNoite },
Estamos aqui para ajudar seu conteúdo na internet a brilhar. Quer saber mais sobre nossos serviços de divulgação? 🤔

Acesse o nosso site👇
https://compartilhatube.net/
O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
         """

        text2 = f"""
        { tardeOuNoite }🚀 
Quer aumentar sua presença online e alcançar mais público? Nós temos a solução ideal para você! 💡 Conheça nossos serviços de divulgação de conteúdo na internet. 😎 Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
        """

        text3 = f"""{ tardeOuNoite }
💻 Seu conteúdo na internet merece destaque! Com nossa equipe especializada, alcançamos resultados eficazes e garantimos seu sucesso online. Tem interesse em conhecer mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text4 = f"""🤗 Oi! { tardeOuNoite }, 
Estamos aqui para transformar a presença do seu conteúdo na internet. Quer aumentar seu engajamento e visibilidade online? 😎 Conheça nossos serviços agora mesmo! Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text5 = f"""{ tardeOuNoite }
🔥 Seu conteúdo na internet precisa de mais visibilidade? Nós temos a solução perfeita! Com nossos serviços de divulgação, alcançamos resultados eficientes e garantimos seu sucesso online.😎 Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text6 = f"""{ tardeOuNoite }💡
Quer aprimorar a imagem do seu conteúdo na internet? Nós temos a solução ideal para você! Com nossa equipe especializada, aumentamos seu engajamento e visibilidade online. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text7 = f"""Olá { tardeOuNoite }🤗!
Nós da equipe de divulgação de conteúdo na internet estamos aqui para transformar a presença do seu conteúdo online. Quer aumentar seu sucesso e alcançar mais público? 😎 Conheça nossos serviços agora mesmo! Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text8 = f"""{ tardeOuNoite } 💻
Quer destacar o seu conteúdo na internet? Nós temos a solução perfeita para você! Com nossos serviços de divulgação, garantimos resultados eficazes e aprimoramos sua imagem digital. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text9 = f"""{ tardeOuNoite } 🚀
Está procurando uma forma de aumentar a presença do seu conteúdo na internet? Nós temos a solução ideal para você! Com nossa equipe especializada, alcançamos resultados eficientes e garantimos seu sucesso online. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text10 = f"""🔥 {tardeOuNoite},
Torne-se um influenciador de sucesso no YouTube🎥 com a ajuda de nossos inscritos reais e engajados. 60 dias de reposição garantidos. Pergunte sobre preço. 🚀📈
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        return [[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10][randint(0, 9)]]

    def sendEmoji(self, text):
        elem = self.findXpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        try:
            act = ActionChains(self.nav)
            pyperclip.copy(text)
            elem.click()
            act.key_down(Keys.CONTROL).key_down("v").key_up(Keys.CONTROL).perform()
            elem.send_keys(Keys.ENTER)
        except ElementClickInterceptedException:
            self.senderMsg(text)

    def senderMsg(self, nu):
        try:
            whats = WhatsApp(browser=self.nav)

            print(Fore.GREEN + "Enviando mensagens...")

            falaBot = self.selectFala()
            
            whats.find_user(nu)
            self.sendEmoji(falaBot[0])
            sleep(randint(20, 35))

        except:
            try:
                self.nav.switch_to.alert.send_keys(Keys.ENTER)
                sleep(2.5)
            except NoAlertPresentException:
                sleep(1)

            sleep(10)
            self.senderMsg(nu)



    def entryGroups(self):


        with open(f"{os.path.dirname(__file__)}/datas/grupos.txt", "r+") as gruposFile:
            dict_aux = dict.fromkeys(gruposFile.readlines())

            for gp in list(dict_aux):
                self.nav.get("https://www.zapgrupos.com/grupos/participar/canaisyoutube/{}/zap/".format(gp))

                soup = BeautifulSoup(self.nav.page_source, 'html.parser')

                for link in soup.findAll('a'):
                    if '/grupos/entrargrupowpp.php?idt=' in link.get("href"):
                        self.nav.get("https://www.zapgrupos.com{}".format(link.get("href")))

                        trys = 0
                        while True:
                            try:
                                sleep(3)
                                self.nav.find_element(By.XPATH, '//*[@id="app"]/div/span['
                                                                '2]/div/div/div/div/div/div/div['
                                                                '2]/div/div[2]').click()
                                sleep(2)
                                break
                            except:
                                if trys > 5:
                                    break
                                trys += 1
                                sleep(4)

    def finish(self):
        self.nav.close()
        print(Fore.RED + "...bye!" + Style.RESET_ALL)

    def switchProfile(self, nProfile):
        print(Fore.BLUE + "Trocando profile...")
        self.nav.close()
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profiles", nProfile, "wpp")
        opt = options.ChromeOptions()
        opt.add_argument(
            r"--user-data-dir={}".format(profile))

        self.nav = Chrome(driver_executable_path=ChromeDriverManager().install(), options=opt)
        print(Fore.GREEN + "Profile trocado!")

    def clearContacts(self):
        os.system("rm {}".format(os.getcwd() + "/execucoes/datas/contacts.txt"))
        os.system("touch {}".format(os.getcwd() + "/execucoes/datas/contacts.txt"))
        print(Fore.GREEN + "Limpo ;)")
        sleep(1)

    def startPreAutomatic(self):
        tiverNumero = True

        profiles = os.listdir(
            os.path.join(
                os.getcwd(),
                "profiles"
            )
        )
        
        shuffle(profiles)

        while tiverNumero:

            for profile in profiles:
                print(Fore.MAGENTA + Style.BRIGHT + "Profile atual: " + profile)
                self.switchProfile(profile)

                with (open(f"{os.path.dirname(__file__)}/datas/contacts.txt")) as file:

                    range_sender = 25 # 35

                    allLines = file.read().split("\n")

                    try:
                        allLines.remove('')
                    except ValueError:
                        continue

                    if allLines:
                        conta = allLines[0:range_sender]

                        with open(f"{os.path.dirname(__file__)}/datas/contacts.txt", "w") as fileUpdate:
                            fileUpdate.writelines([l + "\n" for l in allLines[range_sender:]])

                        for line in conta:
                            self.senderMsg(line)

                    else:
                        tiverNumero = False

            print("Esperando para ciclar novamente")
            sleep(300)
