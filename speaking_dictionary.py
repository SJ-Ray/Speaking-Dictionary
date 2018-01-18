import pyperclip
import time
import re
import os

from nltk.corpus import wordnet

new_data="";
clean_re=re.compile('[_\d\!@#\$%\^\&\*\(\)\-\+\=\[\]\{\}\|~`\'\":;,\?\.\<\>\\\\]')

while True:
	time.sleep(2)
	prev_data=pyperclip.paste()
	if prev_data!=new_data:
		words=prev_data.strip().split(" ")
		word=words[0].lower()
		if word:
			clean_wrd=re.sub(clean_re, '', word)
			try:
				syns=wordnet.synsets(clean_wrd)
				defn=syns[0].definition();
				print(clean_wrd,':',defn+"\n")
				os.system('espeak -v f2 "'+clean_wrd+'"')
				os.system('espeak -v f2 "'+defn+'"')
			except Exception:
				print(clean_wrd,": no meaning found\n")
	new_data=pyperclip.paste()