romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def get_arabic(r_num):
    arabic_num = 0
    prev_r_num = None
    for r in r_num:
        if not prev_r_num:
            arabic_num += romans[r]
        else:
            if romans[r] <= romans[prev_r_num]:
                arabic_num += romans[r]
            else:
                arabic_num += romans[r]
                arabic_num = arabic_num - 2 * romans[prev_r_num]
        prev_r_num = r
    return arabic_num


calc = get_arabic('XL')
print(calc)
