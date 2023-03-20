import numpy as np
from scipy.optimize import minimize_scalar

class StockMarketSimulation:
    def __init__(self, num_investors, k, initial_stock_price, initial_dividend, bond_return):
        self.num_investors = num_investors
        self.k = k
        self.stock_history = np.zeros(k)
        self.stock_price = initial_stock_price
        self.dividend = initial_dividend
        self.bond_return = bond_return
        self.investors_wealth = np.ones(num_investors)
        self.investors_shares = np.zeros(num_investors)
        
    def update_stock_history(self, stock_return):
        self.stock_history[:-1] = self.stock_history[1:]
        self.stock_history[-1] = stock_return
        
    def calculate_stock_return(self):
        stock_return = (self.stock_price - self.stock_history[-1] + self.dividend) / self.stock_history[-1]
        return stock_return
        
    def calculate_utility(self, wealth, stock_history, investment_proportion):
        return np.mean([np.log((1 - investment_proportion) * wealth * (1 + self.bond_return) + 
                               investment_proportion * wealth * (1 + stock_history[i])) for i in range(self.k)])
        
    def calculate_demand(self, investor_wealth, investor_stock_history, price):
        investment_proportion = self.find_optimal_investment_proportion(investor_wealth, investor_stock_history, price)
        demand = (investment_proportion * investor_wealth) / price
        return demand
        
    def find_optimal_investment_proportion(self, investor_wealth, investor_stock_history, price):
        def expected_utility(investment_proportion):
            return -self.calculate_utility(investor_wealth, investor_stock_history, investment_proportion)
        res = minimize_scalar(expected_utility, bounds=(0, 1), method='bounded')
        return res.x
        
    def calculate_equilibrium_price(self):
        total_demand = sum([self.calculate_demand(self.investors_wealth[i], self.investors_shares[i], self.stock_price) 
                            for i in range(self.num_investors)])
        equilibrium_price = total_demand / 1  # assuming fixed number of shares
        return equilibrium_price
    
    def update_investors(self):
        for i in range(self.num_investors):
            demand = self.calculate_demand(self.investors_wealth[i], self.investors_shares[i], self.stock_price)
            cost = self.stock_price * demand
            self.investors_wealth[i] -= cost
            self.investors_shares[i] += demand
    
    def run_simulation(self, num_steps):
        for step in range(num_steps):
            stock_return = self.calculate_stock_return()
            self.update_stock_history(stock_return)
            self.update_investors()
            self.stock_price = self.calculate_equilibrium_price()


import matplotlib.pyplot as plt
import numpy as np

# Create the simulation object
num_investors = 100
k = 15
initial_stock_price = 4
initial_dividend = 0.20
bond_return = 0.04
simulation = StockMarketSimulation(num_investors, k, initial_stock_price, initial_dividend, bond_return)

# Set simulation parameters
num_years = 200
dividend_growth_rate = 0.05
time_period = 1  # year

# Initialize lists to store data
stock_prices = []
dividends = []
total_wealths = []

# Run simulation for specified number of years
for year in range(num_years):
    # Update dividend
    if year > 0:
        simulation.dividend *= (1 + dividend_growth_rate)

    # Run simulation for one time period
    for i in range(time_period):
        stock_return = simulation.calculate_stock_return()
        simulation.update_stock_history(stock_return)
        simulation.update_investors()
        simulation.stock_price = simulation.calculate_equilibrium_price()
        
    # Store data
    stock_prices.append(simulation.stock_price)
    dividends.append(simulation.dividend)
    total_wealths.append(sum(simulation.investors_wealth) + sum(simulation.investors_shares) * simulation.stock_price)


