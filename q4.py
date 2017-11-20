class word_iterator(object):
	def __init__(self,file):
		self.iterator = open(file,"r")
		self.words = []
	def __iter__(self):
		return self
	def next(self):
		if len(self.words) > 0:
			return self.words.pop(0)
		else:
			self.words = self.iterator.next().split()
			return self.next()

def find_popular(name):
	word_count = {}
	word_itr = word_iterator(name)
	for word in word_itr:
		if word in word_count:
			word_count[word] += 1
		else: 
			word_count[word] = 1
	sorted_words = sorted(word_count.items(), reverse= True,key= lambda x:x[1])
	return [word[0] for word in sorted_words[:10]]

if __name__ == "__main__":

	print find_popular("test.txt")








