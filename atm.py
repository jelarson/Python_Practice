"""
Create a Virtual Wallet in Python

- A user should be able to interact with your wallet in the following ways:
  - Choices made in a menu screen
  - Check Balance
  - Withdrawal Cash
  - Deposit Cash
  - Go back to the main menu
  - Exit the Program

Try using OOP principles to build this program. I will be looking at how your control structures ( the flow of your program, function routing, etc ) come together.

- Bonus
  - Attempt to use a Flask API to persist account information.

You have until Friday morning to get this finished. Help each other out, and good luck!

"""


class User:
    def __init__(self, name, check_bal, sav_bal, acct_num, pin_num="1234"):
        self.name = name
        self.check_bal = check_bal
        self.sav_bal = sav_bal
        self.acct_num = acct_num
        self.pin_num = pin_num


jim = User("Jim", 100, 200, '123')
sarah = User("Sarah", 50, 0, '456')
debbie = User("Debbie", 2500, 4000, '789')
balance = 100


def virtual_wallet():
    users = [jim, sarah, debbie]
    locked_user = []
    i = 0
    while i < 2:
        print('What is your account number?\n')
        acct_input = input()
        for user in locked_user:
            if acct_input == user.acct_num:
                print("\nYour account has been locked out")
                # return False
            if acct_input != user.acct_num:
                pass
        for user in users:
            if acct_input == user.acct_num:
                print('\nPin Number?\n')
                pin_input = input()
                if pin_input == user.pin_num:
                    print(f'\nWelcome, {user.name}!\n')
                    while i < 1:
                        print(
                            "Main Menu\n\n1: Check Balance\n2: Deposit\n3: Withdrawl\n4: Transfer Within Your Account\n5: Exit\n")
                        main_menu_input = input()

                        if main_menu_input == "1":
                            print(
                                f'\nYour current Savings balance is ${user.sav_bal}\n')
                            print(
                                f'Your current Checking balance is ${user.check_bal}\n')
                        if main_menu_input == "2":
                            print(
                                "\nWhich account would you like to deposit to?\n1: Saving Account\n2: Checking Account\n")
                            deposit_account_input = input()
                            if deposit_account_input == '1':
                                print("\nHow much would you like to deposit?\n")
                                deposit_input = input()
                                if int(deposit_input) >= 0:
                                    user.sav_bal += int(deposit_input)
                                    print(
                                        f'\nYour new Saving balance is ${user.sav_bal}\n')
                                if int(deposit_input) < 0:
                                    print("invalid amount\n")
                            if deposit_account_input == '2':
                                print("\nHow much would you like to deposit?\n")
                                deposit_input = input()
                                if int(deposit_input) >= 0:
                                    user.check_bal += int(deposit_input)
                                    print(
                                        f'\nYour new Checking balance is ${user.check_bal}\n')
                                if int(deposit_input) < 0:
                                    print("\ninvalid amount\n")
                        if main_menu_input == "3":
                            print(
                                "\nWhich account would you like to withdrawl from?\n1: Saving Account\n2: Checking Account\n")
                            withdrawl_account_input = input()
                            if withdrawl_account_input == '1':
                                print("\nHow much would you like to withdrawl?\n")
                                withdrawl_input = input()
                                if int(withdrawl_input) > user.sav_bal:
                                    print(
                                        "\nYou do not have enough funds in your Saving Account to withdrawl that much.\n")
                                if int(withdrawl_input) >= 0 and int(withdrawl_input) <= user.sav_bal:
                                    user.sav_bal += -int(withdrawl_input)
                                    print(
                                        f'\nYour new Saving Account balance is ${user.sav_bal}\n')
                                if int(withdrawl_input) < 0:
                                    print("\ninvalid amount\n")
                            if withdrawl_account_input == '2':
                                print("\nHow much would you like to withdrawl?\n")
                                withdrawl_input = input()
                                if int(withdrawl_input) > user.check_bal:
                                    print(
                                        "\nYou do not have enough funds in your Checking Account to withdrawl that much.\n")
                                if int(withdrawl_input) >= 0 and int(withdrawl_input) <= user.check_bal:
                                    user.check_bal += -int(withdrawl_input)
                                    print(
                                        f'\nYour new Checking Account balance is ${user.check_bal}\n')
                                if int(withdrawl_input) < 0:
                                    print("\ninvalid amount\n")
                        if main_menu_input == "4":
                            print(
                                "\nWhich account would you like to transfer from?\n1: Saving Account\n2: Checking Account\n")
                            transfer_account_input = input()
                            if transfer_account_input == '1':
                                print(
                                    "\nHow much would you like to transfer from your Saving Account to your Checking Account?\n")
                                transfer_input = input()
                                if int(transfer_input) > user.sav_bal:
                                    print(
                                        '\nYou don\'t have enough in your Saving Account to transfer that much\n')
                                if int(transfer_input) >= 0 and int(transfer_input) <= user.sav_bal:
                                    user.sav_bal += -int(transfer_input)
                                    user.check_bal += int(transfer_input)
                                    print(
                                        f'\nYour new Savings balance is ${user.sav_bal}\n')
                                    print(
                                        f'Your new Checking balance is ${user.check_bal}\n')
                                if int(transfer_input) < 0:
                                    print("\ninvalid amount\n")
                            if transfer_account_input == "2":
                                print(
                                    "\nHow much would you like to transfer from your Checking Account to your Saving Account?\n")
                                transfer_input = input()
                                if int(transfer_input) > user.check_bal:
                                    print(
                                        '\nYou don\'t have enough in your Checking Account to transfer that much\n')
                                if int(transfer_input) >= 0 and int(transfer_input) <= user.check_bal:
                                    user.check_bal += -int(transfer_input)
                                    user.sav_bal += int(transfer_input)
                                    print(
                                        f'\nYour new Checking balance is ${user.check_bal}\n')
                                    print(
                                        f'Your new Savings balance is ${user.sav_bal}\n')
                                if int(transfer_input) < 0:
                                    print("\ninvalid amount\n")
                        if main_menu_input == "5":
                            print("\nYou have successfully logged out\n")
                            return False
                        if main_menu_input == "99":
                            user.sav_bal += -(user.sav_bal)
                            user.check_bal += -(user.check_bal)
                            print(
                                f'\nCurrent Saving Balance: ${user.sav_bal}\n')
                            print(
                                f'Current Checking Balance: ${user.check_bal}\n')
                            print("You have been locked out\n")
                            locked_user.append(user)
                            i = 1
        print('\nInvalid account number\n')


virtual_wallet()
