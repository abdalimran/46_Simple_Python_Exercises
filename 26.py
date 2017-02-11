from functools import reduce

def max_in_list(x,y):
	if x>y:
		return x
	else:
		return y
	

def main():
	L = map(int,input("Enter the list of numbers: ").split())
	
	print("Maximum element: {}".format(reduce(max_in_list,L)))
	
if __name__=="__main__":
	main()
