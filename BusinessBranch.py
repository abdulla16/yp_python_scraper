class BusinessBranch:

	def __init__(self):
		self.__branchId = ""
		self.__details = {}
		self.__postalCode = ""
		self.__addressLocality = ""
		self.__addressRegion = ""
		self.__streetAddress = ""
		self.__phones = []

	@property
	def branchId(self):
		return self.__branchId
	
	@branchId.setter
	def branchId(self, branchId):
		self.__branchId = branchId
	
	@property
	def streetAddress(self):
		return self.__streetAddress
	
	@streetAddress.setter
	def streetAddress(self, streetAddress):
		self.__streetAddress = streetAddress
	
	@property
	def addressLocality(self):
		return self.__addressLocality
	
	@addressLocality.setter
	def addressLocality(self, addressLocality):
		self.__addressLocality = addressLocality
	
	@property
	def addressRegion(self):
		return self.__addressRegion
	
	@addressRegion.setter
	def addressRegion(self, addressRegion):
		self.__addressRegion = addressRegion
	
	@property
	def postalCode(self): 
		return self.__postalCode

	@postalCode.setter
	def postalCode(self, postalCode):
		self.__postalCode = postalCode
	
	@property
	def phones(self):
		return self.__phones
	
	@phones.setter
	def phones(self, phones):
		self.phones = phones
	
	@property
	def details(self):
		return self.__details
	
	@details.setter
	def details(self, details):
		self.__details = details
