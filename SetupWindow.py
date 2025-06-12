import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Frame, Label, Button


class SetupWindow:
	def __init__(self, on_start_callback):
		self.on_start_callback = on_start_callback

		self.root = tk.Tk()
		self.root.title("Setting up the Lorenz Attractor")

		style = Style(theme="flatly")
		self.style = style

		self.frame = Frame(self.root, padding=20)
		self.frame.pack(fill='both', expand=True)

		Label(self.frame, text="Amount of points(1000 - 20000):").pack(anchor='w')
		self.num_points_var = tk.IntVar(value=10000)
		self.num_points_scale = tk.Scale(self.frame, from_=1000, to=20000,
			variable=self.num_points_var, orient='horizontal',
			length=300)
		self.num_points_scale.pack()

		Label(self.frame, text="Error for starting x value(-0.001 - 0.001):").pack(anchor='w')
		self.error_var = tk.DoubleVar(value=0.0001)
		self.error_scale = tk.Scale(self.frame, from_=-0.001, to=0.001,
			variable=self.error_var, orient='horizontal',
			length=300, resolution=0.00001)
		self.error_scale.pack()

		self.start_button = Button(self.frame, text="Show attractor and error chart", command=self.start)
		self.start_button.pack(pady=10)

	def start(self):
		num_points = self.num_points_var.get()
		error = self.error_var.get()
		self.root.destroy()
		self.on_start_callback(num_points, error)

	def run(self):
		self.root.mainloop()