import matplotlib.pyplot as plt


def show_3d_plot(sol1, sol2):
	fig = plt.figure(figsize=(10, 7))
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(sol1.y[0], sol1.y[1], sol1.y[2], label='Starting state - [1,1,1]')
	ax.plot(sol2.y[0], sol2.y[1], sol2.y[2], label='Starting state(with error)', linestyle='--')
	ax.legend()
	plt.title('The Lorenz Attractor')
	plt.show()