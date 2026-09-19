""" Abstraction"""

"""
from abc import ABC, abstractmethod,property

class BankApp(ABC):
    @property
    @abstractmethod
    def security(self):
        pass 

class MobileApp(BankApp):
    def mobileui(self):
        print('from mobileui')

    def security(self):
        print('Mobile app security')
obj=MobileApp()

obj.mobileui()
obj.security()

"""