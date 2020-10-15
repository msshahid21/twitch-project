'''
Codecademy-Twitch Cumulative Project (Data Science Career Path):

Purpose of this part is to visualize the data obtained from the SQL queries within the previous part of the project.
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Bar Graph: Featured Games (games-to-viewers.png)
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

ax = plt.subplot(1, 1, 1)
plt.bar(range(len(games)), viewers, color = 'teal')
plt.title('Game to Number of Viewers')
plt.ylabel('Number of Viewers')
plt.xlabel('Game Title')
plt.legend(["Twitch"])
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation='45')
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts (leagueoflegends-viewers.png)
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, colors = colors, explode = explode, shadow = True, startangle = 345, autopct = '%1.0f%%', pctdistance = 1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc = "right")
plt.show()
plt.clf()

# Line Graph: Time Series Analysis (viewers-by-hour.png)
hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

upper_err = [x * 1.15 for x in viewers_hour]
lower_err = [x * 0.85 for x in viewers_hour]

ax = plt.subplot(1, 1, 1)
plt.plot(hour, viewers_hour)
plt.legend(["2015-01-01"])
plt.title("Viewers Per Hour")
plt.ylabel("Number of Viewers")
plt.xlabel("Hour of the Day")
plt.fill_between(hour, upper_err, lower_err, alpha = 0.2)
ax.set_xticks(hour)
plt.show()
plt.clf()
