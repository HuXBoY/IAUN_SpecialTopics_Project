import msvcrt
from colorama import Fore, Back, Style
import accounts


def main():
    accounts.init_accounts()
    while 1:
        action = input(
            "\n" * 25 +
            f"{Fore.MAGENTA}==={Fore.RESET} Banking operations menu {Fore.MAGENTA}==={Fore.RESET}\n"
            "1. Show balance of all accounts\n"
            "2. Deposit into account\n"
            "3. Withdrawal from account\n"
            "4. Show accounts with higher than average balance\n"
            "5. Exit\n"
        )

        if action == "1":
            print(
                "\n" * 25 + Fore.YELLOW +
                "Showing balance of all accounts . . .\n" + Style.RESET_ALL)
            act1()
            act_end()

        elif action == "2":
            print(
                "\n" * 25 + Fore.YELLOW +
                "Depositing into account . . .\n" + Style.RESET_ALL)
            act2()
            act_end()

        elif action == "3":
            print(
                "\n" * 25 + Fore.YELLOW +
                "Withdrawing from account . . .\n" + Style.RESET_ALL)
            act3()
            act_end()

        elif action == "4":
            print(
                "\n" * 25 + Fore.YELLOW +
                f"Showing balance of all accounts highter than average : {accounts.get_avg_balance()} . . .\n" + Style.RESET_ALL)
            act4()
            act_end()

        elif action == "5":
            print(f"{Fore.BLACK}{Back.LIGHTRED_EX}Exiting . . .{Style.RESET_ALL}")
            break

        else:
            print("Request not accepted. Please try again!")


def act1():
    for i in range(len(accounts.account_owner)):
        print(
            Fore.MAGENTA + accounts.account_owner[i],
            "->" + Fore.RESET, accounts.account_balance[i])


def act2():
    print("Which account to deposit into ?\n")
    for i in range(len(accounts.account_owner)):
        print(i+1, "->", accounts.account_owner[i])
    depo_to_acc = int(input("-> "))
    for i in range(len(accounts.account_owner)):
        if depo_to_acc == i+1:
            amount = int(input("How much to deposit? "))
            accounts.account_balance[i] += amount
            print(
                "\n" * 25 +
                f"Deposited {amount}\n"
                f"Your current balance is: {accounts.account_balance[i]}")


def act3():
    print("Which account to withdraw from ?\n")
    for i in range(len(accounts.account_owner)):
        print(i+1, "->", accounts.account_owner[i])
    depo_to_acc = int(input("-> "))
    for i in range(len(accounts.account_owner)):
        if depo_to_acc == i+1:
            amount = int(input("How much to deposit? "))
            if amount > accounts.account_balance[i]:
                print(f"{Fore.BLACK}{Back.RED}Not enough balance!{Style.RESET_ALL}")
            else:
                accounts.account_balance[i] -= amount
                print(
                    "\n" * 25 +
                    f"Withdrew {amount}\n"
                    f"Your current balance is: {accounts.account_balance[i]}")


def act4():
    avg = accounts.get_avg_balance()
    for i in range(len(accounts.account_balance)):
        if accounts.account_balance[i] >= avg:
            print(
                f"{Fore.MAGENTA} {accounts.account_owner[i]} -> {Style.RESET_ALL} {accounts.account_balance[i]}")


def act_end():
    print("\n\n\nPress any key to continue")
    msvcrt.getch()


main()
