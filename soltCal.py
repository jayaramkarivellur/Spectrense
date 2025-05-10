import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

# Frequency definition
freq = rf.Frequency(1, 10, 101, 'ghz')

# Create ideal calibration standards
short = rf.Network(frequency=freq, s=np.full((101, 1, 1), -1))  # S11 = -1
open_ = rf.Network(frequency=freq, s=np.full((101, 1, 1), 1))   # S11 = +1
load = rf.Network(frequency=freq, s=np.full((101, 1, 1), 0))    # S11 = 0

# Simulate raw measurements with errors (example: directivity + reflection tracking)
# Here, we create "measured" values by distorting the ideal ones
def add_error(ideal, gamma_d=0.05, gamma_r=0.1):
    return (gamma_d + gamma_r * ideal)  # simplified error model

measured_short = rf.Network(frequency=freq, s=add_error(short.s))
measured_open  = rf.Network(frequency=freq, s=add_error(open_.s))
measured_load  = rf.Network(frequency=freq, s=add_error(load.s))

# Perform one-port calibration
cal = rf.OnePort(
    frequency=freq,
    measured=[measured_short, measured_open, measured_load],
    ideals=[short, open_, load]
)

# Apply calibration to a DUT (Device Under Test)
# Let's define a DUT as a reflection of +0.5 (S11 = 0.5)
dut_ideal = rf.Network(frequency=freq, s=np.full((101, 1, 1), 0.5))
dut_measured = rf.Network(frequency=freq, s=add_error(dut_ideal.s))

# Correct the measurement
dut_corrected = cal.apply_cal(dut_measured)

# Plot comparison
plt.figure(figsize=(10, 5))
plt.plot(freq.f, np.abs(dut_measured.s[:, 0, 0]), label='Measured')
plt.plot(freq.f, np.abs(dut_corrected.s[:, 0, 0]), label='Calibrated')
plt.plot(freq.f, np.abs(dut_ideal.s[:, 0, 0]), '--', label='Ideal')
plt.title('One-Port SOL Calibration (Magnitude of S11)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('|S11|')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
