def my_map(func,iterable):
	if func is None:
		return list(iterable)
	else:
		return [func(i) for i in iterable]

def my_reduce(func, iterable, start=None):
	iterator = iter(iterable)
	if start is None:
		try:
			start = iterator.next()

		except StopIteration:
			raise TypeError("my_reduce() of empty sequence with no initial value")			
	accum = start
	for i in iterable:
		accum = func(accum, i)
	return accum

def my_filter(func, iterable):

	if func is None:
		result = [i for i in iterable if i]
	else: 
		result = [i for i in iterable if func(i)]
	
	if type(iterable) == tuple:
		return tuple(result)
	elif type(iterable) == str:
		return ''.join(result)
		
	return result

