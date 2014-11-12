#!/usr/bin/env python
from prepar3d import event_listener
from prepar3d._internal import simconnect
import matplotlib.pyplot as plt
import numpy

plt.ion()

class FrameCounter(event_listener.EventListener):
    def __init__(self, hanlde):
        super(FrameCounter, self).__init__(handle, 'Frame', simconnect.SIMCONNECT_RECV_ID.SIMCONNECT_RECV_ID_EVENT_FRAME, frequency=100)
        self.frames = list()
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'r--')
        self.ax.set_autoscaley_on(True)
        self.ax.grid()

    def event(self, event, cbData, blubb):
        self.frames.append(event.fFrameRate)
        self.lines.set_ydata(self.frames)
        self.lines.set_xdata(range(0,len(self.frames)))
        self.ax.set_xlim(0, len(self.frames))
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


(result, handle) = simconnect.SimConnect_Open("Test", None, 0, None, 0)

fc = FrameCounter(handle)
fc.start()

print('fc startet...')

fc.join()

simconnect.SimConnect_Close(handle)