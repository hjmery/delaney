import requests
import time

f = open('flags.txt','r')
countries = f.readlines()
for i in range(len(countries)):
	countries[i] = countries[i].strip()

img_url="https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"
urls = []
filenames = []
requestlist = []

for i in range(len(countries)):
	urls.append(img_url + countries[i] + '-lgflag.gif')
	filenames.append(countries[i]+'lgflag.gif')

for i in range(len(countries)):
	requestlist.append(requests.get(urls[i]))

r=requests.get("https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/us-lgflag.gif")

#need to create list or dic to store values of flag and have it iterate over that list in order to download all gifs

for i in range(len(countries)):
	with open( filenames[i],"wb") as f:
		f.write(requestlist[i].content)

# for i in range(len(file)):
print("Total time elapsed: ",time.perf_counter ())