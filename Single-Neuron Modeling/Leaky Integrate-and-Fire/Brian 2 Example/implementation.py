import matplotlib.pyplot as plt
import brian2 as b2
import numpy as np


def gen_step_current(start_time: int, end_time: int, unit_time, amplitude, add_zero=True):

    assert b2.units.fundamentalunits.have_same_dimensions(amplitude, b2.amp)
    temp_size = end_time + 1 + add_zero

    temp = np.zeros((temp_size, 1)) * b2.amp

    temp[start_time: end_time + 1, 0] = amplitude

    current = b2.TimedArray(temp, dt=1. * unit_time)
    return current



def simulate_LIF_neuron(I, simulation_time=5 * b2.ms):
    v_rest = -70.0 * b2.mV
    R = 10.0 * b2.Mohm
    tau = 8.0 * b2.ms
    

    eqs = """dv/dt = ( -(v-v_rest) + R * I(t,i) ) / tau : volt"""

    ref_period = 2.0 * b2.ms
    v_r = -75 * b2.mV
    theta_thresh = -50.0 * b2.mV

    neuron = b2.NeuronGroup(
        1, model=eqs, reset="v=v_r", threshold="v>theta_thresh",
        refractory=ref_period, method="euler")
    
    neuron.v = v_rest  

    voltages = b2.StateMonitor(neuron, ["v"], record=True)
    spikes = b2.SpikeMonitor(neuron)

    b2.run(simulation_time)
    return voltages, spikes


step_current = gen_step_current(
        start_time=100, end_time=200, unit_time=b2.ms,
        amplitude=8.0 * b2.namp)


(voltages, spikes) = simulate_LIF_neuron(I=step_current, simulation_time=400 * b2.ms)

b2.plot(voltages.t / b2.ms, voltages.v[0])
#b2.plot(spikes)
plt.show()

