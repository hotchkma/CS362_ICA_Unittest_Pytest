def WordCount(x):
	count = 1
	for i in range(int(len(x))):
			if(x[i]==" "):
					count=count+1
	return count

print(WordCount("hello there"))
print(WordCount("hi, my name is Matthew"))
print(WordCount("haha that's so funny bro!"))
print(WordCount("This is a long ass sentence and god damn there are some words in it!"))
