for num in range(100, 1000, 1):
    bak = num // 100
    sip = (num - (bak * 100)) // 10
    ill = num - (bak * 100) - (sip * 10)

    if bak * 100 + sip * 10 + ill == bak**3 + sip**3 + ill**3:
        print(f'{num}은 암스트롱 수입니다.')

