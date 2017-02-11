def main():
	
	words = input("Enter the list of words: ").split()

	#~ 1. using a for-loop
	result1 = []
	for word in words:
		result1.append(len(word))
	print(result1)

	#~ 2. using the higher order function map()
	result2 = list(map(len,words))
	print(result2)
	
	#~ 3. using list comprehensions.
	result3 = [len(word) for word in words]
	print(result3)
	
if __name__=="__main__":
	main()
