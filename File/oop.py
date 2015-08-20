
class Person(object):
    """Person class.

    >>> steven = Person('Steven')
    >>> steven.repeat()       # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say('Hello')
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask('preserve abstraction barriers')
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        self.previous = "I squirreled it away before it could catch on fine"

    def say(self, stuff):
        self.previous = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.say(self.stuff)

        "*** YOUR CODE HERE ***"

class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account("Eric")
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance."""
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions.append(('deposit', amount))
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    def deposit_check(Check):
        if Check.deposited == True
            return "The police have been notified"
        elif Check.payable_to == self.holder:
            Check.deposited = True
            self.deposit(Check.amount)
        else:
            return "The police have been notified"
            


# Don't forget to modify CheckingAccount above!

class Check(object):
    def __init__(self, payable_to, amount):
    self.payable_to = payable_to
    self.amount = amount
    self.deposited = False
    "*** YOUR CODE HERE ***"

    f = add_skittle
    instance = bag1

    
