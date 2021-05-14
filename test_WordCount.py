import pytest
import WordCount

def WordCount_case(x):
		assert WordCount("Hello,") == 1
		assert WordCount("Can you hear me?") == 4
		assert WordCount("I'm in California") == 3
		assert WordCount("Dreaming of who we used to be") == 7
		assert WordCount("When we were younger") == 4
		assert WordCount("and free") == 2
