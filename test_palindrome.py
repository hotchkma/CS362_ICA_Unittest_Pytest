import pytest
import palindrome

def palindrome_case(x):
		assert palindrome("racecar") == 1
		assert palindrome("") == 1
		assert palindrome("hello") == 0
		assert palindrome("mom") == 1
		assert palindrome("a") == 1
		assert palindrome("h a h a") == 0
