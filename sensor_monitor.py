import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import os


################################################## generate data
def generate_readings(minimum_value, maximum_value, number_of_samples):
    random.seed(353)
    readings = [random.randint(minimum_value, maximum_value) for _ in range(number_of_samples)]
    return readings


################################################## statistics
def calculate_statistics(readings):
    data = np.array(readings)
    return {
        "count": len(data),
        "mean": np.mean(data),
        "minimum": np.min(data),
        "maximum": np.max(data),
        "std": np.std(data),
    }


def find_outliers(readings, threshold):
    data = np.array(readings)
    return data[data > threshold]


################################################## visualize data
def plot_readings(readings, threshold, sensor_type):
    sample_numbers = list(range(1, len(readings) + 1))

    plt.figure()
    plt.plot(sample_numbers, readings, marker="o", label="Sensor reading")
    plt.axhline(y=threshold, color="red", linestyle="--", label="Alert threshold")
    plt.title(f"{sensor_type} readings per sample")
    plt.xlabel("Sample number")
    plt.ylabel(f"{sensor_type} reading")
    plt.grid(True)
    plt.legend()
    plt.xticks(sample_numbers)


def plot_histogram(readings, sensor_type):
    plt.figure()
    plt.hist(readings, bins=10, edgecolor="black")
    plt.title(f"Distribution of {sensor_type} readings")
    plt.xlabel(f"{sensor_type} reading")
    plt.ylabel("Number of readings")
    plt.grid(True)
##################################################


################################################## save and load data
def save_readings(readings, filename="sensor_readings.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sample_number", "sensor_reading"])
        for sample_number, reading in enumerate(readings, start=1):
            writer.writerow([sample_number, reading])
    print(f"Readings saved to {os.path.abspath(filename)}")


def load_readings(filename="sensor_readings.csv"):
    readings = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            readings.append(int(row[1]))
    return readings
##################################################


################################################## user can't fill in a letter when a number is asked, number can't be zero or negative
def ask_number(question, minimum=None):
    while True:
        try:
            value = int(input(question))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"The value must be at least {minimum}.")
            continue
        return value


################################################## main program
def main():
    choice = input("Generate new readings or load from CSV file? (generate/load): ").strip().lower()

    sensor_type = input("sensor type: ")
    alert_threshold = ask_number("alert threshold: ")

    if choice == "load":
        try:
            readings = load_readings()
        except FileNotFoundError:
            print("No sensor_readings.csv found. Generate readings first.")
            return
    else:
        while True:
            minimum_value = ask_number("minimum value: ")
            maximum_value = ask_number("maximum value: ")
            if minimum_value < maximum_value:
                break
            print("The minimum value must be smaller than the maximum value.")
        number_of_samples = ask_number("number of samples: ", minimum=1)
        readings = generate_readings(minimum_value, maximum_value, number_of_samples)
        save_readings(readings)

    print(readings)

    stats = calculate_statistics(readings)
    outliers = find_outliers(readings, alert_threshold)
    print(f"Number of readings: {stats['count']}")
    print(f"Mean: {stats['mean']}")
    print(f"Minimum: {stats['minimum']}")
    print(f"Maximum: {stats['maximum']}")
    print(f"Standard deviation: {stats['std']}")
    print(f"Number of readings above threshold: {len(outliers)}")
    print(f"Readings above threshold: {outliers}")

    plot_readings(readings, alert_threshold, sensor_type)
    plot_histogram(readings, sensor_type)
    plt.show()


if __name__ == "__main__":
    main()
##################################################
