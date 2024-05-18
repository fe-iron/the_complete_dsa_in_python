my_dict = {'a': 5, 'b': 9, 'c': 2}
def max_value_key(my_dict):
    # TODO
    max_val_ind = -1
    max_val = float('-inf')
    for key, val in my_dict.items():
        if val >= max_val:
            max_val = val
            max_val_ind = key
    print(max_val_ind)
    # max(my_dict, key=my_dict.get)


def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}


