import toga
from appliances.iron import Iron

def calculate_iron_cost(widget):
    power = float(input_power.value)
    period = float(input_period.value)
    rate = float(input_rate.value)

    iron = Iron(power, period)
    energy_consumption = iron.calculate_energy_consumption()
    cost = iron.calculate_cost(rate)

    label.value = f"Energy consumption: {energy_consumption} kWh\nCost: {cost} $"

def save_to_file(widget):
    # Save results to .doc or .xls file using python-docx or openpyxl
    pass

def build(app):
    box = toga.Box()

    global input_power
    input_power = toga.TextInput(placeholder='Power in W')
    box.add(input_power)

    global input_period
    input_period = toga.TextInput(placeholder='Period in hours')
    box.add(input_period)

    global input_rate
    input_rate = toga.TextInput(placeholder='Rate in $ per kWh')
    box.add(input_rate)

    button = toga.Button('Calculate', on_press=calculate_iron_cost)
    box.add(button)

    global label
    label = toga.Label('Results:')
    box.add(label)

    save_button = toga.Button('Save to File', on_press=save_to_file)
    box.add(save_button)

    return box

def main():
    app = toga.App('Appliances Calculator', 'com.example.appliances_calculator', startup=build)
    app.main_loop()

if __name__ == '__main__':
    main()
 
 
