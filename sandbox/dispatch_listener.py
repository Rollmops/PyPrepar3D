#!/usr/bin/env python
import prepar3d
from prepar3d._internal import simconnect
import matplotlib.pyplot as plt
import numpy
from multiprocessing import freeze_support

plt.ion()

class FrameCounter(prepar3d.EventListener):
    def __init__(self, connection):
        super(FrameCounter, self).__init__(connection, 'Frame', simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME, frequency=100)
        self.frames = list()
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([], [], 'r--')
        self.ax.set_autoscaley_on(True)
        self.ax.grid()

    def event(self, event, cbData, blubb):
        self.frames.append(event.fFrameRate)
        self.lines.set_ydata(self.frames)
        self.lines.set_xdata(range(0, len(self.frames)))
        self.ax.set_xlim(0, len(self.frames))
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

if __name__ == '__main__':

    connection = prepar3d.Connection('Test', open=True)
    
    fc = FrameCounter(connection)
    fc.start()
    
    print('fc startet...')

    fc.join()
    connection.close()