# pythonJobOffersAggregator
import config
import scrapper
import joboffer


if __name__ == '__main__':
    configs = config.Config()
    scrapper.Scrapper.main_worker_update(configs)
