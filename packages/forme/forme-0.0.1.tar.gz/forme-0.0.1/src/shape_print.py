import numpy as np

def shape_print(first_input, second_input):
    first_shape = []
    second_shape = []
    
    try:
        first_input = np.array(first_input)
        second_input = np.array(second_input)

        for idx in range(len(first_input)):
            first_shape.append(first_input.shape)

        for idx in range(len(second_input)):
            second_shape.append(second_input.shape)

    except IndexError:
        print("U over it. too much.")

    except TypeError:
        print("U picked a wrong type foo.")