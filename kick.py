from selenium import webdriver
import json
import os

username = 'shakomako' #please unban stylertier and mamadee3

url = f"https://kick.com/api/v1/channels/{username}"

driver = webdriver.Firefox()

driver.get(url)

with open("response.html", "w", encoding='utf-8') as f:
    f.write(driver.page_source)

fp = open("response.html","r")
lines = fp.readlines()
fp.close()

line = lines[0].split(r"<body>")[1].split(r"</body>")[0]

jsonstr = json.loads(line)

#frontid = jsonstr["playback_url"].split(r".m3u8?token=")[0].split(r"/")[-1].split(".")[1]
#midid = jsonstr["playback_url"].split(r".m3u8?token=")[0].split(r"/")[-1].split(".")[-1]

for jsondata in jsonstr["previous_livestreams"]:
	#lastid = jsondata["thumbnail"]["src"].split(r'/')[-2]
	#urlname = r'https://stream.kick.com/ivs/v1/'+frontid+r'/'+midid+r'/'+jsondata["start_time"][0:4]+r'/'+str(int(jsondata["start_time"][5:7]))+r'/'+str(int(jsondata["start_time"][8:10]))+r'/'+str(int(jsondata["start_time"][11:13]))+r"/"+str(int(jsondata["start_time"][14:16]))
	#urlname+= r'/'+lastid +r'/media/hls/master.m3u8'
	#filename=jsondata["slug"]
	videourl = r'https://kick.com/video/'+jsondata['video']['uuid']
	cmd = r'./yt-dlp_macos '+videourl
	print(cmd)
	os.system(cmd)

driver.quit()
