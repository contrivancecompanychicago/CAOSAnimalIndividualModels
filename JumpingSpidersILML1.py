import random
import requests

# Set the probability of the jumping spider biting an acquaintance to 0.12
probability_of_bite = 0.12

# Set the number of guests to 20
number_of_guests = 20

# Create a list to store the number of guests bitten by the jumping spider
number_of_bites = []

# Get the current temperature in Illinois
temperature = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Illinois&appid=YOUR_API_KEY").json()["main"]["temp"]

# For each guest, generate a random number between 0 and 1
for guest in range(number_of_guests):
    bite_probability = random.random()

    # If the random number is less than the probability of bite, add 1 to the number of bites
    if bite_probability < probability_of_bite:
        number_of_bites.append(1)

# Calculate the expected number of bites based on the temperature
expected_bites = probability_of_bite * number_of_guests * temperature / 273.15

# Print the number of guests bitten by the jumping spider and the expected number of bites
print("The number of guests bitten by the jumping spider is:", sum(number_of_bites))
print("The expected number of bites is:", expected_bites)
