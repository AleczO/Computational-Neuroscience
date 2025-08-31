import nengo
import matplotlib.pyplot as plt

model = nengo.Network()
with model:
    input_signal = nengo.Node(lambda t: t**2 * 2 - 1)
    input_probe = nengo.Probe(input_signal)

with nengo.Simulator(model) as sim:
    sim.run(2.0)

plt.figure()
plt.plot(sim.trange(), sim.data[input_probe])
plt.xlim(0, 2)
plt.show()


