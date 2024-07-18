import cirq
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a simple quantum circuit to simulate the collapse of a star
qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit()

# Apply a series of gates to simulate the collapse
circuit.append(cirq.H(qubit))  # Hadamard gate
circuit.append(cirq.rx(np.pi/2)(qubit))  # Rotation around X-axis
circuit.append(cirq.ry(np.pi/2)(qubit))  # Rotation around Y-axis
circuit.append(cirq.rz(np.pi/2)(qubit))  # Rotation around Z-axis

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.simulate(circuit)
state_vector = result.final_state_vector

# Extract the real and imaginary parts of the statevector
real_part = np.real(state_vector)
imag_part = np.imag(state_vector)

# Create a 3D plot of the statevector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the real part
ax.quiver(0, 0, 0, real_part[0], real_part[1], 0, color='r', label='Real part')  # Adjusted to 2D

# Plot the imaginary part
ax.quiver(0, 0, 0, imag_part[0], imag_part[1], 0, color='b', label='Imaginary part')  # Adjusted to 2D

# Set limits to better visualize the 2D vectors in 3D space
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Representation of Star Collapse Simulation')
ax.legend()

plt.show()

# Calculate the 2D line components
real_2d = real_part[:2]  # Only take the first two components
imag_2d = imag_part[:2]  # Only take the first two components

real_2d, imag_2d
