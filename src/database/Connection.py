# This is an abstract class. It is used to create the three connection objects used in the full workflow of
# EvoRecSys.
class Connection:

    # These values should be changed according to your network configurations.
    HOST = '127.0.0.1'  
    USER = 'developer'
    PASSWORD = 'marcelo3548'
    DATA_BASE = 'evorecsys'

    # Constructor
    def __init__(self):

        self.connector = None
