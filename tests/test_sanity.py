import pytest
import numpy as np
from lorenz import LorenzAttractor



def test_lorenz_calculation_runs():
	attractor = LorenzAttractor()
	t_span = (0, 10)
	num_points = 100
	initial_state_1 = [0., 1., 1.05]
	initial_state_2 = [0.0001, 1., 1.05]

	sol1, sol2, t_eval = attractor.calculate(t_span, num_points, initial_state_1, initial_state_2)

	assert len(t_eval) == num_points
	assert sol1.y.shape == sol2.y.shape

def test_gui_initializes():
	try:
		from SetupWindow import SetupWindow
		def dummy_callback(a, b):
				pass
		app = SetupWindow(dummy_callback)
		app.root.update()
		app.root.destroy()
	except Exception as e:
		pytest.fail(f"GUI doesn't work: {e}")