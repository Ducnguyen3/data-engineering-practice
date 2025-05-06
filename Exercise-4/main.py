import os
import json
import csv
import glob
from pathlib import Path


def flatten_json(json_data, parent_key='', sep='_'):
    """
    Làm phẳng cấu trúc JSON lồng nhau thành một dictionary phẳng
    """
    items = {}
    for k, v in json_data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        elif isinstance(v, list):
            if v and isinstance(v[0], dict):
                for i, item in enumerate(v):
                    items.update(flatten_json(item, f"{new_key}_{i}", sep=sep))
            else:
                items[new_key] = v
        else:
            items[new_key] = v
    return items


def process_json_file(json_file_path):
    """
    Xử lý một file JSON và chuyển đổi thành CSV
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    flattened_data = flatten_json(json_data)
    
    csv_file_path = str(json_file_path).replace('.json', '.csv')
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=flattened_data.keys())
        writer.writeheader()
        writer.writerow(flattened_data)
    
    print(f"Đã chuyển đổi {json_file_path} thành {csv_file_path}")


def main():
    json_files = glob.glob('data/**/*.json', recursive=True)
    
    for json_file in json_files:
        try:
            process_json_file(json_file)
        except Exception as e:
            print(f"Lỗi khi xử lý file {json_file}: {str(e)}")


if __name__ == "__main__":
    main()
