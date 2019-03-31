import csv;

filename_reader = "./jyouyou_list_mod.txt";
# https://www.aozora.gr.jp/kanji_table/
# からダウンロードできる常用漢字のリストに関して，
# 全角空白をカンマ(,)に一括置換したテキストファイルを使用

filename1_writer = "./output1.csv";
filename2_writer = "./output2.csv";
# 1ファイルにまとめると25MBをオーバーし，commitのときに問題になったので，
# やむなく出力を2ファイルに分割

def main():

	with open(filename_reader, 'r') as f:
		reader = csv.reader(f);
		for row in reader:
			kanji = row;
	f.close()

	num = len(kanji);
	res = []
	for i in range(0, num):
		for j in range(0, num):
			res.append([kanji[i] + kanji[j]]);

	res1 = res[0:2000000];
	res2 = res[2000000:];

	with open(filename1_writer, 'w', encoding = 'utf-8', newline = '') as f:
		writer = csv.writer(f);
		writer.writerows(res1);
	f.close()

	with open(filename2_writer, 'w', encoding = 'utf-8', newline = '') as f:
		writer = csv.writer(f);
		writer.writerows(res2);
	f.close()

if __name__ == '__main__':
	
	main()
