from scraperwiki import scrape
import scraperwiki
from YellowPagesBusinessExtractor import YellowPagesBusinessExtractor
from DataManager import DataManager

print "Scraper started!";

extractor = YellowPagesBusinessExtractor(scrape, DataManager(scraperwiki.sqlite.save))
businesses = extractor.extractAndSaveBusinesses('Tuscon, AZ', 'cupcakes')


