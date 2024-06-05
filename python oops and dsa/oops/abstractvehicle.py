from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def __init__(self,color,num_tyre,gears):
        self.color=color
        self.num_tyre=num_tyre
        self.gears=gears
        
        