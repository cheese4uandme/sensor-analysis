# Sensor Analysis

A Python program that simulates sensor readings, analyzes them with NumPy,
visualizes them with Matplotlib and saves them to a CSV file.

## Installations

    python -m pip install -r requirements.txt

## program to use

    python sensor_monitor.py

The program asks whether to generate new readings or load them from
`sensor_readings.csv`, then asks for the sensor type and alert threshold.
When generating, it also asks for the number of readings and the minimum and maximum value.

## Output

- Statistics in the terminal (count, mean, minimum, maximum, standard deviation, readings above the threshold)
- A line plot with the alert threshold and a histogram
- `sensor_readings.csv` with sample number and sensor reading