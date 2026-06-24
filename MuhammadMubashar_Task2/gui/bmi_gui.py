import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt

def save_record(record):
    try:
        with open("data/bmi_records.json", "r") as file:
            records = json.load(file)

        records.append(record)

        with open("data/bmi_records.json", "w") as file:
            json.dump(records, file, indent=4)

    except Exception as error:
        print(f"Error saving record: {error}")

def view_history():
    try:
        with open("data/bmi_records.json", "r") as file:
            records = json.load(file)

        if not records:
            messagebox.showinfo(
                "History",
                "No BMI records found."
            )
            return

        history_text = ""

        for record in records:
            history_text += (
                f"Name: {record['name']}\n"
                f"BMI: {record['bmi']}\n"
                f"Category: {record['category']}\n"
                f"Date: {record['timestamp']}\n"
                f"{'-' * 30}\n"
            )

        messagebox.showinfo(
            "BMI History",
            history_text
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not load history.\n{error}"
        )

def show_statistics():
    try:
        with open("data/bmi_records.json", "r") as file:
            records = json.load(file)

        if not records:
            messagebox.showinfo(
                "Statistics",
                "No BMI records available."
            )
            return

        bmi_values = [record["bmi"] for record in records]

        total_records = len(bmi_values)
        average_bmi = sum(bmi_values) / total_records
        highest_bmi = max(bmi_values)
        lowest_bmi = min(bmi_values)

        stats_text = (
            f"Total Records: {total_records}\n\n"
            f"Average BMI: {average_bmi:.2f}\n"
            f"Highest BMI: {highest_bmi:.2f}\n"
            f"Lowest BMI: {lowest_bmi:.2f}"
        )

        messagebox.showinfo(
            "BMI Statistics",
            stats_text
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not calculate statistics.\n{error}"
        )

def show_bmi_graph():
    try:
        with open("data/bmi_records.json", "r") as file:
            records = json.load(file)

        if not records:
            messagebox.showinfo(
                "Graph",
                "No BMI records available."
            )
            return

        dates = []
        bmi_values = []

        for record in records:
            dates.append(
                datetime.strptime(
                    record["timestamp"],
                    "%Y-%m-%d %H:%M:%S"
                )
            )
            bmi_values.append(record["bmi"])

        plt.figure(figsize=(8, 5))
        plt.plot(dates, bmi_values, marker="o")

        plt.title("BMI Trend Analysis")
        plt.xlabel("Date")
        plt.ylabel("BMI")

        plt.grid(True)
        plt.tight_layout()

        plt.show()

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not generate graph.\n{error}"
        )

def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            result_label.config(text="Please enter your name.")
            return

        if weight <= 0 or height <= 0:
            result_label.config(
                text="Weight and height must be positive numbers."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        record = {
            "name": name,
            "weight": weight,
            "height": height,
            "bmi": round(bmi, 2),
            "category": category,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        save_record(record)

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        result_label.config(
            text="Please enter valid numeric values."
        )


# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x450")

# Title
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# Name
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Weight
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(root, width=30)
weight_entry.pack(pady=5)

# Height
height_label = tk.Label(root, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(root, width=30)
height_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack(pady=15)

# History Button
history_button = tk.Button(
    root,
    text="View History",
    command=view_history
)
history_button.pack(pady=5)

# Statistics Button
statistics_button = tk.Button(
    root,
    text="Show Statistics",
    command=show_statistics
)
statistics_button.pack(pady=5)

# Graph Button
graph_button = tk.Button(
    root,
    text="Show BMI Graph",
    command=show_bmi_graph
)
graph_button.pack(pady=5)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)

root.mainloop()