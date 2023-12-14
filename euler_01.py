if __name__ == '__main__':
    limit = 1000
    natural_numbers = range(limit)
    multiples_of_5_or_3 = [x for x in natural_numbers if x % 3 == 0 or x % 5 == 0]
    result = sum(multiples_of_5_or_3)
    print(result)