import requests
import os
import webbrowser

os.system('clear')
slackdomain = input('Please put in your slack domain (i.e.: gpff) ')
tokenaddress = f"https://{slackdomain}.slack.com/customize/emoji"
tokeneneed = input('\nDo you need help getting your Slack Token (y/n)? ')
if tokeneneed == 'y':
	os.system('clear')
	print(f'Great. Copy this command to clipboard:\n\n\nwindow.prompt("your api token is: ", TS.boot_data.api_token)')
	ready = input('\n\n*Press enter to continue* -- you will need to open devtools on the page that opens and paste that command into the console')
	webbrowser.open_new_tab(tokenaddress)
else:
	pass
slackaddress = f'https://{slackdomain}.slack.com/api/emoji.add' #replace with the actual address for your slack instance
TOKEN = input('\nPlease paste your Slack Token: ')
directory = input('\nPlease put in the directory where your emoji are: ')
if directory[-1] == "/":
	pass
else:
	directory = directory+"/"

def dothing():
	files = os.listdir(directory)

	for file in files:
		imagestring = str(directory)+str(file)
		realimage = open(imagestring, "rb")
		cleanname = file.split('.')
		cleanname = cleanname[0]
		req = requests.post(url = slackaddress, data = {'token': TOKEN,'mode': 'data','name': cleanname}, files = {'image': realimage})
		responsetext = req.text
		print(f"Here's what we got back for {cleanname}: \n {responsetext}")

dothing()