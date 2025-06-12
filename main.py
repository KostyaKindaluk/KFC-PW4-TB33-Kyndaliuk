from lorenz import LorenzAttractor;
from SetupWindow import SetupWindow;
from attractor import show_3d_plot
from error_chart import show_error_chart


def main(num_points, error):
	t_span = (0, 30)
	initial_state_1 = [1.0, 1.0, 1.0]
	initial_state_2 = [1.0 + error, 1.0, 1.0]

	model = LorenzAttractor()
	sol1, sol2, t_eval = model.calculate(t_span, num_points, initial_state_1, initial_state_2)

	show_3d_plot(sol1, sol2)
	distance = model.get_distance()
	show_error_chart(t_eval, distance)

if __name__ == "__main__":
	def on_start(num_points, error):
		main(num_points, error)

	app = SetupWindow(on_start)
	app.run()