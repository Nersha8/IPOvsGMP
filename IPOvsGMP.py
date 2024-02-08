import numpy as np
import matplotlib.pyplot as plt

# Placeholder for IPO listing prices and Grey market premiums
ipo_prices = np.zeros(30)  # Assuming data for 30 days
actual_ipo_growth = np.zeros(30)  # Assuming data for 30 days
grey_market_premiums = np.ones(30)  # Assuming data for 30 days

# Days from the IPO launch
days_since_launch = np.arange(1, 31)  # 1 to 30 days

# Reshape arrays
ipo_prices = ipo_prices.reshape(-1, 1)
actual_ipo_growth = actual_ipo_growth.reshape(-1,1)
grey_market_premiums = grey_market_premiums.reshape(-1, 1)

print("IPO Prices array dimensions:", ipo_prices.ndim)
print("Grey Market Premiums array dimensions:", grey_market_premiums.ndim)

# Simulating random data for IPO prices and Grey market premiums
ipo_prices = np.random.randint(100, 500, size=(30, 1))
actual_ipo_growth = np.random.uniform(0, 50, size=(30, 1)) 
grey_market_premiums = np.random.uniform(0, 50, size=(30, 1))

# Broadcasting to calculate the total value for each day
total_value = ipo_prices + actual_ipo_growth
predicted_value = ipo_prices + grey_market_premiums

# Calculate percentage change in GMP
gmp_percentage_change = np.diff(grey_market_premiums, axis=0) / grey_market_premiums[:-1] * 100

# Reshape arrays
ipo_prices = ipo_prices.reshape(-1, 1)
actual_ipo_growth = actual_ipo_growth.reshape(-1,1)
grey_market_premiums = grey_market_premiums.reshape(-1, 1)

# Create an identity matrix for analysis
identity_matrix = np.eye(2)

# Matrix multiplication for analysis
transformed_data = np.dot(np.hstack((ipo_prices, grey_market_premiums)), identity_matrix)

# Display the data
print("IPO Prices:\n", ipo_prices)
print("actual ipo growth:\n", actual_ipo_growth)
print("Grey Market Premiums:\n", grey_market_premiums)
print("GMP Percentage Change:\n", gmp_percentage_change)
print("Transformed Data:\n", transformed_data)


# Calculate percentage change in total value
total_value_percentage_change = np.diff(total_value, axis=0) / total_value[:-1] * 100

# Plotting total value and its percentage change
plt.figure(figsize=(10, 5))

# Plotting actual IPO growth and predicted GMP
plt.plot(days_since_launch, actual_ipo_growth, label='Actual IPO Growth', color='blue')
plt.plot(days_since_launch, grey_market_premiums, label='Predicted GMP', color='orange')

plt.xlabel('Days Since IPO Launch')
plt.ylabel('Values')
plt.title('Actual IPO Growth vs Predicted GMP Over Time')
plt.legend()
plt.grid(True)
plt.show()