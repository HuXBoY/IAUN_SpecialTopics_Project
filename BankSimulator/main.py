import msvcrt
from colorama import Fore, Back, Style
import accounts


def main():
    while 1:
        action = input(
            "\n" * 15 +
            f"{Fore.MAGENTA}==={Fore.RESET} Banking operations menu {Fore.MAGENTA}==={Fore.RESET}\n"
            "1. Show balance of all accounts\n"
            "2. Deposit into account\n"
            "3. Withdrawal from account\n"
            "4. Show accounts with higher than average balance\n"
            "5. Exit\n"
        )

        if action == "1":
            print(
                "\n" * 15 + Fore.YELLOW +
                "Showing balance of all accounts . . .\n" + Style.RESET_ALL)
            act1()
            act_end()

        elif action == "2":
            act2()
            print("Depositing into account . . .")
            act_end()

        elif action == "3":
            act3()
            act_end()

        elif action == "4":
            act4()
            act_end()

        elif action == "5":
            print(f"{Fore.BLACK}{Back.LIGHTRED_EX}Exiting . . .{Style.RESET_ALL}")
            break

        else:
            print("Request not accepted. Please try again!")


def act1():
    for i in accounts.account_balance:
        print(Fore.MAGENTA + "->" + Fore.RESET, i)


def act2():
    pass


def act3():
    pass


def act4():
    pass


def act_end():
    print("\n\n\nPress any key to continue")
    msvcrt.getch()


main()
