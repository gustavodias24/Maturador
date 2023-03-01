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
