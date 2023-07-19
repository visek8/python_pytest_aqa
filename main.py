def area_calculator(s_one, s_two):
    if type(s_one) == int and type(s_two) == int:
        year = 1
        while s_one > 0.1 * s_two:
            s_one *= 2
            s_two *= 3
            year += 1
        return s_one, s_two, year
    else:
        return "Error"
