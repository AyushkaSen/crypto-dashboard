import requests
import matplotlib.pyplot as plt

# Fetch last 30 days of Bitcoin price data
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params = {
    "vs_currency": "usd",
    "days": "30"
}

response = requests.get(url, params=params)
data = response.json()

# Extract prices
prices = data["prices"]

dates = [item[0] for item in prices]
values = [item[1] for item in prices]

# Plot the chart
plt.figure(figsize=(12, 6))
plt.plot(values, color="orange")
plt.title("Bitcoin Price - Last 30 Days")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()