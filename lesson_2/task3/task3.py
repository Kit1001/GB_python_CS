import yaml

original_dict = {
    "items": ["computer", "printer", "mouse", "keyboard"],
    "items_count": 4,
    "items_price": {
        "computer": "400$",
        "printer": "150$",
        "mouse": "20$",
        "keyboard": "10$"
    }
}

with open('file.yaml', 'w+') as f:
    f.write(yaml.dump(original_dict, default_flow_style=False, allow_unicode=True))
    f.seek(0)
    result_dict = yaml.load(f.read(), Loader=yaml.Loader)

print(result_dict == original_dict)
