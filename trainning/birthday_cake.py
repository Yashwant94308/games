lists = []

number_candle = int(input("enter total number of candle : "))
if 1 <= number_candle <= 10 ** 5:

    for i in range(number_candle):
        n = int(input("enter height of " + str(i + 1) + " candle : "))
        if 1 <= n <= 10**7:
            lists.append(n)
        else:
            print("you are out of range, eg: 1 <= height <= 10**7")
            break
    if len(lists) == number_candle:
        m = max(lists)
        j = 0
        for li in lists:
            if li == m:
                j += 1
        print("Total candle can be blown out = ", j)
else:
    print("you are out of range, eg: 1 <= number of candle <= 10 ** 5")
