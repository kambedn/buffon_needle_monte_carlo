import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec


SPACE = 1  # The spacing between grid lines
NED_LEN = 0.5  # The length of the needle
N = 1000  # The number of needles to simulate and plot
random.seed(54654324)


def plot_grid(ax, line_spacing):
    """
    Plots grid lines on the given axes.

    Parameters:
        ax (matplotlib.axes.Axes): The axes object to plot on.
        line_spacing (float): The spacing between grid lines.

    Returns:
        None
    """
    for y in np.arange(-10, 10.5, line_spacing):
        ax.plot([-10, 10], [y, y], color='black', alpha=0.3)


def estimate_pi(vec, needle_len, spacing):
    """
    Estimates the value of π using Buffon's needle problem.

    Parameters:
        vec (list): A list representing the success vector.
        needle_len (float): The length of the needle.
        spacing (float): The spacing between grid lines.

    Returns:
        float: The estimated value of π.
    """
    prob = np.sum(vec) / len(vec)
    if not prob:
        prob = 1e-6
    pi_estimation = 2 * needle_len / (spacing * prob)
    return pi_estimation


def buffon_needle_problem(n, needle_len, spacing, plot=False, axis=None):
    """
    Simulate Buffon's needle problem and calculate the success vector.

    Parameters:
        n (int): The number of needles to simulate.
        needle_len (float): The length of the needle.
        spacing (float): The spacing between grid lines.
        plot (bool, optional): Whether to plot the needles. Defaults to False.
        axis (matplotlib.axes.Axes, optional): The axes object to plot on. Defaults to None.

    Returns:
        list: A list representing the success vector.
    """
    success_vector = []
    for _ in range(n):
        x_start = random.uniform(-10, 10)
        y_start = random.uniform(-10, 10)
        angle = math.radians(random.uniform(0, 180))

        x_end = x_start + needle_len * math.cos(angle)
        y_end = y_start + needle_len * math.sin(angle)

        nearest_line = (y_start // spacing + 1) * spacing
        color = 'blue'

        if y_end >= nearest_line:
            success_vector.append(1)
        else:
            color = 'red'
            success_vector.append(0)

        if plot:
            axis.plot([x_start, x_end], [y_start, y_end], color=color)

    return success_vector


# Figure and subplot grid
fig = plt.figure(figsize=(14, 14), facecolor='white')
fig.suptitle('Estimating the value of π using Buffon\'s needle problem and a Monte Carlo method\n', fontsize=18,
             fontweight='bold')
gs = gridspec.GridSpec(2, 2, figure=fig)

# Needles
ax0 = fig.add_subplot(gs[0, 0])
plot_grid(ax0, SPACE)
v = buffon_needle_problem(1000, NED_LEN, SPACE, True, ax0)

ax0.set_xlabel('X', fontsize=14)
ax0.set_ylabel('Y', fontsize=14)
ax0.set_title('Randomized Needles\n'
              'blue - crosses a line; red - otherwise', fontsize=16)

# Cumulative Estimation for N=1000
ax1 = fig.add_subplot(gs[0, 1])
v_1000_est = []
for i in range(1, 1000):
    v_1000_est.append(estimate_pi(v[:i], NED_LEN, SPACE))

ax1.plot(v_1000_est)
ax1.set_ylim([1.5, 5])
ax1.set_xlim([0, 1000])
ax1.axhline(y=math.pi, color='r')
ax1.text(1000, math.pi, f'π ≈ {math.pi:.4f}', va='bottom', ha='right', color='r')
ax1.set_xlabel('N', fontsize=14)
ax1.set_ylabel('π estimation', fontsize=14)
ax1.set_title(f'Cumulative Estimation for N={N}', fontsize=16)

# Boxplots
ax2 = fig.add_subplot(gs[1, :])
v_N = np.arange(100, 100000, 100)
estimations = []
for i in v_N:
    ve = buffon_needle_problem(i, NED_LEN, SPACE)
    prob1 = np.sum(ve) / i
    estimations.append(2 * NED_LEN / (SPACE * prob1))
res = pd.DataFrame({"N": v_N, "Estimation": estimations})
res["Group"] = v_N // 10000
grouped_data = res.groupby("Group")["Estimation"].apply(list)

group_labels = ['<1' if label == 0 else label for label in grouped_data.index]

ax2.set_title('Grouped Boxplots of Estimations of π', fontsize=16)
ax2.set_xlabel('N × 10⁴', fontsize=14)
ax2.set_ylabel('Estimation of π', fontsize=14)
ax2.boxplot(grouped_data.values, labels=group_labels, showmeans=True)
ax2.axhline(y=math.pi, color='r', linestyle='--', alpha=0.6)
ax2.text(10.45, math.pi, 'π', va='bottom', ha='right', color='r')

plt.tight_layout()
plt.show()
