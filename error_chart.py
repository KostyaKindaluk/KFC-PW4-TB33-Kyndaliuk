import matplotlib.pyplot as plt


def show_error_chart(t_eval, distance):
	plt.figure(figsize=(10, 5))
	plt.plot(t_eval, distance)
	plt.yscale('log')
	plt.xlabel('Час')
	plt.ylabel('Distance between trajectories(log-scale)')
	plt.title('Error chart')
	plt.grid()
	plt.show()