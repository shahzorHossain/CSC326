def find_product(l):
	sequences = map(lambda x: (x, x + 5), list(range(len(s) - 4)))
	#print sequences
	slices = map(lambda x: s[x[0]:x[1]], sequences)
	products = map(lambda l: reduce(lambda x,y: x * y, l), slices)
	index = reduce(lambda x, y: x if x[1] > y[1] else y, enumerate(products))
	return index

	
if __name__ == "__main__":
    s = [1,2,3,4,5,6,4,2,1,3]	
    print find_product(s)
	
	


