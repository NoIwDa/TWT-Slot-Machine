import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_to_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

# Tutaj. szykowanie zawartosci wystwitalenj przez columns

    colums = []
    for col in range(cols):
        colums = []
        for row in range(rows):
            value = random. choice(all_symbols)

def deposit():
    while True:
        amount = input("Ile chcesz wplacic? \n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Musisz wplacic wiecej niz 0.")
        else:
            print("Podana amount nie jest poprawna.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Ile wierszy chcesz obstawic? (1 -" + str(MAX_LINES) + ")? \n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Musisz wskazac wiecej niz 0.")
        else:
            print("Podaj poprawny numer.")

    return lines

def get_bet():
    while True:
        amount = input("Ile chcesz obstawić \n")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Kwota musi byc pomiedzy {MIN_BET} a {MAX_BET}. ")
        else:
            print("Podana kwota nie jest poprawna.")

    return amount


def main():
    balance= deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Nie masz wystarczajaco srodkow aby tak obstawiac. Twoj bilans to {balance}")

        else:
            break
    print(f"Obstawiasz {bet} na {lines} kolumny. Lacznie onstawiasz {total_bet}. ")

    print(balance, lines)
main()