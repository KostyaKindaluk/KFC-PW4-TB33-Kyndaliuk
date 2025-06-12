import numpy as np
from scipy.integrate import solve_ivp


class LorenzAttractor:
	def __init__(self, sigma=10, beta=8/3, rho=28):
		self.sigma = sigma
		self.beta = beta
		self.rho = rho
		self.sol1 = None
		self.sol2 = None
		self.t_eval = None


	def lorenz(self, t, state):
		x, y, z = state
		return [self.sigma*(y - x), x*(self.rho - z) - y, x*y - self.beta*z]

	def calculate(self, t_span, num_points, initial_state_1, initial_state_2):
		self.t_eval = np.linspace(t_span[0], t_span[1], num_points)
		self.sol1 = solve_ivp(self.lorenz, t_span, initial_state_1, t_eval=self.t_eval)
		self.sol2 = solve_ivp(self.lorenz, t_span, initial_state_2, t_eval=self.t_eval)
		return self.sol1, self.sol2, self.t_eval

	def get_distance(self):
		if self.sol1 is None or self.sol2 is None:
			raise ValueError("No previous calculations, do calculate() first!")
		return np.linalg.norm(self.sol1.y - self.sol2.y, axis=0)