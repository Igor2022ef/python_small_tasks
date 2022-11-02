def is_prime(num:int):
    res = list(map(int, str(num)))
    if len(res) == 1:
        if 1 < num < 4 or num == 5 or num == 7:
            return "Простое"
        else:
            return "Не простое"
    else:
        if (res[len(res)-1]%2 == 0) or res[len(res)-1] == 0 or res[len(res)-1] == 5:
            return "Не простое"
        else:
            p = 3
            from math import sqrt
            while p < sqrt(num)+1:
                if num%p != 0:
                    p += 1
                else:
                    return "Не простое"
                    break
            return "Простое"


if __name__ == '__main__':
    print(is_prime(73))
