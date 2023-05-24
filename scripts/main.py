import csv
import re
from pprint import pprint
import requests
from bs4 import BeautifulSoup







class ScrapeToCsv(object):
	def __init__(self,exclude_list,url_list):
		self.exclude_list=exclude_list
		self.url_list=url_list
		pass

	def main(self):
		csv_res_list_list=[]

		for url in self.url_list:
			if url.startswith('https://animanch.com'):
				sorted_res_list=self.animanch(url)
			elif url.startswith('https://bbs.animanch.com'):
				sorted_res_list=self.animanch_bbs(url)
			elif url.startswith('https://hayabusa.open2ch.net'):
				sorted_res_list=self.onj(url)
			elif '5ch.net' in url:
				sorted_res_list=self.fivech(url)
			else:
				csv_res_list_list.append(['サイトのURLが不正です'])
				break

			# 共通処理
			excluded_word_res_list=self.exclude_word(sorted_res_list)
			excluded_word_url_res_list=self.exclude_url(excluded_word_res_list)
			csv_res_list_list.append(excluded_word_url_res_list)

		return csv_res_list_list

	'''
	utils
	'''

	# スクレイピング結果のリストを受け取ってcsvで保存
	def write_csv(self,res_list):
		# f_readline_strip_listの必要なデータのみ別のcsvファイルに出力する
		# extrasaction='ignore'→リストで指定したkeyだけ書き込む
		# newline=''→改行しない
		sorted_csv='test.csv'
		with open(sorted_csv,'w',newline='',encoding='utf-8') as csv_file:
			writer=csv.writer(csv_file)
			writer.writerows(res_list)

	# スクレイピング結果のリストを受け取ってURLのみを削除
	def exclude_url(self,res_list):
		return [re.sub(r'https?://[^| |\t|\n|\r|\f|\"|\']*','',res) for res in res_list]

	# 除外ワードリストとスクレイピング結果のリストを受け取って除外ワードが含まれるレスを削除
	def exclude_word(self,res_list):
		excluded_res_list=[]
		for i in res_list:
			for j in self.exclude_list:
				if j in i: break
			else:
				excluded_res_list.append(i)
		# pprint(res_list,sort_dicts=False)
		# pprint(excluded_res_list,sort_dicts=False)
		return excluded_res_list

	# レス番号、返信レス番号、レス内容を含んだ辞書から返信順で並び替え
	def reply_sort(self,res_dict):
		csv_res_list=[]

		# 返信レス番号から再帰的に返信順で並び替える再帰関数
		def recursion_reply(reply_from_number_list):
			for reply_from_number in reply_from_number_list:
				csv_res_list.append(res_dict[reply_from_number]['resbody'])
				if []!=res_dict[reply_from_number]['reply_from_number']:
					recursion_reply(res_dict[reply_from_number]['reply_from_number'])

		# 返信レス番号から再帰的に返信順で整理する
		for resnumber,res in res_dict.items():
			# 返信レスは除外
			if '>>' not in res['resbody']:
				csv_res_list.append(res['resbody'])
				for j in res['reply_from_number']:
					csv_res_list.append(res_dict[j]['resbody'])
					recursion_reply(res_dict[j]['reply_from_number'])

		return csv_res_list

	# テスト用 レスにレス番号付与
	def reply_sort_test(self,res_dict):
		csv_res_list=[]

		# 返信レス番号から再帰的に返信順で並び替える再帰関数
		def recursion_reply(reply_from_number_list):
			for reply_from_number in reply_from_number_list:
				csv_res_list.append(reply_from_number+' '+res_dict[reply_from_number]['resbody'])
				if []!=res_dict[reply_from_number]['reply_from_number']:
					recursion_reply(res_dict[reply_from_number]['reply_from_number'])

		# 返信レス番号から再帰的に返信順で整理する
		for resnumber,res in res_dict.items():
			# 返信レスは除外
			if '>>' not in res['resbody']:
				csv_res_list.append(resnumber+' '+res['resbody'])
				for j in res['reply_from_number']:
					csv_res_list.append(j+' '+res_dict[j]['resbody'])
					recursion_reply(res_dict[j]['reply_from_number'])

		return csv_res_list

	# reply_to_numberからreply_from_numberを作成
	def get_reply_from_number(self,res_dict):
		for resnumber,resbody in res_dict.items():
			for reply_to_number in resbody['reply_to_number']:
				res_dict[reply_to_number]['reply_from_number'].append(resnumber)
		return res_dict

	'''
	サイト別スクレイピング処理メソッド
	'''

	# あにまんch
	def animanch(self,url):
		bs4obj=BeautifulSoup(requests.get(url).text,'html.parser')

		# レス一覧の取得
		# いきなりレスやコメントのbodyを指定しても取得できた
		# res_list=[[i.get_text(separator='\n',strip=True)] for i in bs4obj.select('div.t_b')]
		# print(res_list)
		# コメント一覧の取得
		# comment_list=[[i.get_text(separator='\n',strip=True)] for i in bs4obj.select('div.commentbody')]
		# print(comment_list)
		# レスとコメントを統合する
		# res_comment_list=res_list+comment_list

		# レスとコメント一覧の取得
		# ,で繋ぐと上からorで検索するのでレス→コメントの順で一度で取得できた
		csv_res_comment_list=[[i.get_text(separator='\n',strip=True)] for i in bs4obj.select('div.t_b,div.commentbody')]
		# print(res_comment_list)

		return csv_res_comment_list

	# あにまん掲示板
	def animanch_bbs(self,url):
		res_dict={}
		bs4obj=BeautifulSoup(requests.get(url).text,'html.parser')
		# レス一覧の取得
		# レス番号、レス内容、返信レス番号を辞書にまとめる
		for i in bs4obj.select('li.list-group-item'):
			resnumber=i.select_one('span.resnumber').text
			try:
				reply_tag=i.select_one('div.reply').extract()
				reply_from_number=[j.text.replace('>>','') for j in reply_tag.select('a.reslink')]
			except:
				reply_from_number=[]
			resbody=i.select_one('div.resbody').get_text(separator='\n',strip=True)
			res_dict[resnumber]={'resbody':resbody,'reply_from_number':reply_from_number}

		sorted_res_list=self.reply_sort(res_dict)
		# pprint(sorted_res_list,sort_dicts=False)

		return sorted_res_list

	# おんJ
	def onj(self,url):
		res_dict={}

		# ローカル環境
		# USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Iron Safari/537.36'
		# 空でも取得できた
		USER_AGENT=''
		headers={"User-Agent":USER_AGENT}
		bs4obj=BeautifulSoup(requests.get(url,headers=headers).text,'html.parser')
		# print(bs4obj)

		# レス一覧の取得
		# レス番号、レス内容、返信先レス番号、返信元レス番号、を辞書にまとめる
		for i in bs4obj.select('div.thread > dl'):
			# おんJでは最初のレス番号に名無し等が含まれるので属性値をスレ番号とした
			resnumber=i.select_one('a.num').get('val')
			resbody=i.select_one('.mesg.body').get_text(separator='\n',strip=True)
			# おんJではアンカー番号がタグで囲まれた形では取得できなかったので正規表現で取得
			reply_to_number=re.findall(r'>>(.*)',resbody)
			res_dict[resnumber]={
				'resbody':resbody,'reply_from_number':[],'reply_to_number':reply_to_number}
		# pprint(res_dict,sort_dicts=False)
		# print(res_dict)

		contain_from_res_dict=self.get_reply_from_number(res_dict)
		# pprint(contain_from_res_dict,sort_dicts=False)

		# res_list=self.reply_sort_test(contain_from_res_dict)
		sorted_res_list=self.reply_sort(contain_from_res_dict)
		# pprint(res_list,sort_dicts=False)

		return sorted_res_list

	# 5ch
	def fivech(self,url):
		res_dict={}
		bs4obj=BeautifulSoup(requests.get(url).text,'html.parser')

		# レス一覧の取得
		# レス番号、レス内容、返信先レス番号、返信元レス番号、を辞書にまとめる
		for i in bs4obj.select('div.post'):
			resnumber=i.select_one('span.number').text
			# 返信先レス番号 requestsでは返信元レス番号が表示されないので、返信先レス番号を利用
			reply_to_number=[j.text.replace('>>','') for j in i.select('a.reply_link')]
			# 返信元レス番号 後ほど使うので空にする
			reply_from_number=[]
			resbody=i.select_one('div.message').get_text(separator='\n',strip=True)
			res_dict[resnumber]={
				'resbody':resbody,'reply_from_number':reply_from_number,'reply_to_number':reply_to_number}

		contain_from_res_dict=self.get_reply_from_number(res_dict)
		# pprint(contain_from_res_dict,sort_dicts=False)

		# res_list=self.reply_sort_test(contain_from_res_dict)
		sorted_res_list=self.reply_sort(contain_from_res_dict)
		# pprint(res_list,sort_dicts=False)

		return sorted_res_list



if __name__=='__main__':
	exclude_list=[
		'自己主張',
		'嘘',
		'変わってない',
	]

	url_list=[
		# 'https://nova.5ch.net/test/read.cgi/livegalileo/1684319120/',
		# 'https://bbs.animanch.com/board/1908222/',
		'https://hayabusa.open2ch.net/test/read.cgi/livejupiter/1684224962/',
		# 'https://aaa',
	]

	stc=ScrapeToCsv(exclude_list,url_list)
	csv_res_list_list=stc.main()

	# pprint(csv_res_list_list,sort_dicts=False)
	print(csv_res_list_list)