"""1"""
def distribute(n, seq):
    """delar upp listor"""
    new_list = []
    step = 0
    for _ in range(n):
        new_list.append([])
    for element in seq:
        new_list[step].append(element)
        step = 0 if step == n-1 else step + 1
    return new_list


if __name__ == '__main__':
    print(distribute(3, [1,2,3,4,5,6]))
