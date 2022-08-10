#function to check if a number is narcissistic or not

def narcissistic(value):
    string_num, number = str(value), 0
    for i in string_num:
        number+=int(i)**len(string_num)
    return True if number == value else False
