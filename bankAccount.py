

class Account():
	def __init__(self):

		self.balance = 10000
		self.password = 5060
		self.number = 1335

	def withdraw(self):
		# numberPrompt(self)
		pass
	

	def deposit(self):
		pass
		# numberPrompt()

	def checkbalance(self):
		# numberPrompt()
		pass

	def numberPrompt(self, ac):
		if ac == self.number:
			return True
		return False



myAccount = Account()
anAccount = input("\nWhat is your account number?")
if myAccount.numberPrompt(anAccount):
	print("\nOk. I see your account.")
myAccount.withdraw()
