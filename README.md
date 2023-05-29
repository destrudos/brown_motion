# Simple Brown motion simulator

## Introduction
Brownian motion, also known as particle theory, is a physical phenomenon that describes the random movement of particles suspended in a fluid (liquid or gas). This motion results from the fast and random collisions of the particles with the molecules of the fluid in which they are immersed. The theory is named after the botanist Robert Brown, who first observed the motion in 1827 while looking at pollen particles floating in water under a microscope.
See [#wiki](https://en.wikipedia.org/wiki/Brownian_motion)
## Unordered
To run this properly you need
1. Python => 3.8
2. Matplotlib
3. numpy

## Characteristics
This script implements only the basic inelastic particle collisions i.e. the simplest approach is to assume that the particles are perfect spheres that bounce off each other at right angles (the angle of incidence equals the angle of reflection). 

## How to use it
Script contains following *env* variables:
1. `x_size` — width of simulation box
2. `y_size` — height of simulation box
3. `speed` — particle speed
4. `radius` — particle radius

After adjustments just run it if you have all necessary library in your python environment:

`$ python brown-main.py`
