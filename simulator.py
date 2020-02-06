#! /usr/bin/env python

import gcodeParser
import vizualizer

class simulate():

	def __init__(self, timeStep):

		self.gcode = gcodeParser.parse()
		self.gcode.openFile('test3.gcode')
		self.plot  = vizualizer.vizualize(xSize = 200, ySize = 200, xInit = 0, yInit =0)
		self.x = None
		self.y = None
		self.timeStep = timeStep
		self.steps = self.gcode.getLines()
		self.gcode.openFile('test3.gcode')
		print(self.steps)


	def update(self, i):
 
			line  = self.gcode.parseLine()

			if self.gcode.process(line):
				self.x, self.y, feed = self.gcode.process(line)
				self.plot.appendPlot(self.x, self.y, feed)

			else:
				if 'M' in line.keys():
					self.plot.spray(self.x, self.y)
				else:
					self.gcode.process(line)				


	def main(self):
		self.plot.animate(callback = self.update, steps = self.steps, freq = self.timeStep)
	
if __name__ == '__main__':
	simulator = simulate(timeStep = 1)
	simulator.main()