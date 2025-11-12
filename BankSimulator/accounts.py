import random

account_owner = []
account_balance = []
name_pool = [
    "Ali", "Reza", "Mohammad", "Hossein", "Amir", "Sina", "Ehsan", "Navid", "Arash", "Kourosh",
    "Farid", "Saeed", "Behnam", "Hamed", "Milad", "Peyman", "Kian", "Nima", "Soroush", "Mehdi",
    "Sara", "Maryam", "Narges", "Parisa", "Elham", "Nazanin", "Mahsa", "Samira", "Roya", "Leila",
    "Shirin", "Mina", "Fatemeh", "Yasmin", "Taraneh", "Arezoo", "Sepideh", "Sanaz", "Pegah", "Niloofar",
    "Shabnam", "Hanieh", "Zahra", "Bahareh", "Elaheh", "Mahdokht", "Fereshteh", "Sadaf", "Negar", "Katayoun"]


def init_accounts():
    choise = input(
        "\n" * 25 +
        "=== Initialize accounts ===\n1.RANDOM: randomly generate n number of accounts\n2.CUSTOM: Add n number of account with custom names and initial values\n").lower()
    if choise == "1" or choise == "set":
        n = int(input("Number of random accounts: "))
        for i in range(n):
            account_owner.append(random.choice(name_pool))
            account_balance.append(random.randint(10, 10000) * 100)
        print(f"Made {n} number of random accounts.")

    elif choise == "2" or choise == "custom":
        acc_amount = int(input(
            "\n" * 25 +
            "How many accounts do you want to have? "))
        for i in range(acc_amount):
            name = input(f"What to name the account  #{i+1} : ")
            account_owner.append(name)
            initial_value = int(
                input(f"Enter Initial value for account #{i+1}: "))
            account_balance.append(initial_value)


def get_avg_balance():
    sum = 0
    for i in account_balance:
        sum += i
    avg = sum / len(account_balance)
    return avg
