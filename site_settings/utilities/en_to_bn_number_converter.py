"""site_settings > utilities > en_to_bn_number_converter.py"""
# PYTHON IMPORTS


def en_to_bn_number_converter(values):
    numbers = {
        '0': '০',
        '1': '১',
        '2': '২',
        '3': '৩',
        '4': '৪',
        '5': '৫',
        '6': '৬',
        '7': '৭',
        '8': '৮',
        '9': '৯',
        ',': ',',
        '.': '.'
    }
    bangla_numbers = []
    for en in str(values):
        for key, value in numbers.items():
            if en == key:
                bangla_numbers.append(value)
    actual_value = "".join(str(v) for v in bangla_numbers)
    return actual_value
