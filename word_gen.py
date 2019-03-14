import csv
import numpy as np


# Generate the list and file of all words
words = dict()
word_conv = list()

with open("data/Syllable_dictionary.txt") as f:
	for index, line in enumerate(f):
		contents = line.split(" ")
		contents[-1] = contents[-1][:-1]
		
		words[contents[0]] = index

		if(len(contents) > 2):
	   		ending = False
	   		for i in range(1, len(contents)):
	   			if(contents[i].startswith("E")):
	   				ending = True
	   				break
	   		if(ending):
	   			for j in range(1, len(contents)):
	   				if(i != j):
	   					word_conv.append([index, int(contents[j]), int(contents[i][-1]), 0])
	   		else:
   				word_conv.append([index, int(contents[1]), 0, int(contents[2])])
		else:
			word_conv.append([index, int(contents[1]), 0, 0])
word_conv = np.array(word_conv)

with open("output.csv",'w') as resultFile:
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows(words)









# Convert a single line to a valid 10 syllable line
def gen_line(line):
	contents = line.split(" ")
	converts = np.zeros([len(contents), 3])
	multi = false
	for i, c in enumerate(contents):
		contents[i] = (words.index(i))
		if(word.conv[:, 0].where(c).shape[0] == 1):
			converts[i] = word_conv[c]
		else:
			multi = true
	if(multi):
		syls = np.sum(converts[:, 1])
		mutlis = converts[:, 1].where(0)
		print(multis.shape[0]) 










poems = list()
poems_text = list()

with open("data/shakespeare.txt") as f:
	index = 0
	new = False
	for line in f:
		l = line.lstrip()[:-1].replace(',', '').replace('"', '').replace(':', '').replace(';', '').replace('.', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '').lower()
		if(len(list(filter(None, l.split(" "))))>0):
			if(new):
				l_mod = list()
				for i, w in enumerate(l.split(" ")):
					if w in words:
						l_mod.append(words[w])
					else:
						l_mod.append(words[w.replace("'", "")])
					conv = word_conv[np.where( word_conv[:, 0] == l_mod[-1] )][0]
					# sprint(conv)
					if(int(conv[2]) > 0 and i == len(l.split())-1):
						conv[1] = conv[2]
						for w,v in words.items():
							if(v==conv[0]):
								# print(w)
								break
					l_mod[-1] = conv
				poems[-1].append(l_mod)
				poems_text[-1].append(l)
			else:
				poems.append(list())
				poems_text.append(list())
				new = True
		else:
			# print('\n',end='')
			index += 1
			new = False
			ends = list()









for poem in poems:
	for line in poem:
		multi = list()
		syls = 0
		for i, word in enumerate(line):
			if(word[3] > 0):
				multi.append(i)
			syls += word[1]
		if(syls != 10 and len(multi) > 0):
			for i in multi:
				if(10-syls == line[i][3]-line[i][1]):
					syls-=line[i][1]
					syls+=line[i][3]
					line[i][1]=line[i][3]









def a():
	for j, poem in enumerate(poems):
		print(str(j)+'\n')
		for line in poem:
			for i, word in enumerate(line):
				if(i > 0):
					print('|', end='')
				for k, letter in enumerate(word):
					if(k>0):
						print(',', end='')
					print(letter, end='')
			print('\n', end='')
		print('\n')

# a()









def b():
	for j, poem in enumerate(poems):
		print(str(j)+'\n')
		for line in poem:
			agg = 0
			multi = list()
			for word in line:
				agg+=int(word[1])
				if(word[3] > 0):
					multi.append('('+str(word[1])+','+str(word[3])+')')
			print(agg, end='')
			if(len(multi) > 0 ):
				print(multi, end = '\n')
			else:
				print('', end = '\n')
		print('\n')

# b()



with open("poems.txt",'w') as resultFile:
	for p in poems:
		for l in p:
			for i, w in enumerate(l):
				if(i > 0):
					resultFile.write(';')
				resultFile.write(str(w[0])+','+str(w[1]))
			resultFile.write('\n')
		resultFile.write('\n')


# word_conv = np.array(word_conv)



# Generate poems as a new list of words with syllable descriptions
