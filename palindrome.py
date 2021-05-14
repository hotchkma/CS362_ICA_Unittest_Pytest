def palindrome(x):
	l = x
	for i in range(int(len(l)/2)):
		if (l[i]!=l[len(l)-1-i]):
			return 0
	return 1
