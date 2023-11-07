import os
import sys
import subprocess
import time

def ver_os():
    platform = sys.platform
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "mac"
    elif platform == "win32":
        return "win"


if ver_os() == "win":
    import steamclient
    import winreg


class SteamCli:
    def __init__(self, game_name, username, password):
        self.username = username
        self.password = password
        self.game_name = game_name
        # TODO: read valid user_id for given username
        self.user_id = None
        self.client_proc = self.__start_client()
        time.sleep(30)
        self.game = self.__get_game()


    def __del__(self):
        if self.client_proc:
            self.__stop_client()

    @staticmethod
    def __path():
        # Find the Steam install directory or raise an error
        try:  # 32-bit
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Valve\\Steams")
        except FileNotFoundError:
            try:  # 64-bit
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Valve\\Steam")
            except FileNotFoundError as e:
                print("Failed to find Steam Install directory")
                raise e
        return winreg.QueryValueEx(key, "InstallPath")[0]

    def __get_user_id(self):
        if ver_os() != "win":
            return None
        users = steamclient.get_users()
        matches = (user for user in users if user.id == self.user_id)

        return next(matches) if self.user_id else users[0].id

    def __get_game(self):
        if ver_os() != "win":
            return None

        games = steamclient.get_games(self.__get_user_id())
        result = None
        for game in games:
            if game.name == self.game_name:
                result = game

        return result

    def __gen_url(self):
        return f'steam://rungameid/{self.game.id}]'

    @staticmethod
    def __client_oper(params):
        command = f"Steam.exe {params}"
        path = os.path.realpath(f"{SteamCli.__path()}\\{command}")
        process = subprocess.Popen(path)
        return process.pid

    def __start_client(self):
        login_params = f"-silent -login {self.username} {self.password}"
        return self.__client_oper(login_params)

    def __stop_client(self):
        shutdown_params = f"-shutdown"
        return self.__client_oper(shutdown_params)

    def run(self):
        if ver_os() != "win":
            return None

        run_game_params = f"-applaunch {self.game.id}"
        return self.__client_oper(run_game_params)
