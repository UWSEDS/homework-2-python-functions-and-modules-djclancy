import pandas as pd
import requests
import os
import string
import random

#creates a dataframe from a url
def urlToDf(url):
	r = requests.get(url)
	#creates a random file name which the user is unlikely to have
	fileName = randString_withCSV()
	open(fileName,'wb').write(r.content)
	df = pd.read_csv(fileName)
	os.remove(fileName)
	return df

#returns a string with random labels
def randString_withCSV(length=10):
	letts = string.ascii_letters + string.digits
	st = ''.join(random.choice(letts) for j in range(0,length))
	return st+".csv"

# does part 2
def test_create_dataframe(df, cols):
	c = df.columns
	c.sort()
	cols.sort()
# see if the sorted columns are the same
	if c != cols:
		return False
# find out if there are fewer than 10 indices
	elif len(df.index) < 10:
		return False
# find out if the columns are each of the same type
	else:
		sameColTypes = [str(df[y].dtype) != 'object' for y in c]
		return (sum(sameColTypes) == len(sameColTypes))

