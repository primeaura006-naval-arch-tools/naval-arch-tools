import numpy as np
import matplotlib.pyplot as plt

# Constants
rho = 1025
Cd = 0.2
A = 500

# Speed array — 1 se 20 m/s
V = np.linspace(1, 20, 100)

# Resistance calculate karo — har speed pe
# Formula — R = 0.5 * rho * V² * Cd * A

# KHUD SE LIKHO YE LINE 👇
R = 0.5*(V**2)*A*Cd*rho

# Graph banao
'''
plt.plot(V, R)
plt.xlabel("Ship Speed (m/s)")
plt.ylabel("Resistance (ohm)")
plt.title("Ship Speed vs Resistance 🚢")
plt.grid(True)
'''

plt.plot(V, R, color='blue', linewidth=2, label='Resistance')
plt.xlabel("Ship Speed (m/s)", fontsize=12)
plt.ylabel("Resistance (N)", fontsize=12)
plt.title("Ship Speed vs Resistance", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()


P = R * V  # Power = Resistance × Speed

plt.figure(figsize=(12, 5))

# Graph 1
plt.subplot(1, 2, 1)
plt.plot(V, R, color='blue', linewidth=2,label="Resistance")
plt.title("Speed vs Resistance")
plt.xlabel("Speed (m/s)")
plt.ylabel("Resistance (N)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Graph 2
plt.subplot(1, 2, 2)
plt.plot(V, P/1000, color='red', linewidth=2)
plt.title("Speed vs Power")
plt.xlabel("Speed (m/s)")
plt.ylabel("Power (kW)")
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

#1
R_cargo = 0.5 * rho * (V**2) * 0.4 * 800
R_warship = 0.5 * rho * (V**2) * 0.25 * 400
R_yacht = 0.5 * rho * (V**2) * 0.15 * 150
#!

plt.subplot(2,2,1)
plt.plot(V,R_cargo,color='green',linewidth=3)
plt.title("Speed vs R cargo")
plt.xlabel("Speed (m/s)")
plt.ylabel("R cargo (N)")
plt.grid(True, linestyle='--', alpha=0.7)

#!!
plt.subplot(2, 2, 2)
plt.plot(V, R_warship, color='red', linewidth=2)
plt.title("Speed vs R warship")
plt.xlabel("Speed (m/s)")
plt.ylabel("R warship (N)")
plt.grid(True, linestyle='--', alpha=0.7)

#!!!
plt.subplot(2, 2, 3)
plt.plot(V, R_yacht, color='red', linewidth=2)
plt.title("Speed vs R yacht")
plt.xlabel("Speed (m/s)")
plt.ylabel("R yacht (N)")
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(V, R_cargo,   color='green', linewidth=2, label='Cargo Ship')
plt.plot(V, R_warship, color='blue',  linewidth=2, label='Warship')
plt.plot(V, R_yacht,   color='red',   linewidth=2, label='Yacht')
plt.title("3 Ships Speed vs Resistance Comparison")
plt.xlabel("Speed (m/s)")
plt.ylabel("Resistance (N)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
