import urllib
import lxml.html
from BusinessExtractorInterface import BusinessExtractorInterface
from Business import Business
from BusinessBranch import BusinessBranch
import time
from lxml import etree

class YellowPagesBusinessExtractor(BusinessExtractorInterface):
	
	
	__baseUrl = "http://www.yellowpages.com"
	
	def __init__(self, scraper, dataManager):
		self.__scraper = scraper
		self.__dataManager = dataManager

	def extractAndSaveBusinesses(self, location, searchTerms):
		parameters = urllib.urlencode({"geo_location_terms": location, "search_terms": searchTerms})
		print parameters
		moreResults = True
		
		page = 1
		businesses = {}
		while(moreResults):
			time.sleep(1)
			try:
				html = self.__scraper(YellowPagesBusinessExtractor.__baseUrl + "/search?" + parameters + "&page=" + str(page))
				root = lxml.html.fromstring(html)
				
				moreResults = False;
				organicResults = root.cssselect("div.organic")
				
				if(len(organicResults) > 0):
					moreResults = True
					for searchResult in organicResults[0].cssselect("div.result"):
						name = self.__extractItem(searchResult, 'name')
						print "Extracting business: ",
						print name,
						print "..."
						businessBranch = BusinessBranch()
						businessBranch.streetAddress = self.__extractItem(searchResult, 'streetAddress')
						businessBranch.addressLocality = self.__extractItem(searchResult, 'addressLocality')
						businessBranch.setAddressRegion = self.__extractItem(searchResult, 'addressRegion')
						businessBranch.setPostalCode = self.__extractItem(searchResult, 'postalCode')
						businessBranch.setPhones = self.__extractPhones(searchResult)
						
						branchId = searchResult.get("data-ypid")
						businessBranch.branchId = branchId
						
						url = self.__extractDetailsURL(searchResult)
							
						if(len(url) > 0):
							self.__extractDetails(businessBranch, url)
						
						if(name in businesses):
							businesses[name].addBranch(businessBranch)
						else:
							business = Business()
							business.name = name
							business.addBranch(businessBranch)
							businesses[name] = business
						
						self.__dataManager.saveBusiness(business)
			except:
				#TODO: log error
				print "Unexpected error"
			page += 1
		return businesses
	
	def __extractDetails(self, branch, detailsURL):
		print "Extracting details: ",
		print detailsURL,
		print "..."
		details = {}
		try:
			html = self.__scraper(YellowPagesBusinessExtractor.__baseUrl + detailsURL);
			root = lxml.html.fromstring(html)
				
			dl = root.cssselect("dl")
			if(len(dl) > 0):
				dl = dl[0]
				children = list(dl)
				i = 0
				while(i <  len(children)):
					child = children[i]
					#The dt element contains the property description (e.g., hours)
					if(child.tag == 'dt'):
						
						prop = child.text
						prop = prop.strip()
						prop = prop.strip(":")
						
						#The dd element contains the value (e.g., Mon-Sun 9am - 5pm)
						#We need to skip the other elements
						while(i < len(children) - 1):
							i += 1
							child = children[i]
							if(child.tag == 'dd'):
								value = ""
								if(child.text != None):
									value += child.text
								for valueChild in child.iterdescendants():
									value += etree.tostring(valueChild)
									if(len(value) > 0 and not(prop.lower().find('hours') != -1 and \
									value.lower().find('do you know the hours for this business?') != -1)):
										details[prop] = value
								break
					
					i += 1
		except:
			#TODO: log error
			print "Unexpected error"
		branch.details = details
	
	def __extractDetailsURL(self, searchResult):
		url = ""
		item = searchResult.cssselect("a.business-name")
		if(len(item) > 0):
			item = item[0]
			url = item.get("href")
		return url;
	
	def __extractItem(self, searchResult, itemprop):
		result = ""
		item = searchResult.cssselect("[itemprop='" + itemprop + "']")
		if(len(item) > 0):
			item = item[0]
			result = item.text
			result = result.strip()
			result = result.strip(",")
		return result
	
	def __extractPhones(self, searchResult):
		print "Extracting phones:...\n"
		phones =  []
		phoneElements = searchResult.cssselect("[itemprop='telephone']")
		for phoneElement in phoneElements: 
			phones.append(phoneElement.text)
		return phones