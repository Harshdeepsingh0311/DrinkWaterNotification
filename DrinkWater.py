import time
from plyer import notification

if __name__ == '__main__':
	while True:
		notification.notify(
			title="Please Drink Water Now!!",
			message="It may improve memory and mood.\nIt can help reduce sugar cravings and aid weight maintenance.\n It may improve exercise performance.\nIt may reduce headaches and migraines.\n",
			app_icon = "C:\\Users\\Admin\\Downloads\\water.ico",
			timeout=10)

		time.sleep(60*60)