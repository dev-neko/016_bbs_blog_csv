
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








if __name__=='__main__':
	# t01()
	# t02()
	t03()