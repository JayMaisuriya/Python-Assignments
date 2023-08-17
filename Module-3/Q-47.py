# Write a Python program to combine values in python list of dictionaries.

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]
result_dict = {}
for entry in data:
    item = entry['item']
    amount = entry['amount']
    result_dict[item] = result_dict.get(item, 0) + amount

print("Combined dictionary:", result_dict)

