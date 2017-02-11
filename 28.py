from functools import reduce

def find_max(x,y):
	if x>y:
		return x
	else:
		return y

def find_longest_word(words):
	lengths = list(map(len,words))
	
	return (reduce(find_max,lengths))

def main():
	
	words = input("Enter the list of words: ").split()
	
	print(find_longest_word(words))
	
if __name__=="__main__":
	main()
