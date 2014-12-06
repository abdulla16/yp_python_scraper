import json

class DataManager:
	
	def __init__(self, saveFunction):
		self.__saveFunction = saveFunction
	
	def saveBusiness(self, business):
		self.__saveFunction(unique_keys=['name'], data={'name': business.name}, table_name="data")
		for branch in business.branches:
			self.saveBranch(branch, business.name)

	def saveBranch(self, branch, businessName):
		columnValues = {}
		
		columnValues["branch_id"] = branch.branchId
		columnValues["business_name"] = businessName;
		columnValues["street_address"] = branch.streetAddress
		columnValues["address_locality"] = branch.addressLocality
		columnValues["address_region"] = branch.addressRegion
		columnValues["postal_code"] = branch.postalCode
		
		columnValues["additional_details"] = json.dumps(branch.details)
		self.__saveFunction(unique_keys=["branch_id"], data=columnValues, table_name="branch")
		for phone in branch.phones:
			self.savePhone(phone, branch.branchId)
	
	def savePhone(self, telephone, branchId):
		self.__saveFunction(unique_keys=["branch_id"], data={"branch_id": branchId, "telephone": telephone}, table_name="telephone")
