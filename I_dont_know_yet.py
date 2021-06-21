def get_integer_input(message, error, low, high):
    valid = False
    while not valid:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
        except ValueError:
            print(error)
coffes = get_integer_input('please enetr how amny coffes you had today ', 
                            'plz enter a whole number abuve 0 ',
                            0, 
                            100)
print(f'youve had {coffes} coffes today')