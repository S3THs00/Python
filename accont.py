class Account:
    """
    Represents a bank account.

    Attributes:
    name (str): The account holder's name.
    balance (float): The current account balance.
      """
    def __init__(self, name):
        """
        Initialize a new Account object.

        Args: name (str): The account holder's name.
              """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args: amount (float): The amount to deposit.

        Returns: bool: True if the deposit was successful, False otherwise.
              """
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        Args: amount (float): The amount to withdraw.
        Returns: bool: True if the withdrawal was successful, False otherwise.
            """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        """
        Get the current account balance.

        Returns: float: The account balance.
               """
        return self.__account_balance

    def get_name(self):
        """
        Get the account holder's name.

        Returns: str: The account holder's name.
              """
        return self.__account_name

