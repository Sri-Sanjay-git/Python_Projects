Physics and Electrical Engineering Calculator


This repository contains a set of Python functions that can be used to calculate various physics and electrical engineering formulas, 
including those for frequency conversion, metric unit conversions, speed, time, distance, escape velocity, gravitational force, and more. 
It also includes functions for calculating electrical components in series and parallel circuits, Ohm's law, power law, and CMYK to RGB color conversion.

Features:

Frequency Converter:
Converts frequencies between different units (Hz, kHz, MHz, GHz).

Metric Converter:
Converts between various metric units (e.g., pico, nano, kilo, mega, etc.)

Speed, Distance, and Time Calculations:
Calculates speed, time, and distance using basic formulas.

Computes escape velocity for different planets in the solar system.
Physics Calculations:

Newton's second law (F = ma).
Gravitational force using the formula 
𝐹=𝐺⋅𝑚1⋅𝑚2
F= r2
G⋅m1⋅m2

Tension in a rope or cable.

Mass-energy equivalence using Einstein’s equation 
E=mc2

CMYK to RGB Conversion:
Converts CMYK values to RGB values for color applications.

Electrical Circuit Calculations:
Calculates total resistance, inductance, and capacitance for both series and parallel circuits.
Ohm’s law calculations (voltage, current, resistance).
Power law calculations (voltage, current, power).

Wheatstone Bridge:
Calculates the unknown resistance using the Wheatstone bridge formula.

Functions:
freq_converter(value, from_frq, to_freq): Converts frequency from one unit to another.
metric_converter(value, from_unit, to_unit): Converts between different metric units.
speed(dis, tim): Calculates speed from distance and time.
time(dis, spd): Calculates time from distance and speed.
distance(sped, time): Calculates distance from speed and time.
escape_velocity(planet): Returns the escape velocity of a planet.
cal_escape(G, m, r): Calculates escape velocity using gravitational constant, planet mass, and radius.
Newton2nd(m, a): Calculates force from mass and acceleration.
gravitational_force(G, m1, m2, r): Calculates gravitational force between two masses.
tension(m, g, a): Calculates tension in a rope.
Einstein_Mass_Energy(m): Calculates energy from mass using Einstein's equation.
cmyk_rgb(c, m, y, k): Converts CMYK values to RGB.
series_resistor(*args): Calculates total resistance for resistors in series.
parllel_resisror(*args): Calculates total resistance for resistors in parallel.
series_inductor(*args): Calculates total inductance for inductors in series.
parallel_inductor(*args): Calculates total inductance for inductors in parallel.
series_capacitor(*args): Calculates total capacitance for capacitors in series.
parallel_capacitor(*args): Calculates total capacitance for capacitors in parallel.
wheatstone_bal(R1, R2, R3): Calculates the unknown resistance using the Wheatstone bridge.
ohmslaw(type, V, I, R): Calculates voltage, current, or resistance using Ohm’s law.
powerlaw(type, V, I, P): Calculates power, voltage, or current using the power law.


Usage Examples:
Frequency Conversion:
freq_converter(10, 'kHz', 'MHz')  # Output: 0.01

Ohm’s Law:
ohmslaw("Current", V=10, R=5)  # Output: 2.0 A

Gravitational Force:
gravitational_force(6.67430 * 10**-11, 5.972 * 10**24, 7.348 * 10**22, 384400000)  # Output: 1.9782958926504e+20 N

CMYK to RGB Conversion:
cmyk_rgb(0.5, 0.5, 0.5, 0.5)  # Output: (127, 127, 127)
