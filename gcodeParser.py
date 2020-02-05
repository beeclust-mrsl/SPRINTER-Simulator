#! /usr/bin/env python

import re

def _clean_codestr(value):
	if value < 10:
		return "0%g" % value
	return "%g" % value

REGEX_FLOAT = re.compile(r'^\s*-?(\d+\.?\d*|\.\d+)')
REGEX_INT = re.compile(r'^\s*-?\d+')
REGEX_POSITIVEINT = re.compile(r'^\s*\d+')
REGEX_CODE = re.compile(r'^\s*\d+(\.\d)?')

CLEAN_NONE = lambda v: v
CLEAN_FLOAT = lambda v: "{0:g}".format(round(v, 3))
CLEAN_CODE = _clean_codestr
CLEAN_INT = lambda v: "%g" % v

class wordType():

	def __init__(self, cls, valueRegex, description, clean_value):
		self.cls = cls
		self.valueRegex = valueRegex
		self.description = description
		self.clean_value = clean_value

class parse():

	def __init__(self):

		self.codeDict = {

		    'G': wordType(
		        cls=float,
		        valueRegex=REGEX_CODE,
		        description="Address for preparatory commands",
		        clean_value=CLEAN_CODE,
		    ),
		
		    'M': wordType(
		        cls=float,
		        valueRegex=REGEX_CODE,
		        description="Miscellaneous function",
		        clean_value=REGEX_CODE,
		    ),
		
		    'X': wordType(
		        cls=float,
		        valueRegex=REGEX_FLOAT,
		        description="Absolute or incremental position of X axis",
		        clean_value=CLEAN_FLOAT,
		    ),
		
		    'Y': wordType(
		        cls=float,
		        valueRegex=REGEX_FLOAT,
		        description="Absolute or incremental position of Y axis",
		        clean_value=CLEAN_FLOAT,
		    ),
		
		    'P': wordType(
		        cls=float,
		        valueRegex=REGEX_FLOAT,
		        description="Serves as parameter address for various G and M codes",
		        clean_value=CLEAN_FLOAT,
		    ),
		
		    'S': wordType(
		        cls=float,
		        valueRegex=REGEX_POSITIVEINT,
		        description="Absolute or incremental position of A axis (rotational axis around X axis)",
		        clean_value=CLEAN_INT,
		    ),
		
		    'F': wordType(
		        cls=float,
		        valueRegex=REGEX_FLOAT,
		        description="Feedrate",
		        clean_value=CLEAN_FLOAT,
		    )
		
		}


	def readFile(self, path):
		self.file = open(path, "rt")

		#for x in self.file:
		line = self.file.readline()
		line = line.rstrip('\n')
		print(line[0])

	def parseLine(self, line):

		nextWord = re.compile(r'^.*?(?P<letter>[%s])' % ''.join(self.codeDict.keys()), re.IGNORECASE)
		index = 0

		while True:

			letterMatch = nextWord.search(line[index:])

			if letterMatch:
				# Letter
				letter = letterMatch.group('letter').upper()
				if index == 0:
					self.lastCommand = letter
				index += letterMatch.end()

				# Value
				valueRegex = self.codeDict[letter].valueRegex
				valueMatch = valueRegex.search(line[index:])

				value = valueMatch.group() # matched text
				index += valueMatch.end() # propogate index to end of value

				print(letter,value)

			else:
				break

	def process(self, letter, value):
		print('def')
		

	def test(self):
		self.parseLine('G1X10Y10')


	def main(self):
		self.openFile("sample.gcode")


if __name__ == '__main__':
	test = gcodeParser()
	test.test()
