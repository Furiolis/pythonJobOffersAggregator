import json
import argparse
from datetime import datetime, timedelta

# TODO stworzyc jakies narzedzie do tworzenia logow z pracy aplikacji


class Config:
    config_file = "config.json"

    def __init__(self):
        current_time = datetime.now()
        parser = argparse.ArgumentParser(description="Program do agregacji ofert pracy")
        # parser.add_argument("-h", "--help")
        parser.add_argument("-u", "--update", help="Tryb pracy aktualizacji", action="store_true")
        parser.add_argument("-e", "--edit", help="Tryb edytowania plikow konfiguracyjnych", action="store_true")
        parser.add_argument("-t", "--test", help="Tryb testowania funkcji", action="store_true")
        parser.add_argument("-d", "--debud", help="Tryb debugowania, wyswietla wynik dzialania wybranych instrukcji", action="store_true")
        self.args = parser.parse_args()

        file = open(Config.config_file, "r")
        self.configs_list = json.load(file)
        file.close()

        if self.args.update:
            # TODO dodać logi o braku updatu i z jakiego powodu
            # update_restricion: "none", "no_update", "daily", "24h"
            interval_restriction = self.configs_list["update_interval_restriction"]
            last_update = datetime.strptime(self.configs_list["last_update"], "%Y-%m-%d %H:%M:%S.%f")
            if interval_restriction == "none":
                self.update_allowed = True
                self.configs_list["last_update"] = str(current_time)
            elif interval_restriction == "no_update":
                self.update_allowed = False
            elif interval_restriction == "daily" and last_update.date() == current_time.date():
                self.update_allowed = False
            elif interval_restriction == "24h" and current_time - last_update < timedelta(hours=24):
                self.update_allowed = False
            else:
                self.update_allowed = True
                self.configs_list["last_update"] = str(current_time)

    def __del__(self):
        file = open(Config.config_file, "w")
        json.dump(self.configs_list, file, indent=2)
        file.close()
