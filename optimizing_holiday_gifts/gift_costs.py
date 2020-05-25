import time
import numpy as np

with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
    
gift_costs = np.array(gift_costs).astype(int)  # convert string to int

start = time.time()

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

# 32765421.24
# Duration: 5.311075210571289 seconds

# Refactored Code

start = time.time()

total_price = sum(gift_costs[gift_costs < 25]) * 1.08 # TODO: compute the total price after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))