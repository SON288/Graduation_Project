# Dự án Xử Lý & Trực Quan Dữ Liệu Python (OOP)

Viết theo mô hình hướng đối tượng (OOP) bằng Python.
- Thu thập dữ liệu (file CSV thô),
- Tiền xử lý dữ liệu (làm sạch, ép kiểu),
- Lưu dữ liệu đã xử lý,
- Và trực quan hóa dữ liệu một cách dễ dàng.

---

## Cấu trúc thư mục
```
my_project/
├── data/
│   ├── diem_thi_2020_2021/              # Dữ liệu thô (CSV gốc)
│   └── diem_thi_2022
|        diem_thi_2023
|       diem_thi_2024     
├── notebooks/            # Các notebook thử nghiệm trực quan
├── Python Script/                  # Mã nguồn Python (chia theo lớp OOP)
│   ├── data_cleaning_add_column_code_and_year_oop.ipynb
│   ├── data_cleaning_check
│   ├── data_cleaning_concat
|   |---data_cleaning_drop_column
|   |---data_cleaning_merge_table
│   └── data_cleaning_removed_dup
|   └── data_cleaning_read_csv
|   └── final_data
├── main.py               # Tập tin chính chạy pipeline
└── requirements.txt      # Các thư viện cần thiết
```

---