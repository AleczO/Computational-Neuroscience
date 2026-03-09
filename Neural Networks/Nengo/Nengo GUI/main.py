import nengo

model = nengo.Network()

with model:
    network = nengo.Ensemble(100, dimensions=3, radius=1.0)
    input = nengo.Node([0])
    nengo.Connection(input, network[0])
