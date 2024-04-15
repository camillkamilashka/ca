class Iron:
    def __init__(self, power):
        self.power = power
    
    def calculate_energy_consumption(self, hours):
        return self.power * hours
    
    def calculate_cost(self, hours, rate):
        energy_consumption = self.calculate_energy_consumption(hours)
        return energy_consumption * rate


class TV:
    def __init__(self, power):
        self.power = power
    
    def calculate_energy_consumption(self, hours):
        return self.power * hours
    
    def calculate_cost(self, hours, rate):
        energy_consumption = self.calculate_energy_consumption(hours)
        return energy_consumption * rate


class WashingMachine:
    def __init__(self, power):
        self.power = power
    
    def calculate_energy_consumption(self, hours):
        return self.power * hours
    
    def calculate_cost(self, hours, rate):
        energy_consumption = self.calculate_energy_consumption(hours)
        return energy_consumption * rate
    

    