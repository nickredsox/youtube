import tkinter as tk
import xarm

class GUI():
	def __init__(self):
		self.robot = self.connect_to_robot()
		if self.robot is None:
			print("Exiting program")
			exit()
		print(self.robot)
		self.mw = tk.Tk()
		self.mw.geometry('400x400')

		#Labels
		self.label_gripper = tk.Label(self.mw, text = "Gripper")
		self.label_link2 = tk.Label(self.mw, text = "Link 2")
		self.label_link3 = tk.Label(self.mw, text = "Link 3")
		self.label_link4 = tk.Label(self.mw, text = "Link 4")
		self.label_link5 = tk.Label(self.mw, text = "Link 5")
		self.label_link6 = tk.Label(self.mw, text = "Link 6")

		#Slidebar = Scales
		self.scale_gripper = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_link2 = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_link3 = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_link4 = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_link5 = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_link6 = tk.Scale(self.mw, from_ = 0, to = 1000,
										orient = tk.HORIZONTAL, 
										command = self.send_val)
		self.scale_gripper.set(500)
		self.scale_link2.set(500)
		self.scale_link3.set(500)
		self.scale_link4.set(500)
		self.scale_link5.set(500)
		self.scale_link6.set(500)


		self.label_gripper.place(x = 10, y = 10)
		self.label_link2.place(x = 10, y = 60)
		self.label_link3.place(x = 10, y = 110)
		self.label_link4.place(x = 10, y = 160)
		self.label_link5.place(x = 10, y = 210)
		self.label_link6.place(x = 10, y = 260)

		self.scale_gripper.place(x = 100, y = 0)
		self.scale_link2.place(x = 100, y = 50)
		self.scale_link3.place(x = 100, y = 100)
		self.scale_link4.place(x = 100, y = 150)
		self.scale_link5.place(x = 100, y = 200)
		self.scale_link6.place(x = 100, y = 250)

		tk.mainloop()

	def send_val(self, evt):
		gripper_val = self.scale_gripper.get()
		link2_val = self.scale_link2.get()
		link3_val = self.scale_link3.get()
		link4_val = self.scale_link4.get()
		link5_val = self.scale_link5.get()
		link6_val = self.scale_link6.get()

		self.robot.setPosition(1, gripper_val, wait=False)
		self.robot.setPosition(2, link2_val, wait=False)
		self.robot.setPosition(3, link3_val, wait=False)
		self.robot.setPosition(4, link4_val, wait=False)
		self.robot.setPosition(5, link5_val, wait=False)
		self.robot.setPosition(6, link6_val, wait=False)

	def connect_to_robot(self):
		try:
			arm = xarm.Controller("USB")
			return arm
		except:
			print("Problem connecting to robot. Check connections")
			return None





if __name__ == '__main__':
	gui = GUI()