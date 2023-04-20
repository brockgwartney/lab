class Account:
    def __init__(self,name : str):

        '''
        :param name: This is the name of the account
        
        '''    

        self.__account_name = name
        self.__account_balance = 0


        

    def deposit(self,amount: int) -> int:

        '''
        Used for a user to deposit their money
        :param amount: amount of money they wish to deposit, should be int over 0
        :return: returns True or False depending on if the deposit changed the account balance or not

        
        '''

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
        
    def withdraw(self,amount : int) -> int:

        '''
        Used for a user to withdraw their money
        :param amount: amount of money they wish to withdraw, should be int over 0
        :return: returns True or False depending on if the withdraw changed the account balance or not

        
        '''

        if amount <= 0 or self.__account_balance < amount:
            return False
        else:
            self.__account_balance -= amount
            return True
    def get_balance(self) -> int:
        
        '''
        :return: returns the balance amount

        '''

        return self.__account_balance
    

    def get_name(self) -> str:

        '''
        :return: returns the account name
        '''

        return self.__account_name
    
            
