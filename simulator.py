#! /usr/bin/env python

import gcodeParser
import vizualizer

class simulate():

	def __init__(self, timeStep):

		self.gcode = gcodeParser.parse()
		self.gcode.openFile('sample.gcode')
		self.plot  = vizualizer.vizualize(xSize = 200, ySize = 200, xInit = 0, yInit =0)

		self.timeStep = timeStep
		self.steps = self.gcode.getLines()
		self.gcode.openFile('sample.gcode')
		print(self.steps)


	def update(self, i):
 
			line  = self.gcode.parseLine()

			if self.gcode.process(line):
				x, y, feed = self.gcode.process(line)
				self.plot.appendPlot(x, y, feed)

			else:
				self.gcode.process(line)				


	def main(self):
		self.plot.animate(callback = self.update, steps = self.steps, freq = self.timeStep)
	
if __name__ == '__main__':
	simulator = simulate(1)
	simulator.main()