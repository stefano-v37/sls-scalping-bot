import os

import yaml

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class ApiAuthKeyManager:
    def __init__(self, accout_name: str) -> None:
        self.accout_name = account_name

    def get_keys(self) -> tuple([str, str]):
        with open(f"{dir_path}//api-keys.yml") as file:
            obj = yaml.safe_load(file)
        return obj[self.account_name]["key"], obj[self.account_name]["secret-key"]

    def get_key(self) -> str:
        return self.get_keys()[0]

    def get_secret_key(self) -> str:
        return self.get_keys()[1]
