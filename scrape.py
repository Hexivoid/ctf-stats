from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe")

def updateStats(player):
    print("Loading player " + player)
    driver.get("https://www.brawl.com/players/" + player) #OcharX yairster
    hasPlayed = driver.find_elements_by_class_name("mc-blue")
    if not hasPlayed: #Array is empty
        print("Player " + player + " hasn't played CTF")
    else:
        print("Player " + player + " has played CTF")
        kills = driver.find_element_by_xpath("//span[@class='badge badge-light stat-kills']").text
        deaths = driver.find_element_by_xpath("//span[@class='badge badge-light stat-deaths']").text
        kdr = driver.find_element_by_xpath("//li[@class='list-group-item'][3]/span").text
        print("Kills: " + kills)
        print("Deaths: " + deaths)
        print("KDR: " + kdr)
        print("")

def getTopPlayers():
    driver.get("https://www.brawl.com/stats/ctf/kills/7/")
    playerNames = driver.find_elements_by_xpath("//img[@class='head_16']")
    return playerNames
