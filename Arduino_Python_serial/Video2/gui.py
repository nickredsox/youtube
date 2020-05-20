import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np



class TopPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent = parent)
		
		self.figure = Figure()
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.EXPAND)
		self.SetSizer(self.sizer)
		self.axes.set_xlabel("Time")
		self.axes.set_ylabel("A/D Counts")
		
	def draw(self):
		x = np.arange(0,3,0.01)
		y = np.sin(np.pi*x)
		self.axes.plot(x,y)
		
	def changeAxes(self, min, max):
		self.axes.set_ylim(float(min), float(max))
		self.canvas.draw()

class BottomPanel(wx.Panel):
	def __init__(self, parent, top):
		wx.Panel.__init__(self, parent = parent)

		self.graph = top
		
		self.togglebuttonStart = wx.ToggleButton(self, id = -1, label = "Start", pos = (10,10))
		self.togglebuttonStart.Bind(wx.EVT_TOGGLEBUTTON, self.OnStartClick)
		
		labelChannels = wx.StaticText(self, -1, "Analog Inputs", pos = (200,10))
		self.cb1 = wx.CheckBox(self, -1, label = "A0", pos = (200,30))
		self.cb2 = wx.CheckBox(self, -1, label = "A1", pos = (200,45))
		self.cb3 = wx.CheckBox(self, -1, label = "A2", pos = (200,60))
		self.cb4 = wx.CheckBox(self, -1, label = "A3", pos = (200,75))
		self.Bind(wx.EVT_CHECKBOX, self.OnChecked)
		
		self.textboxSampleTime = wx.TextCtrl(self, -1, "1000", pos = (200,115), size = (50,-1))
		self.buttonSend = wx.Button(self, -1, "Send", pos = (250, 115), size = (50, -1))
		self.buttonSend.Bind(wx.EVT_BUTTON, self.OnSend)

		labelMinY = wx.StaticText(self, -1, "Min Y ", pos = (400,10))
		self.textboxMinYAxis = wx.TextCtrl(self, -1, "0", pos = (400,30))
		labelMaxY = wx.StaticText(self, -1, "Max Y", pos = (400, 60))
		self.textboxMaxYAxis = wx.TextCtrl(self, -1, "1024", pos = (400,80))
		
		self.buttonRange = wx.Button(self, -1, "Set Y Axis", pos =(400,105))
		self.buttonRange.Bind(wx.EVT_BUTTON, self.SetButtonRange)
		
	def SetButtonRange(self, event):
		min = self.textboxMinYAxis.GetValue()
		max = self.textboxMaxYAxis.GetValue()
		self.graph.changeAxes(min,max)
		
	def OnSend(self, event):
		val = self.textboxSampleTime.GetValue()
		print(val)
		
		
	def OnChecked(self, event):
		cb = event.GetEventObject()
		print("%s is clicked" % (cb.GetLabel()))
		
	def OnStartClick(self, event):
		val = self.togglebuttonStart.GetValue()
		if (val == True):
			self.togglebuttonStart.SetLabel("Stop")
		else:
			self.togglebuttonStart.SetLabel("Start")
			
		
		
class Main(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Arduino Oscilloscope", size = (600,600))
		
		splitter = wx.SplitterWindow(self)
		top = TopPanel(splitter)
		bottom = BottomPanel(splitter, top)
		splitter.SplitHorizontally(top, bottom)
		splitter.SetMinimumPaneSize(400)
		top.draw()








if __name__ == "__main__":
	app = wx.App()
	frame = Main()
	frame.Show()
	app.MainLoop()
