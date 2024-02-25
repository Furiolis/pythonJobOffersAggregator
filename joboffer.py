import re


class JobOffer:
    def __init__(self, url):
        self.url = url
        self.company = None
        self.city = None
        self.time = None
        self.experience = None
        self.contract = None
        self.place = None
        self.position = None
        self.technology = None
        self.salary_ranges = (0, 0)

    def update(self, types, data):
        for data, type_of_data in zip(data, types):
            if type_of_data == "company":
                self.company = data
            elif type_of_data == "city":
                self.city = data
            elif type_of_data == "time":
                self.time = data
            elif type_of_data == "experience":
                self.experience = data
            elif type_of_data == "contract":
                self.contract = data
            elif type_of_data == "where":
                self.place = data
            elif type_of_data == "job":
                self.position = data
            elif type_of_data == "skills":
                self.technology = re.findall('{"name":"(.*?)","level":(.*?)}', data)
            elif type_of_data == "gross":
                self.salary_ranges = data

    def display(self):
        print("URL:", self.url)
        print("Firma:", self.company)
        print("Miasto:", self.city)
        print("Wymiar:", self.time)
        print("Doswiadczenie:", self.experience)
        print("Umowa:", self.contract)
        print("Miejsce:", self.place)
        print("Posada:", self.position)
        print("Technologie", self.technology)
        print("Pensja:", self.salary_ranges)

