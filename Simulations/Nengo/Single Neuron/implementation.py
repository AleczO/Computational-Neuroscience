import matplotlib.pyplot as plt
import numpy as np
import nengo
from nengo.utils.matplotlib import rasterplot



model = nengo.Network()


with model:
    neuron = nengo.Ensemble(n_neurons=1,
                            dimensions=1,
                            neuron_type=nengo.LIF(),
                            encoders=[[1]]
                            )



with model:
    input_signal = nengo.Node(lambda t: np.cos(t * 8) )
    nengo.Connection(input_signal, neuron)


with model:
    input_probe = nengo.Probe(input_signal)
    spikes = nengo.Probe(neuron.neurons)
    voltage = nengo.Probe(neuron.neurons, "voltage")
    filtered = nengo.Probe(neuron, synapse=0.01)


with nengo.Simulator(model) as sim:
    sim.run(1)


plt.figure()
plt.plot(sim.trange(), sim.data[filtered])
plt.plot(sim.trange(), sim.data[input_probe])
plt.show()


plt.figure()
rasterplot(sim.trange(), sim.data[spikes])
plt.show()