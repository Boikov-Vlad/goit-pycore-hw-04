from utils import normalize_salary

def total_salary(path):
    total = 0
    workers = 0
    try:
        with open(path, encoding='utf-8') as file:
            for line_number, line in enumerate(file):
                try:
                    _, salary = line.strip().split(',')
                    total += float(salary)
                    workers += 1
                except ValueError:
                    print(f'Invalid salary "{salary}" on line {line_number}, skipping this line')
                    continue

            average = total / workers if workers > 0 else 0

            return normalize_salary(total), normalize_salary(average)

    except FileNotFoundError:
        print(f'File not found: {path}')
        return 0,0 

    except Exception as e:
        print(f'Error: {e} in {path} file')
        return 0, 0

total, average = total_salary("./salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
