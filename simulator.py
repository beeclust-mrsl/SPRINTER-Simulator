#! /usr/bin/env python

import gcodeParser
import vizualizer
import time

class simulate():

	def __init__(self, timeStep):

		self.gcode = gcodeParser.parse('sample.gcode')
		self.plot  = vizualizer.vizualize(x_size = 100, y_size = 100)

		self.timeStep = timeStep


	def update(self, i):
 
			code  = self.gcode.parseLine()

			if code == lorem:
				x, y, feedrate = self.gcode.process(code)
				self.plot.appendPlot(x, y, feedrate)


	def main(self):
		self.plot.animate(self.update, lines, self.timeStep)
	
if __name__ == '__main__':
	simulator = simulate()
	simulator.main()