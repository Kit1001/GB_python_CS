import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {"item": item, "quantity": quantity, "price": price, "buyer": buyer, "date": date}
    with open('orders.json', 'r+b') as f:
        f.seek(-3, 2)
        comma = '' if f.read().decode('utf-8')[0] == '[' else ',\n'
        f.seek(-2, 2)
        string_ = f'{comma}{json.dumps(data, indent=4, ensure_ascii=false)}]{"}"}'
        f.write(string_.encode('utf-8'))


write_order_to_json('монитор', "10", "9950", "петров", "12.11.2021")
write_order_to_json('принтер', "3", "4500", "иванов", "02.03.2021")
