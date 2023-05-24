from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# URLでサイト判別
def t01():
	url_list=[
		'https://animanch.com/archives/20875298.html',
		'https://bbs.animanch.com/board/1908222/',
		'https://nova.5ch.net/test/read.cgi/livegalileo/1683746280/',
		'https://egg.5ch.net/test/read.cgi/sugiuraayano/1684388704/',
		'https://sora.5ch.net/test/read.cgi/livetx/1684386830/',
		'https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1684224962/',
		'https://aaa',
		]

	# compare_dict={
	# 	'':'',
	# 	'':'',
	# 	'':'',
	# 	'5ch':'5ch.net',
	# }

	for i in url_list:
		if i.startswith('https://animanch.com'):
			site_type='animanch'
		elif i.startswith('https://bbs.animanch.com'):
			site_type='animanch_bbs'
		elif i.startswith('https://hayabusa.open2ch.net'):
			site_type='onj'
		elif '5ch.net' in i:
			site_type='fivech'
		else:
			site_type=None
		print(i,site_type)

# urlだけ削除
def t02():
	import re

	# res_str='そろそろトレパク絵師を折り返すのんｺﾞﾛﾝﾔﾒﾛｵｵｵｵ<a href="https://twitter.com/hajime_tetsu" target="_blank">@hajime_tetsu</a> 空気さん… — S極 (Skyoku_69) 2023年05月09日'
	res_str_list=[
		'そろそろ\n<a href="https://twitter.com/hajime_tetsu" target="_blank">@hajime_tetsu</a> 空気さん\n— S極 (Skyoku_69)\n2023年05月09日',
		'aaahttps://twitter.com/hajime_tetsu uuiii',
		'aaa https://twitter.com/hajime_tetsu uuiii',
		'aaa http://twitter.com/hajime_tetsu\nuuiii\nhttps://twitter.com/hajime_tetsu ',
		'aaa\nhttps://twitter.com/hajime_tetsu\nuuiii',
	]

	for i in res_str_list:
		print(repr(i))

		result=re.findall(r'https?://[^| |\t|\n|\r|\f|\"|\']*',i)
		print(repr(result))

		print(repr(re.sub(r'https?://[^| |\t|\n|\r|\f|\"|\']*','',i)))

# リストをcsvに変換
def t03():
	from io import BytesIO
	import csv
	import zipfile
	import numpy as np

	csv_res_list_list=[
		'与党→在日の味方\n野党→在日の味方\nマスコミ→在日の味方\n反社団体→在日の味方\n法曹業界→在日の味方\n教育界→在日の味方\n芸能界→在日の味方\nスポーツ界→在日の味方\nすげえやん',
		'韓国人は優等人種だと主張する在日韓国人にレスバで負けたから',
		'>>1\nまずは君の考えが知りたい',
		'>>2\nこれ',
		'>>2\n>>3\n韓国人劣等人種\nなぜなら日本に併合されたかた',
		'>>2\n>>3\n韓国人劣等人種\nなぜなら日本に併合されたかた',
		'反日だから',
		'興味ない\n降りかかる火の粉だけ払えばいい',
		'>>6\n浅はか\n元を断てば火の粉は消える',
		'>>8\nコスパ悪すぎ\n北に統一されたあとならあり',
	]

	l=[0,1,2,3,4,5]

	np_csv_res_list_list=np.array(csv_res_list_list).reshape(-1,1).tolist()
	# print(np.array(csv_res_list_list).reshape(-1,1).tolist())

	sorted_csv='test.csv'
	with open(sorted_csv,'w',newline='',encoding='utf-8') as csv_file:
		writer=csv.writer(csv_file)
		writer.writerows(np_csv_res_list_list)

