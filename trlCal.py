import numpy as np
import skrf as rf
import matplotlib.pyplot as plt

# Frequency definition
freq = rf.Frequency(1, 10, 201, unit='ghz')

# Generate ideal standards
# Thru: ideal zero-length line
thru = rf.Network(frequency=freq, s=np.zeros((len(freq), 2, 2)))

# Reflect: ideal short on both ports
reflect_s = -np.ones((len(freq), 2, 2))
np.fill_diagonal(reflect_s[:, :, :], -1)
reflect = rf.Network(frequency=freq, s=reflect_s)

# Line: 90-degree transmission line (e.g., λ/4 at center frequency)
line_length = 0.025  # in meters (example)
er = 4.0  # relative permittivity
c = 3e8 / np.sqrt(er)  # wave speed
beta = 2 * np.pi * freq.f / c
s21_line = np.exp(-1j * beta * line_length)
line_s = np.zeros((len(freq), 2, 2), dtype=complex)
line_s[:, 0, 1] = s21_line
line_s[:, 1, 0] = s21_line
line = rf.Network(frequency=freq, s=line_s)

# Simulate DUT with some arbitrary behavior (e.g., 6 dB attenuator + phase shift)
atten = 10**(-6/20)  # linear scale
phase = np.exp(-1j * np.pi * freq.f / freq.f[-1])
dut_s = np.zeros((len(freq), 2, 2), dtype=complex)
dut_s[:, 0, 1] = atten * phase
dut_s[:, 1, 0] = atten * phase
dut_ideal = rf.Network(frequency=freq, s=dut_s)

# Add error model (for demonstration only: some arbitrary error terms)
def add_error(s, e_mag=0.05):
    return s + (e_mag * (np.random.randn(*s.shape) + 1j*np.random.randn(*s.shape)))

measured_dut = rf.Network(frequency=freq, s=add_error(dut_ideal.s))

# Simulate measured standards (imperfect versions of ideal standards)
measured_thru = rf.Network(frequency=freq, s=add_error(thru.s))
measured_reflect = rf.Network(frequency=freq, s=add_error(reflect.s))
measured_line = rf.Network(frequency=freq, s=add_error(line.s))

# Build the TRL calibration
cal = rf.TRL(
    frequency=freq,
    measured=[measured_thru, measured_reflect, measured_line],
    ideals=[None, None, None]  # Tell scikit-rf to use estimated ideal models
)

# Apply the calibration
dut_calibrated = cal.apply_cal(measured_dut)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(freq.f, 20 * np.log10(np.abs(measured_dut.s[:, 0, 1])), label='Measured DUT')
plt.plot(freq.f, 20 * np.log10(np.abs(dut_calibrated.s[:, 0, 1])), label='Calibrated DUT')
plt.plot(freq.f, 20 * np.log10(np.abs(dut_ideal.s[:, 0, 1])), '--', label='Ideal DUT')
plt.title('TRL Calibration (|S21| in dB)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
