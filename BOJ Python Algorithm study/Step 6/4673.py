def d():
    creator_numbers = []
    all_numbers = []

    for i in range(10001):
        all_numbers.append(i)

    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    creator_numbers.append(1001 * a + 101 * b + 11 * c + 2 * d)

    creator_numbers = set(creator_numbers)
    all_numbers = set(all_numbers)

    result = list(all_numbers - creator_numbers)
    result.sort()
    for k in result:
         print(k)

d()
