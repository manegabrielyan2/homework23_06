#numbers in english
def int_str(n : int):
    if n is None:
        print()
        return
    
    units = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }

    tens_1 = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }

    tens = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'fourty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninty',
    }
    
    str_num = str(n)
    num_size = len(str_num)

    if num_size == 1:
        print(units[str_num])
    if num_size == 2:
        if str_num.startswith('1'):
            print(tens_1[str_num])
        else:
            print(f'{tens[str_num[0]]}-{units[str_num[1]]}')
    if num_size == 3:
        print(f'{units[str_num[0]]} hundreed', end=' ')
        int_str(int(str_num[1:]))
    if num_size == 4:
        print('one thousand', end=' ')
        int_str(int(str_num[1:]))

int_str(0)

