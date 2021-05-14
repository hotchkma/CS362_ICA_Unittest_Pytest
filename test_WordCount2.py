import WordCount
import unittest

class testCaseCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(WordCount.WordCount("I am testing this function"),5)
		self.assertEqual(WordCount.WordCount("But this function assumes proper grammar"),6)
		self.assertEqual(WordCount.WordCount("So"),1)
		self.assertEqual(WordCount.WordCount("I must"),2)
		self.assertEqual(WordCount.WordCount("Maintain the proper"),3)
		self.assertEqual(WordCount.WordCount("Grammar or else the"),4)
		self.assertEqual(WordCount.WordCount("Program totally will not work for me"),7)


if __name__ == "__main__":
	unittest.main()
