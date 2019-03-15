import os
import numpy as np
from IPython.display import HTML

from HMM import unsupervised_HMM
from HMM_helper import (
    text_to_wordcloud,
    states_to_wordclouds,
    parse_observations,
    sample_sentence,
    visualize_sparsities,
    animate_emission
)

poem_obs = []

# Take out the syllables from poems.txt!!!!!!!!!!!!!!
with open("poems.txt") as f:
	for line in f:
		l = line.split(";")
		row = []
		for pair in l:
			tup = pair.split(",")
			row.append(tup[0])
		poem_obs.append(row)

poems = []
# Make obs_map
with open("data/shakespeare.txt") as f:
	for line in f:
		check_int = line.strip()
		if len(check_int) > 3:
			l = line.lstrip()[:-1].replace(',', '').replace('"', '').replace(':', '').replace(';', '').replace('.', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '').lower()
			l_split = l.split(" ")
			row = []
			for word in l_split:
				row.append(word)
			poems.append(row)

# Populate obs_map
poem_obs_map = {}
for i in range(len(poems)):
	for j in range(len(poems[i])):
		if poems[i][j] not in poem_obs_map.keys():
			poem_obs_map[poems[i][j]] = poem_obs[i][j]





