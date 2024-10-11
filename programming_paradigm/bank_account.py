class BankAccount:
    def __init__(self, initial_balance = 0):
        """Initialize BankAccount with 0. initial balance"""
        self._account_balance = initial_balance

    def deposit(self,amount):
        """Add the specified amount to account balance"""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposted amount must be a postive number/integer")
    
    def withdraw(self,amount):
        """Withdraws only if specific amount is present in the account"""
        if amount > self._account_balance:
            return False
        
        elif amount > 0:
            self._account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive number.")
            return False
        
    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self._account_balance:.2f}")