
class BankAccount:
  def __init__(self, account_number, balance, owner, type):
     self.account_number =account_number
     self.balance= balance
     self.owner= owner
     self.type=type
  def __repr__(self) -> str:
      return(f"account_number:{self.account_number}, balance: {self.balance}, Account ownner is :{self.owner}, type:{self.type}")


class Bank:
  def __init__(self, name,accounts: list["BankAccount"]):
     self.name=name
     self.accounts= accounts

  def __repr__(self) -> str:
      return(f"account owner:{self.name},  Account types is :{self.accounts}")

  #Add the BankAccount object to the Bank object
  def add_account(self, account):
      self.accounts.append(account)
    

class Customer:
  def __init__(self, name,accounts: list["BankAccount"]):
     self.name=name
     self.accounts= accounts
  def __repr__(self) -> str:
      return(f"accounts:{self.accounts}, Account ownner is :{self.name}")

  def add_account(self, account):
      self.accounts.append(account)



class Transactions:
  def __init__(self, account: "BankAccount", amount: float, type: str ):
     self.account=account
     self.amount= amount
     self.type= type
  def __repr__(self) -> str:
      return(f"account:{self.account}, Existing balance: {self.amount}, type:{self.type}")


  def add_transaction(self, transaction):
      self.transactions.append(transaction)

  def get_transactions(self):
      return self.transactions



#create new bank object and print
bank = Bank("marim",["savings", "fixed"] )


# creat new customer object
customer = Customer("adronah", ["saving", "current"])


# Create a new BankAccount object and print Bankaccount
mybankaccount= BankAccount(23456795, 400000, "mariam", "savings")


#create a new transaction abject and print
transaction= Transactions(mybankaccount, 300000, "savings")


#Add the BankAccount object to the Bank object
bank.add_account(mybankaccount)

#Add the BankAccount object to the customer object
customer.add_account(mybankaccount)

print(bank)
print( customer)
print(mybankaccount)
print(transaction)