import sys


def main():
    a = int(sys.stdin.readline().strip())
    b = sys.stdin.readline().strip()
    c = b.split()
    number = 0
    for i in range(len(c)):
        while a > 1:
            a -= 1
            if int(c[i]) < int(c[i+1]):
                break
            elif c[i] == c[i+1]:
                c.pop(i+1)
                number += 1

    print(' '.join(c) + (' '+'_')*number)

    # c = list(map(int, b.split()))
    # count = 0
    # for i, num in enumerate(c):
    #     count +=1
    #     if isinstance(num, str):
    #         break
    #     while count < a  and c[i] == c[i+1]:
    #         c.pop(i+1)
    #         c.append('_')
    #         count +=1
    # c = list(map(str, c))
    # print(' '.join(c))

    # a = int(sys.stdin.readline().strip())
    # b = sys.stdin.readline().strip()
    # c = b.split()
    # count = 0
    # for i, num in enumerate(c):
    #     count += 1
    #     if num == '_':
    #         break
    #     while count < a and c[i] == c[i+1]:
    #         c.pop(i+1)
    #         c.append('_')
    #         count += 1
    # print(' '.join(c))

    # c = list(map(int, b.split()))
    # d = []
    # e = []
    # for num in c:
    #     if num not in d:
    #         d.append(num)
    #     else:
    #         e.append('_')
    # d = list(map(str, d))
    # print(' '.join(d + e))


if __name__ == '__main__':
    main()
