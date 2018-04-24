import win32com.client
import pyperclip
import time
import re

from nltk.corpus import wordnet
	
new_data="";
clean_re=re.compile('[_\d\!@#\$%\^\&\*\(\)\-\+\=\[\]\{\}\|~`\'\":;,\?\.\<\>\\\\]')
speak = win32com.client.Dispatch('Sapi.SpVoice')

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
				speak.Speak(word)
				speak.Speak(defn)
			except Exception:
				print(clean_wrd,": no meaning found\n")
	new_data=pyperclip.paste()