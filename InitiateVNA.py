import numpy as np
import matplotlib.pyplot as plt

class VNA_GUI:
    def __init__(self):
        # Initialize data arrays for plotting
        self.freq_data = np.array([])  # To store frequency points
        self.magnitude_data = np.array([])  # To store magnitude points

    def start_measurement(self, freq_input):
        # Simulate data collection or interface with your VNA here
        # Example: Collecting dummy data
        try:
            freq = float(freq_input)  # Get the frequency input
            self.freq_data = np.linspace(1, 10, 100)  # Example frequency range (1 to 10 GHz)
            self.magnitude_data = 20 * np.log10(np.abs(np.sin(self.freq_data * np.pi / 10)))  # Example data
            
            self.update_plot()  # Update plot with new data

            print("Measurement Complete!")
        except ValueError:
            print("Invalid frequency input!")

    def update_plot(self):
        # Plot the frequency vs magnitude
        plt.figure(figsize=(6, 4))
        plt.plot(self.freq_data, self.magnitude_data, label="S-Parameter Magnitude")
        plt.title("S-Parameter Plot")
        plt.xlabel("Frequency (GHz)")
        plt.ylabel("Magnitude (dB)")
        plt.legend()
        plt.show()

# Example usage
vna_gui = VNA_GUI()
vna_gui.start_measurement(5.0)  # Start measurement with 5 GHz frequency input
