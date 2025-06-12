import pytest
from lorenz import LorenzAttractor


def test_small_initial_perturbation_distance():
	attractor = LorenzAttractor()
	t_span = (0, 10)
	num_points = 500
	initial_state_1 = [0.0, 0.0, 0.0]
	initial_state_2 = [0.0001, 0.0, 0.0]

	attractor.calculate(t_span, num_points, initial_state_1, initial_state_2)
	distance = attractor.get_distance()

	assert distance[0] < 0.001
	assert max(distance) < 100