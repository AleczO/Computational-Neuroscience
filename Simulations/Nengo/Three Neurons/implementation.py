import matplotlib.pyplot as plt
import numpy as np

import nengo
from nengo.dists import Uniform
from nengo.processes import BrownNoise

from nengo.utils.matplotlib import rasterplot


model = nengo.Network()

with model:
    neurons = nengo.Ensemble(
        n_neurons=3,
        dimensions=1,
        intercepts=Uniform(0,1),
        max_rates=Uniform(100,100),
        noise=BrownNoise()
    )


with model:
    input_signal = nengo.Node(lambda t : np.cos(t))
    nengo.Connection(input_signal, neurons, synapse=0.01)


with model:
    input_probe = nengo.Probe(input_signal)
    spikes = nengo.Probe(neurons.neurons)
    voltage = nengo.Probe(neurons.neurons, "voltage")
    filtered = nengo.Probe(neurons, synapse=0.01)


with nengo.Simulator(model) as sim:
    sim.run(2)

t = sim.trange()


plt.figure()
plt.plot(t, sim.data[filtered])
plt.plot(t, sim.data[input_probe])

plt.show()