from itertools import permutations


def calculate_f(x, y, z, w):
    impl_x_y = not x or y
    impl_y_w = not y or w
    equivalence = impl_x_y == impl_y_w
    not_z_to_x = z and not x
    return equivalence and not_z_to_x


for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if calculate_f(x, y, z, w):
                    print(x, y, z, w)