class Custom_Selenium():
	def __init__(self):
		# chromedriver.exeのインストール先
		self.CDM_INST=ChromeDriverManager().install()

	def qsai_driver(self):
		chrome_options=webdriver.ChromeOptions()
		# アダプタエラー、自動テスト…、を非表示
		chrome_options.add_experimental_option('detach',True)
		chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])
		# chrome_options.add_argument('--headless')  #ヘッドレスモード
		chrome_options.add_argument('--incognito')  #シークレットモード
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--disable-desktop-notifications')
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--disable-application-cache')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--ignore-certificate-errors')
		# chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
		# chrome_options.page_load_strategy='none'
		# 2021年12月30日追加
		# chrome_options.add_argument('--allow-running-insecure-content')
		# chrome_options.add_argument('--disable-web-security')
		# chrome_options.add_argument('--lang=ja')
		# chrome_options.add_argument('--blink-settings=imagesEnabled=false') #画像非表示

		# ブラウザの種類を特定するための文字列
		# 笹澤さんのアプリ
		# USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
		# 前に使っていた
		# USER_AGENT="Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
		# 新しくironで取得した
		# USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Iron Safari/537.36"
		# 新しくchromeで取得した
		# USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
		# USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
		# USER_AGENT='Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'
		# chrome_options.add_argument(f'--user-agent={USER_AGENT}')
		# proxy
		# proxy_server='141.147.184.254'
		# proxy_port='3128'
		# chrome_options.add_argument(f"--proxy-server=http://{proxy_server}:{proxy_port}")

		driver=webdriver.Chrome(self.CDM_INST,options=chrome_options)

		# ページの読み込みで待機する秒数、これ以上経過すると例外発生
		driver.set_page_load_timeout(30)
		#要素が見つかるまで指定した時間まで待機
		driver.implicitly_wait(30)

		return driver

	def sute_driver(self):
		chrome_options=webdriver.ChromeOptions()

		# try:
		# 	# 起動しているdriverを再利用する
		# 	chrome_options.add_argument('--remote-debugging-port=9222')
		# 	# Seleniumでの処理後、Chromeを起動したままにする
		# 	chrome_options.add_experimental_option('detach',True)
		# 	# アダプタエラー、自動テスト…、を非表示
		# 	chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])
		# except:
		# 	chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')

		# chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')

		# Seleniumでの処理後、Chromeを起動したままにする
		chrome_options.add_experimental_option('detach',True)
		# アダプタエラー、自動テスト…、を非表示
		chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])

		# chrome_options.add_argument('--remote-debugging-port=9222')

		# その他
		# chrome_options.add_argument('--headless')  #ヘッドレスモード
		chrome_options.add_argument('--incognito')  #シークレットモード
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--disable-desktop-notifications')
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--disable-application-cache')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--ignore-certificate-errors')
		# chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
		# chrome_options.page_load_strategy='none'
		# 2021年12月30日追加
		# chrome_options.add_argument('--allow-running-insecure-content')
		# chrome_options.add_argument('--disable-web-security')
		# chrome_options.add_argument('--lang=ja')
		# chrome_options.add_argument('--blink-settings=imagesEnabled=false') #画像非表示

		# 新しくchromeで取得した
		USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
		chrome_options.add_argument(f'--user-agent={USER_AGENT}')

		# proxy
		proxy_server='150.230.198.240'
		proxy_port='3128'
		chrome_options.add_argument(f"--proxy-server=http://{proxy_server}:{proxy_port}")

		driver=webdriver.Chrome(self.CDM_INST,options=chrome_options)
		# ページの読み込みで待機する秒数、これ以上経過すると例外発生
		driver.set_page_load_timeout(30)
		#要素が見つかるまで指定した時間まで待機
		driver.implicitly_wait(5)

		# ウィンドウサイズを予め右半分にする
		driver.set_window_size(654,664)
		driver.set_window_position(633,0)

		return driver

def t04():
	cs=Custom_Selenium()
	driver=cs.sute_driver()

	url='https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1684224962/'
	driver.get(url)

	bs4obj=BeautifulSoup(driver.page_source,'html.parser')
	print(bs4obj)

	driver.quit()

if __name__=='__main__':
	# t01()
	# t02()
	# t03()
	t04()