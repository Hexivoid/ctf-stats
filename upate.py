from scrape import updateStats
from scrape import getTopPlayers
import os
import psycopg2

DATABASE_URL = os.environ['postgres://lqxkejvjriobip:3ade897410db3623da33081005503dd5a40b4331b2a401fd22bba73b4c2c09b1@ec2-52-21-153-207.compute-1.amazonaws.com:5432/d9bkkqcoi428up']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

trackedPlayers = ["Hexivoid", "Fit", "OcharX"]

#trackedPlayersElements = getTopPlayers()

#for player in trackedPlayersElements:
#    trackedPlayers.append(player.get_attribute("title"))

#print(trackedPlayers)

#for players in trackedPlayers:
#    updateStats(players)
