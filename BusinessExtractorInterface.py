
class BusinessExtractorInterface:
	
	"""Abstract method
	@param location: e.g., Tuscon, AZ
	@param searchTerms:  e.g., cupcakes"""
	def extractAndSaveBusinesses(self, location, searchTerms):
		raise NotImplementedError("Subclass must implement this") 