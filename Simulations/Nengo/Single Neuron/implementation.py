import matplotlib.pyplot as plt
import numpy as np
import nengo
from nengo.utils.matplotlib import rasterplot
from nengo.dists import Uniform



model = nengo.Network()


with model:
    neuron = nengo.Ensemble(n_neurons=1,
                            dimensions=1,
                            intercepts=Uniform(-0.5,-0.5),
                            max_rates=Uniform(2,8),
                            encoders=[[-0.01]]
                            )



with model:
    input_signal = nengo.Node(lambda t: ( 2 * np.sin(t)) )
    nengo.Connection(input_signal, neuron)


with model:
    input_probe = nengo.Probe(input_signal)
    spikes = nengo.Probe(neuron.neurons)
    voltage = nengo.Probe(neuron.neurons, "voltage")
    filtered = nengo.Probe(neuron, synapse=0.01)


with nengo.Simulator(model) as sim:
    sim.run(10)


plt.figure()
plt.plot(sim.trange(), sim.data[filtered])
plt.plot(sim.trange(), sim.data[input_probe])
# plt.xlim(2, 4)
plt.show()