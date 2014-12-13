import math


def average(numbers):
    summ = sum(numbers)
    summ = float(summ)
    results = summ / len(numbers)
    return results


print average([2, 5, 8])


def median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 != 0:
        result = numbers[len(numbers) / 2]
    elif len(numbers) % 2 == 0:
        result = average([numbers[len(numbers) / 2], numbers[len(numbers) / 2 - 1]])
    return result


print median([1, 5, 3, 4])


def mode(numbers):
    dic = {}
    for num in numbers:
        if str(num) not in dic.keys():
            dic.update({str(num): 1})
        elif str(num) in dic.keys():
            dic[str(num)] += 1
    prev = ['', 0]
    for key in dic.keys():
        if dic[key] > prev[1]:
            prev[1] = dic[key]
            prev[0] = key
    return prev[0]


print mode([1, 2, 1, 1, 1, 1, 3, 3, 3, 3])


def rang(numbers):
    numbers = sorted(numbers)
    results = numbers[len(numbers) - 1] - numbers[0]
    return results


print rang([1, 5, 3])
