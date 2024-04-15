def calculate_sewing_cost(fabric_cost, fabric_needed):
    # Расчет стоимости пошива
    # fabric_cost - стоимость ткани за метр
    # fabric_needed - расход ткани на изделие

    # добавляем стоимость фурнитуры (нитки, пуговицы и т.д.)
    additional_materials_cost = 20

    # добавляем стоимость работы
    labor_cost_per_meter = 30
    labor_cost = labor_cost_per_meter * fabric_needed

    sewing_cost = fabric_cost * fabric_needed + additional_materials_cost + labor_cost
    return sewing_cos