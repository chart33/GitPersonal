
def two_sums(nums, t):
	# use a single pass hash table
	track = {}
	for i in range (0, len(nums)):
		track[nums[i]] = i

		num = nums[i]
		needed = t - num

		if needed in track and needed != num:
			return [i, track[needed]]



print two_sums([1,2,3], 4)



