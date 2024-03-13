# Estimating the value of π using Buffon's needle problem and Monte Carlo methods

## Description:
This repository contains Python code implementing simulations and visualizations related to Buffon's needle problem for estimating the value of π using Monte Carlo methods. Buffon's needle problem is a classic problem in geometric probability theory, where one estimates the value of π by dropping needles onto a grid and observing how many crosses a line.

## Contents:

buffon_needle.py: Python script containing the main simulation functions and visualization code.
results.png: Image file containing plots generated from the simulations.

## Results:
The results.png file contains three plots:

1. Randomized Needles Plot: This plot shows randomly generated needles dropped onto a grid. Blue lines indicate needles that cross a grid line, while red lines indicate those that do not.

2. Cumulative Estimation Plot: This plot displays the cumulative estimation of π as the number of simulated needles increases. The red dashed line represents the actual value of π.

3. Grouped Boxplots of Estimations: These boxplots illustrate the distribution of π estimations grouped by the number of simulated needles. Each boxplot represents estimations obtained from a certain range of simulated needle counts.

## References:

[Wikipedia - Buffon's Needle](https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)

[Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
