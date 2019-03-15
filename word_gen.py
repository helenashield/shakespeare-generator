import csv
import numpy as np


# Generate the list and file of all words
words = dict()
word_conv = list()

# a word is: [ID, syllables, syllables when ending, alternate syllable count]

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









# convert every poem in the text file to its associated ID
poems = list()
poems_text = list()

with open("data/shakespeare.txt") as f:
	# The poem we are currently on
	index = 0

	# whether we are starting a new poem based on a line
	new = False
	for line in f:
		# Remove leading spaces, strip punctuation and convert to lowercase
		l = line.lstrip()[:-1].replace(',', '').replace('"', '').replace(':', '').replace(';', '').replace('.', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '').lower()
		
		# If our line is not blank (blanks mean we are in between poems)
		if(len(list(filter(None, l.split(" "))))>0):
			
			# Check if we already started a new poem
			if(new):
				l_mod = list()
				for i, w in enumerate(l.split(" ")):

					# Check if the word is in the list, if not, drop "'" and try again
					if w in words:
						l_mod.append(words[w])
					else:
						l_mod.append(words[w.replace("'", "")])

					# Pick the first instance of the word in the dictionary
					conv = word_conv[np.where( word_conv[:, 0] == l_mod[-1] )][0]
					
					# If we have an ending character and are on the last character, then replace with end value
					if(int(conv[2]) > 0 and i == len(l.split())-1):
						conv[1] = conv[2]
						for w,v in words.items():
							if(v==conv[0]):
								# print(w)
								break

					# Set the output to the modified dictionary entry
					l_mod[-1] = conv

				# Add the line to the current poem
				poems[-1].append(l_mod)
				poems_text[-1].append(l)

			# If we have not started, a new poem, start a new poem
			else:
				poems.append(list())
				poems_text.append(list())
				new = True

		# If we are on a blank, move to the next poem and indicate that we have not started a new one
		else:
			# print('\n',end='')
			index += 1
			new = False
			ends = list()








# Loop through the poems, correcting line lengths
for poem in poems:
	for line in poem:

		# Keeping track of all the instances with multiple syllable counts
		multi = list()

		# Syllable count of the current line
		syls = 0
		for i, word in enumerate(line):
			if(word[3] > 0):
				multi.append(i)
			syls += word[1]
		# If we do not have 10 syllables and have words with multiple syllables
		if(syls != 10 and len(multi) > 0):

			# then loop through all multiple syllable words
			for i in multi:

				# and if they fix the syllable count, switch the syllable count with the correct one
				if(10-syls == line[i][3]-line[i][1]):
					syls-=line[i][1]
					syls+=line[i][3]
					line[i][1]=line[i][3]








# Testing function, prints the output
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








# Testing function, prints the poems as syllables per line, and marks ones with multiple possible syllables
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



# Produce the output
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
