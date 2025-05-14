def generate_s1p(filename, freq_data, s11_data, freq_unit='GHz', format_type='MA', z0=50):
    """
    Generate a .s1p file with given frequency and S11 data.

    Parameters:
    - filename: Output .s1p filename (e.g., 'output.s1p')
    - freq_data: List or array of frequency points
    - s11_data: List of S11 values (magnitude, angle in degrees)
    - freq_unit: Frequency unit (e.g., 'GHz', 'MHz', 'Hz')
    - format_type: 'MA' for magnitude/angle, 'DB' for dB/angle, 'RI' for real/imag
    - z0: Characteristic impedance (default 50 ohms)
    """
    assert len(freq_data) == len(s11_data), "Mismatch in data length"

    header = f"# {freq_unit} S {format_type} R {z0}"
    lines = [header]

    for f, (mag, ang) in zip(freq_data, s11_data):
        line = f"{f:.6f} {mag:.6f} {ang:.6f}"
        lines.append(line)

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    print(f"S1P file '{filename}' written successfully.")

# Example usage
import numpy as np

# Frequency from 1 to 10 GHz
freqs = np.linspace(1, 10, 10)

# Dummy S11 data: magnitude and phase
s11_vals = [(0.9, -30 + i * -5) for i in range(len(freqs))]

# Generate file
generate_s1p("example.s1p", freqs, s11_vals)
