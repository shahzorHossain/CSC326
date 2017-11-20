from time import clock

PROFILE_FUNCTIONS = True
PROFILE_RESULTS = {}


def profile(foo):
	def wrapper():
		if PROFILE_FUNCTIONS == True:
			start = clock()
			foo(*args, **kwargs)
			duration = clock() - start
			
			if (foo.__name__ in PROFILE_RESULTS):
				old_func_calls = PROFILE_RESULTS[foo.__name__][1]
				old_runtime = PROFILE_RESULTS[foo.__name__][0]
				old_average = old_func_calls * old_runtime
				new_average = (old_average + duration)/ (old_func_calls + 1)
				PROFILE_RESULTS[foo.__name__] = (new_average, old_func_calls + 1)
				
			else:
				PROFILE_RESULTS[foo.__name__] = (duration, 1)

		else:
			foo(*args, **kwargs)
	return wrapper

if __name__ == "__main__":

	@profile
	def my_func():
		sum = 0
		for i in range(25):
			sum += i


	my_func()
	print PROFILE_RESULTS

