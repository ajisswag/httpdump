import requests
from time import sleep

link = input("What website would you like to dump?: ")

url = requests.get(link)

print("Dumping website")
sleep(3)

save = open("dump.txt", "w")

save.write(url.text)
save.close()

print("Info has been put into dump.txt")



