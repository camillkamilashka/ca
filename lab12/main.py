import tkinter as tk
from appliances import Iron, TV, WashingMachine
from report import save_to_doc, save_to_xlsx

def calculate():
    iron_power = float(iron_power_entry.get())
    tv_power = float(tv_power_entry.get())
    washing_machine_power = float(washing_machine_power_entry.get())
    hours = float(hours_entry.get())
    rate = float(rate_entry.get())

    iron = Iron(iron_power)
    tv = TV(tv_power)
    washing_machine = WashingMachine(washing_machine_power)

    iron_energy_consumption = iron.calculate_energy_consumption(hours)
    tv_energy_consumption = tv.calculate_energy_consumption(hours)
    washing_machine_energy_consumption = washing_machine.calculate_energy_consumption(hours)

    iron_cost = iron.calculate_cost(hours, rate)
    tv_cost = tv.calculate_cost(hours, rate)
    washing_machine_cost = washing_machine.calculate_cost(hours, rate)

    result_label.config(text=f"Iron energy consumption: {iron_energy_consumption} kWh\n"
                             f"TV energy consumption: {tv_energy_consumption} kWh\n"
                             f"Washing machine energy consumption: {washing_machine_energy_consumption} kWh\n\n"
                             f"Iron cost: {iron_cost} $ \n"
                             f"TV cost: {tv_cost} $ \n"
                             f"Washing machine cost: {washing_machine_cost} $ ")

def save_report():
    hours = float(hours_entry.get())
    rate = float(rate_entry.get())

    iron = Iron(float(iron_power_entry.get()))
    tv = TV(float(tv_power_entry.get()))
    washing_machine = WashingMachine(float(washing_machine_power_entry.get()))

    iron_cost = iron.calculate_cost(hours, rate)
    tv_cost = tv.calculate_cost(hours, rate)
    washing_machine_cost = washing_machine.calculate_cost(hours, rate)

    save_report_btn = tk.Button(window, text="Save Report", command=save_report)
    save_report_btn.grid(row=7, column=1) 
    