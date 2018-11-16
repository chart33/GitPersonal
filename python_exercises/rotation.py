# find the index at which a roation occurred, see if you can do it brute force, then in O(logn) time

def rotation_brute_force(arr):
	n = 0

	if arr == sorted(arr):
		# no rotation occurred
		return n

	for i in range(0, len(arr)):
		print "comparing "
		print i
		print i+1

		this = [arr[i], arr[i+1]]
		this_sort = sorted(this)

		if this_sort != this:
			print "this is the rotation!"
			# then we have found the rotation point
			return i+1


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# print rotation_brute_force(words)


def rotation(words):
	left_index = 0 # start at 0
	left_word = words[0]
	right_index = len(words)-1

	while (left_index+1) < right_index:
		# start in the middle of whatevers left, like binary sort
		i = left_index+((left_index+right_index)/2)
		if words[i] >= words[0] :
			# move the left index to where we guessed
			left_index = i
		else:
			 # move the right index to where we guessed
			 right_index = i

print rotation(words)




