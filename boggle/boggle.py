"""
File: boggle.py
Name:Claire
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dic_list = []
word_list=[]
boggle=[]
def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	read_dictionary()

	while True:
		row_1 = input('1 row of letters: ').lower()
		if check_input(row_1) :
			print('Illegal input')
			break
		row_2 = input('2 row of letters: ').lower()
		if check_input(row_2):
			print('Illegal input')
			break
		row_3 = input('3 row of letters: ').lower()
		if check_input(row_3):
			print('Illegal input')
			break
		row_4 = input('4 row of letters: ').lower()
		if check_input(row_4):
			print('Illegal input')
			break

		find_word(boggle,[])


	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')
def find_word(boggle,ans_list):
	count=[0]
	m, n = len(boggle), len(boggle[0])
	for i in range(m):
			for j in range(n):
					helper(i,j,ans_list,[],'',count)

	print(f'There are {count[0]} words in total.')

def helper(x,y,ans_list,used_index,current_s,count):
	if len(current_s)>=4 and current_s in dic_list and current_s not in ans_list:
		print('Found: ' + current_s)
		ans_list.append(current_s)
		count[0]+=1
		for i in range(-1,2):
			for j in range(-1,2):
				new_x, new_y = x + j, y + i
				if 0 <= new_x < len(boggle) and 0 <= new_y < len(boggle[0]) and (new_x,new_y) not in used_index:
					# Choose
					current_s += boggle[new_x][new_y]
					used_index.append((new_x, new_y))

					if has_prefix(current_s):
						helper(new_x, new_y, ans_list, used_index, current_s, count)
					current_s = current_s[:-1]
					used_index.pop()

	# Recursive case
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				new_x, new_y = x + j, y + i
				if 0 <= new_x < len(boggle) and 0 <= new_y < len(boggle[0]) and (new_x,new_y) not in used_index :
					# Choose
					current_s += boggle[new_x][new_y]
					used_index.append((new_x,new_y))
					# Explore
					if has_prefix(current_s):
						helper(new_x,new_y,ans_list, used_index, current_s,count)
					# Unchoose
					current_s = current_s[:-1]
					used_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE,'r') as f:
		for line in f:
			dic_list.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic_list:
		if word.startswith(sub_s):
			return True
	return False

def check_input(s):
	global word_list
	if len(s)!=7:
		return True
	for i in range(len(s)):

		if i %2==0:
			word_list.append(s[i])

			if not s[i].isalpha():
				return True
		elif i%2==1:
			if not s[i]==' ':
				return True
	boggle.append(word_list)
	word_list=[]







if __name__ == '__main__':
	main()
