import numpy as np
import matplotlib.pyplot as plt

import nengo
from nengo.dists import Uniform
from nengo.utils.ensemble import tuning_curves
from nengo.processes import WhiteNoise
from nengo.utils.matplotlib import rasterplot



def regulate(n, radius=0.9):
    intercepts = np.linspace(-radius, radius, n)
    encoders = np.tile([[1], [-1]], (n // 2, 1))
    intercepts *= encoders[:, 0]
    return intercepts, encoders




model = nengo.Network()

with model:
    input_signal = nengo.Node(lambda t: t * 2 - 1)
    input_probe = nengo.Probe(input_signal)

NEURONS = 20

intercepts, encoders = regulate(NEURONS)
with model:
    Net = nengo.Ensemble(
        NEURONS,
        dimensions=1,
        intercepts=intercepts,
        max_rates=Uniform(70, 100),
        encoders=encoders,
        neuron_type=nengo.LIF()
    )


with nengo.Simulator(model) as sim:
    eval_points, activities = tuning_curves(Net, sim)

plt.figure()
plt.plot(eval_points, activities, lw=2)
plt.show()

# ---------------------------------------------------------------------------

with model:
    nengo.Connection(input_signal, Net)
    Net_spikes = nengo.Probe(Net.neurons)

with nengo.Simulator(model) as sim:
    sim.run(5)

plt.figure()
rasterplot(sim.trange(), sim.data[Net_spikes])
plt.show()

# ---------------------------------------------------------------------------

with model:
    filtered = nengo.Probe(Net, synapse=0.01)

with nengo.Simulator(model) as sim:
    sim.run(5)


plt.figure()
plt.plot(sim.trange(), sim.data[input_probe])
plt.plot(sim.trange(), sim.data[filtered])
plt.xlim(0,4)
plt.show()

# ---------------------------------------------------------------------------