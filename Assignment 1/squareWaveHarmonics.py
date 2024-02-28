# Question 1
import numpy as np
import matplotlib.pyplot as plt

# Question 1a
T = 2e-9
A = 5

def squareFourierCoeff(A, n):
    if n == 0:
        return A / 2
    if n % 2 == 0:
        return 0
    else:
        return 2*A / (n * np.pi)

# Question 1b
n = range(0,41)
coeffs = [squareFourierCoeff(A, i) for i in n] 
plt.stem(n, coeffs)
plt.grid(True)
plt.title("Square Wave Harmonics (1b)")
plt.xlabel("Harmonic Number")
plt.ylabel("Harmonic Amplitude (V)")
plt.show()


# Question 1c
def plotSquareWaveHarmonics(n, T, A):
    t = np.linspace(0, 2*T, 1000)
    y = np.ones(len(t))
    y = squareFourierCoeff(A, 0) * y
    plt.plot(t/1e-9, y, label=f"n=DC")
    for i in range(1, n+1):
        # Plot the harmonics, not the sum
        y = squareFourierCoeff(A, i) * np.sin(2 * np.pi * i * t / T)
        plt.plot(t/1e-9, y, label=f"n={i}")
    plt.legend()    
    plt.grid(True)
    plt.title("Square Wave Harmonics (1c)")
    plt.xlabel("Time (ns)")
    plt.ylabel("Amplitude (V)")
    plt.show()
plotSquareWaveHarmonics(5, T, A)

# Question 1d
def plotSquareWaveHarmonicsFullWave(n, T, A):
    t = np.linspace(0, 2*T, 1000)
    y = np.ones(len(t))
    y = squareFourierCoeff(A, 0) * y
    plt.plot(t/1e-9, y, label=f"n=DC")
    for i in range(1, n+1):
        # Plot the harmonics, not the sum
        y += squareFourierCoeff(A, i) * np.sin(2 * np.pi * i * t / T)
        plt.plot(t/1e-9, y, label=f"n<{i}")
    plt.legend()    
    plt.grid(True)
    plt.title("Square Wave Harmonics Progressive Sum (1d)")
    plt.xlabel("Time (ns)")
    plt.ylabel("Amplitude (V)")
    plt.show()
plotSquareWaveHarmonicsFullWave(5, T, A)


# Question 1e
def plotSquareWaveRisingEdge(n, T, A, nToPlot):
    t = np.linspace(0, T/4, 1000)
    y = np.ones(len(t))
    y = squareFourierCoeff(A, 0) * y
    #plt.plot(t/1e-9, y, label=f"n=DC")
    for i in range(1, n+1):
        # Plot the harmonics, not the sum
        y += squareFourierCoeff(A, i) * np.sin(2 * np.pi * i * t / T)
        if i in nToPlot:
            plt.plot(t/1e-9, y, label=f"n<={i}")
    plt.legend()    
    plt.grid(True)
    plt.title("Square Wave Rising Edge (1d)")
    plt.xlabel("Time (ns)")
    plt.ylabel("Amplitude (V)")
    plt.show()
plotSquareWaveRisingEdge(35, T, A, [1,3,5,35])

