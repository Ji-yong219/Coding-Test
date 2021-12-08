def main():
    coin_type = [500, 100, 50, 10]

    price = 1260
    count = 0

    for coin in coin_type:
        count += price // coin
        price %= coin

    return count
