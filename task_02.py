def get_cats_info(path):
    cats_list = []
    try:
        with open(path, encoding='utf-8') as file:
            for line_number, line in enumerate(file):
                try:
                    cat_id, name, age = line.strip().split(',')
                except ValueError:
                    print(f"Invalid line format on line {line_number}: {line}, skipping")
                    continue

                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": age,
                })
    except FileNotFoundError:
        print(f'File not found: {path}')

    except Exception as e:
        print(f'Error: {e} in {path} file')

    return cats_list

cats_info = get_cats_info("./cats.txt")
print(cats_info)
