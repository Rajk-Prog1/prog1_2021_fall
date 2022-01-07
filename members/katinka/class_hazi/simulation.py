import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt

class Person:
    death_rate = 0.01
    incubation_days = 5
    recovery_days = 30
    
    def __init__(self, exposed: bool = False):
        self.dead = False
        if exposed:
            self.susceptible = False
            self.exposed = True
        else:
            self.susceptible = True
            self.exposed = False
        
        self.infectious = False
        self.recovered = False
        self.since_infected = 0
        
    def death(self):
        if np.random.random() < self.death_rate:
            self.dead = True
            self.infectious = False
            
    def infection(self, infection_rate):
        if np.random.random() < infection_rate:
            self.exposed = True
            self.susceptible = False
            
    def incubation(self):
        self.since_infected += 1
        if self.since_infected > self.incubation_days:
            self.infectious = True
            self.exposed = False
    
    def recovery(self):
        self.death()
        self.since_infected += 1
        if not self.dead and self.since_infected > self.recovery_days:
            self.recovered = True
            self.infectious = False
            
    def update(self, infection_rate):
        if self.dead:
            pass
        elif self.susceptible:
            self.infection(infection_rate)
        elif self.exposed:
            self.incubation()
        elif self.infectious:
            self.recovery()
                        
class Society:
    infection_rate = 0.5
    
    def __init__(self, start_population: int = 1000, exposed_rate: float = 0.01, person_class = Person):
        self.init_statistics()

        self.population = []
        for person in range(start_population):
            if np.random.random() < exposed_rate:
                self.population.append(person_class(exposed=True))
                self.exposed += 1
            else:
                self.population.append(person_class())
                self.susceptible += 1
        
    def get_infection_rate(self):
        return self.infectious / len(self.population) * self.infection_rate
        
    def init_statistics(self):
        self.dead = 0
        self.susceptible = 0
        self.exposed = 0
        self.infectious = 0
        self.recovered = 0
        
    def update(self):
        self.init_statistics()
        
        for person in self.population:
            person.update(self.get_infection_rate())
            
            if person.dead:
                self.dead += 1
            elif person.susceptible:
                self.susceptible += 1
            elif person.exposed:
                self.exposed += 1
            elif person.infectious:
                self.infectious += 1
            elif person.recovered:
                self.recovered += 1

class Simulator:
    def __init__(self, start_population: int=1000, exposed_rate:float=0.05):
        self.start_population = start_population
        self.exposed_rate = exposed_rate
        
    def init_stat(self) -> None:
        self.dead = []
        self.susceptible = []
        self.exposed = []
        self.infectious = []
        self.recovered = []
        
    def simulate(self, days: int = 100, plot: bool = True, person_class=Person):
        self.init_stat()
        self.days = range(days)
        self.society = Society(start_population=self.start_population, exposed_rate=self.exposed_rate, person_class=person_class)
        
        for year in tqdm(self.days):
            self.dead.append(self.society.dead)
            self.susceptible.append(self.society.susceptible)
            self.exposed.append(self.society.exposed)
            self.infectious.append(self.society.infectious)
            self.recovered.append(self.society.recovered)
            self.society.update()
            
        if plot:
            self.plot()

    def plot(self):
        fig, axes = plt.subplots(figsize = [16,8])
        axes.plot(self.days, self.dead, label = 'dead')
        axes.plot(self.days, self.susceptible, label = 'susceptible')
        axes.plot(self.days, self.exposed, label = 'exposed')
        axes.plot(self.days, self.infectious, label = 'infectious')
        axes.plot(self.days, self.recovered, label = 'recovered')
        axes.legend()
        fig.show(warn=False)