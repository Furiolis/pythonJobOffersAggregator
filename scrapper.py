import requests
import re
import json
from joboffer import JobOffer


class Scrapper:
    @staticmethod
    def main_worker_update(configs):
        file = open("sites.json", "r")
        sites = json.load(file)
        file.close()

        for site in sites:
            site_name = site["name"]
            site_url = site["url"]
            scrapper_guide = site["scrapper"]

            # NOTICE testowy kod
            ###########################
            if configs.args.test:
                plik = open("test_site_source.txt", "r", encoding='utf-8')
                site_source = plik.read()
                match = re.findall(site["url_pattern"], site_source)
                print(match)
                offer = Scrapper("test", scrapper_guide, configs)
            ###########################
            else:
                site_source = requests.get(site_url).text
                match = re.findall(site["url_pattern"], site_source)
                for offer_url in match:
                    offer = Scrapper(site_name + site["url_part_fill"] + offer_url, scrapper_guide, configs)
                    # TODO kod do obslugi oferty

    def __init__(self, offer_url, scrapper_guide, configs):
        self.offer_url = offer_url
        self.scrapper_guide = scrapper_guide
        # TODO trzeba dodac kod sprawdzajacy czy dana oferta jest juz obecna w bazie aby nie tworzyc zbednego ruchu

        # NOTICE testowy kod
        ###########################
        if configs.args.test:
            plik = open("test_offer_source.txt",  "r", encoding='utf-8')
            site_source = plik.read()
        ###########################
        else:
            site_source = requests.get(self.offer_url).text

        offer = JobOffer(self.offer_url)
        for pattern in self.scrapper_guide:
            match = re.findall(pattern["pattern"], site_source)
            offer.update(pattern["meanings"], match)
            ##########################
            # NOTICE testowy kod
            if configs.args.test:
                print(match)
            ######################

        offer.display()
