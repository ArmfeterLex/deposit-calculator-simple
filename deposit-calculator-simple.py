def calc_s(init_deposit):
    int_rate = 0.04
    balance1 = round(init_deposit * (1 + int_rate), 2)
    balance2 = round(balance1 * (1 + int_rate), 2)
    balance3 = round(balance2 * (1 + int_rate), 2)
    print(f"1 год: {balance1}")
    print(f"2 год: {balance2}")
    print(f"3 год: {balance3}")

init_deposit = float(input("Первоначальный депозит: "))
calc_s(init_deposit)