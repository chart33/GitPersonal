my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# we want to combine the two into a list that includes both
# the lists are already each sorted

def MergeSort(a,b):
	combined_len = len(a)+len(b)
	combined = [0]*combined_len
	
	a_i = 0
	b_i = 0
	c_i = 0

	while c_i < combined_len:
		exhausted_a = a_i >= len(a)
		exhausted_b = b_i >= len(b)
		
		# when do I set the current index of combined to a?
		if (not exhausted_a and (exhausted_b or a[a_i] < b[b_i])):
			combined[c_i] = a[a_i]
			a_i += 1
		else:
			combined[c_i] = b[b_i]
			b_i += 1

		# increment combined
		c_i += 1
			
	return combined


print "combining my list and alice's list..."

combined = MergeSort(my_list, alices_list)

print combined