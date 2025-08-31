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
        max_rates=Uniform(100,100),
        neuron_type=nengo.LIF(),
        noise=BrownNoise(),
        encoders=[[1],[1],[-10]]

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



times = sim.trange()

plt.figure()
plt.plot(times, sim.data[filtered])
plt.plot(times, sim.data[input_probe])
plt.show()


plt.figure()
rasterplot(sim.trange(), sim.data[spikes])
plt.xlim(0, 1)
plt.show()