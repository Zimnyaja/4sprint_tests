import sys


def find_element(sorted_numbers, element):
    left = 0
    right = len(sorted_numbers)-1
    while left <= right:
        mid = (left + right)//2
        if sorted_numbers[mid] == element:
            a = dublicate_low(sorted_numbers, mid)
            return print(a)
        if sorted_numbers[mid] < element:
            left = mid + 1
        if sorted_numbers[mid] > element:
            right = mid - 1
    return print(new(sorted_numbers, mid, element))


def dublicate_low(sorted_numbers, index):
    if index == 0:
        return index
    small = (sorted_numbers[0:index+1])
    a = len(small)
    m = -1
    while a > 1:
        a -= 1
        if small[m] > small[m-1]:
            break
        elif small[m] == small[m-1]:
            m = m-1
    return index + m + 1


def dublicate_up(sorted_numbers, index):
    small = (sorted_numbers[index:])
    count = 0
    for i in range(len(small)-1):
        if small[i] < small[i+1]:
            break
        elif small[i] == small[i+1]:
            count += 1
    return index+count


def new(current_list, mid, element):
    a = dublicate_low(current_list, mid)
    b = dublicate_up(current_list, mid)
    if element < current_list[a]:
        return a
    elif element > current_list[b]:
        return b + 1
    else:
        return a + 1


def main():
    b = list(map(int, (sys.stdin.readline().strip()).split()))
    a = int(sys.stdin.readline().strip())

    find_element(b, a)


if __name__ == '__main__':
    main()
