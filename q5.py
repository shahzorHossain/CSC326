import re

def split_sentence(name):
	text = open(name).read()
	text = text.replace('\n', ' ')
	m = re.split(r"(?<=[^A-Z].[.?]) +(?=[A-Z])", text)
	for i in m:
        	print i

if __name__ == "__main__":
	split_sentence("smith.txt")
