from functools import reduce


def compute_sum_positive_odd_numbers():
    get_num = list(map(int, input("Enter number of elements:").split()))
    less_than_zero = list(filter(lambda x: (x % 2 == 1 and x > 0), get_num))
    product = reduce((lambda x, y: x + y), less_than_zero)
    return print(product)


if __name__ == '__main__':
    compute_sum_positive_odd_numbers()
