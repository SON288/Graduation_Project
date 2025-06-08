import os
from data_load import load_csv  

def main():
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diem_thi_thpt_2022.csv")
    headers, data = load_csv(filepath)
    if data:
        print("Header:", headers)
        print(data[:5])
    else:
        print("Khong co du lieu.")

if __name__ == "__main__":
    main()

