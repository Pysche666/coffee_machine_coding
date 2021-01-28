from collections import OrderedDict
from coffee_machine.core.beverage import Beverage
from coffee_machine.apputils.exceptions import InvalidInputOptionException

"""
   Class for showing the beverage options and read/interpret them
"""
class BeverageOptionsImpl:
    
    def __init__(self, beverages):
        for beverage in beverages:
            assert (isinstance(beverage, Beverage))
        self._beverages = OrderedDict()
        self._construct_beverage_dict(beverages)
    
    """
        :param beverages: a list of Beverages
        construct a dict with key as index and value as Beverage
        :return:
    """
    def _construct_beverage_dict(self, beverages):
        
        for idx, beverage in enumerate(beverages):
            self._beverages[idx + 1] = beverage

    def get_beverage_dict(self):
        return self._beverages

    
    """
        print options
        :return:
    """
    def display_options(self):
        
        display_data=''
        for idx, beverage in self._beverages.items():
            display_data += str(idx) + '.' + beverage.name + '\n'
        display_data += "--------\n"
        display_data += '{0}.Refill\n'.format(idx+1)
        display_data += '{0}.Show_Inventory\n'.format(idx+2)
        print("Dispenser is ready to serve. Please enter an option number")
        print(display_data)

    def read_option(self):
        """
        :return: valid input option
        """
        print(">>>", end='')
        try:
            input_option = int(input())
            assert (0 <= input_option <= len(self._beverages) + 2)
        except:
            raise InvalidInputOptionException

        return input_option
