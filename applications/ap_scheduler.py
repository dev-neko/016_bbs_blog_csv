import requests
from apscheduler.schedulers.background import BackgroundScheduler
# import os


def periodic_execution():
	response=requests.get('https://exeltowebpage.devnekoreplit.repl.co/')
	print(response.status_code)

# スケジュールの設定
def start():
	scheduler=BackgroundScheduler()
	scheduler.add_job(
		periodic_execution,
		'interval',
		minutes=1
	)
	scheduler.start()
