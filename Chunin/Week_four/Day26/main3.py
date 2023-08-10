#Dictionary Comprehension Exercise 1 - Chech the number of words per word
sentence = "What is the Airspeed Velocity of an Umladen Swallow?"

result = {word:len(word) for word in sentence.split()2 -
print(result)

#Dictionary Comprehension Exercise 2 -Converting a dictionary of temperatures in celcius to temperature in fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
}