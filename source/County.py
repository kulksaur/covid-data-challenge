import datetime

# A county class used for storing data in DB for counties
# The class variables are dynamically created
class County:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
                setattr(self, k, v)


