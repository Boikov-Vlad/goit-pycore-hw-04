def normalize_salary(value: float):
    return int(value) if value.is_integer() else value
