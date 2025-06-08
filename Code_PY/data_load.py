import csv

def load_csv(filepath):
    data = []
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                data.append(row)
        return headers, data
    except FileNotFoundError:
        print(f"Khong tim thay file: {filepath}")
        return None, None
    except Exception as e:
        print(f"Loi khi doc file: {e}")
        return None, None
