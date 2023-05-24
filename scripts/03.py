import requests
from bs4 import BeautifulSoup


# おんJ
def test01(url):
	res_dict={}
	bs4obj=BeautifulSoup(requests.get(url).text,'html.parser')
	print(bs4obj)
	# レス一覧の取得
	# レス番号、レス内容、返信先レス番号、返信元レス番号、を辞書にまとめる
	for i in bs4obj.select('div.thread > dl'):
		resnumber=i.select_one('a.num').text
		reply_resnumber=[]
		resbody=i.select_one('mesg body').get_text(separator='\n',strip=True)
		res_dict[resnumber]={'resbody':resbody,'reply_resnumber':reply_resnumber}

	print(res_dict)

# return self.reply_sorting(res_dict)



if __name__=='__main__':
	url='https://mi.5ch.net/test/read.cgi/news4vip/1684230524/'
	# url='https://eagle.5ch.net/test/read.cgi/livejupiter/1684229791/'
	# url='https://nova.5ch.net/test/read.cgi/livegalileo/1683746280/'
	# url='https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1684224962/'
	# url='https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1684226544/'
	test01(url)
	# test02()
	# test03()