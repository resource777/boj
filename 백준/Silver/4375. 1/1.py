while True:
    try:
        n = int(input())
    except:
        break
    digit = 1
    num = 0
    while True:
        num = num * 10 + 1
        if num % n == 0:
            print(digit)
            break
        else:
            digit += 1