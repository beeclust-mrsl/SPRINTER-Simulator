#! /usr/bin/env python

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle

class vizualize():

	def __init__(self, x_size = 100, y_size = 100):
		self.indexX = 0
		self.indexY = 10

		self.x_size = x_size
		self.y_size = y_size

		self.xs = np.array([])
		self.ys = np.array([])

		self.mask = np.array([])

		self.grid = plt.figure()

		self.ax = self.grid.add_subplot(111)
		self.ax = plt.axes(xlim=(0, self.x_size), ylim=(0, self.y_size))
		plt.axis('scaled')

		self.path, = self.ax.plot([], [], lw=1, color = 'b', linestyle = '--')
		self.feed, = self.ax.plot([], [], lw=2, color = 'k')

		self.circle = Circle((0, 0), radius=2, color='r')
		self.ax.add_patch(self.circle)

		#self.ax.set_title('Grid Map')


	def plotStep(self):
		self.x = self.indexX
		self.y = self.indexY

		self.indexX+=1
		self.indexY+=1


	def appendPlot(self, x, y, feedrate):
		self.xs = np.append(self.xs, x)
		self.ys = np.append(self.ys, y)

		if feedrate:
			self.mask = np.append(self.mask, 0)
		else:
			self.mask = np.append(self.mask, 1)

		maskedX = np.ma.masked_where(self.mask==1, self.xs)
		maskedY = np.ma.masked_where(self.mask==1, self.ys)

		self.path.set_data(self.xs, self.ys)
		self.feed.set_data(maskedX, maskedY)

		self.circle.center = (x, y)

		return self.path, self.circle


	def animate(self, callback, steps, freq):
		anim = animation.FuncAnimation(self.grid, func=callback, frames=steps, interval=freq, repeat=False)
		plt.show()

x = 0
y = 0



obj = vizualize()

def cb(i):
	if i>10 and i<50:
		a = 1
	else:
		a = 0
	obj.appendPlot(i,i,a)

if __name__ == '__main__':
	obj.animate(cb, steps=100, freq=100)