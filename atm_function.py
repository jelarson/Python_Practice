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

users = [jim, sarah, debbie]

locked_user = []


def acct_pin_verif(users, locked_user):
    print('What is your account number?\n')
    acct_input = input()
    locked = False
    for user in locked_user:
        if acct_input == user.acct_num:
            print("\nYour account has been locked out")
            locked = True
    if locked:
        return acct_pin_verif(users, locked_user)
    for user in users:
        if acct_input != user.acct_num:
            print('\nIncorrect Account Number\n')
            return acct_pin_verif(users, locked_user)
        if acct_input == user.acct_num:
            print('\nWhat is your PIN Number?\n')
            pin_input = input()
            if pin_input != user.pin_num:
                print('\nIncorrect PIN number\n')
                return acct_pin_verif(users, locked_user)
            if pin_input == user.pin_num:
                print(f'\nWelcome, {user.name}!\n')
                return main_menu(user)


def main_menu(user):
    print("Main Menu\n\n1: Check Balance\n2: Deposit\n3: Withdrawl\n4: Transfer Within Your Account\n5: Exit\n")
    main_menu_input = input()
    if main_menu_input == "1":
        balance_display(user)
        return back_option(user)
    if main_menu_input == "2":
        return option_two(user)
    if main_menu_input == "3":
        return option_three(user)
    if main_menu_input == "4":
        return option_four(user)
    if main_menu_input == "5":
        print("\nYou have successfully logged out\n")
        return acct_pin_verif(users, locked_user)
    if main_menu_input == "99":
        return option_ninety_nine(user)


def back_option(user):
    print('\nWhat would you like to do next?\n1: Main Menu\n2: Logout\n')
    back_option_input = input()
    if back_option_input == "1":
        return main_menu(user)
    if back_option_input == "2":
        return acct_pin_verif(users, locked_user)


def option_two(user):
    print("\nWhich account would you like to deposit to?\n1: Saving Account\n2: Checking Account\n")
    deposit_account_input = input()
    if deposit_account_input == '1':
        print("\nHow much would you like to deposit?\n")
        deposit_input = input()
        if int(deposit_input) >= 0:
            user.sav_bal += int(deposit_input)
            print(f'\nYour new Saving balance is ${user.sav_bal}')
            return back_option(user)
        if int(deposit_input) < 0:
            print("invalid amount")
            return back_option(user)
    if deposit_account_input == '2':
        print("\nHow much would you like to deposit?\n")
        deposit_input = input()
        if int(deposit_input) >= 0:
            user.check_bal += int(deposit_input)
            print(f'\nYour new Checking balance is ${user.check_bal}')
            return back_option(user)
        if int(deposit_input) < 0:
            print("\ninvalid amount")
            return back_option(user)


def option_three(user):
    print("\nWhich account would you like to withdrawl from?\n1: Saving Account\n2: Checking Account\n")
    withdrawl_account_input = input()
    if withdrawl_account_input == '1':
        print("\nHow much would you like to withdrawl?\n")
        withdrawl_input = input()
        if int(withdrawl_input) > user.sav_bal:
            print(
                "\nYou do not have enough funds in your Saving Account to withdrawl that much.")
            return back_option(user)
        if int(withdrawl_input) >= 0 and int(withdrawl_input) <= user.sav_bal:
            user.sav_bal += -int(withdrawl_input)
            print(f'\nYour new Saving Account balance is ${user.sav_bal}')
            return back_option(user)
        if int(withdrawl_input) < 0:
            print("\ninvalid amount")
            return back_option(user)
    if withdrawl_account_input == '2':
        print("\nHow much would you like to withdrawl?\n")
        withdrawl_input = input()
        if int(withdrawl_input) > user.check_bal:
            print(
                "\nYou do not have enough funds in your Checking Account to withdrawl that much.")
            return back_option(user)
        if int(withdrawl_input) >= 0 and int(withdrawl_input) <= user.check_bal:
            user.check_bal += -int(withdrawl_input)
            print(f'\nYour new Checking Account balance is ${user.check_bal}')
            return back_option(user)
        if int(withdrawl_input) < 0:
            print("\ninvalid amount")
            return back_option(user)


def option_four(user):
    print("\nWhich account would you like to transfer from?\n1: Saving Account\n2: Checking Account\n")
    transfer_account_input = input()
    if transfer_account_input == '1':
        print("\nHow much would you like to transfer from your Saving Account to your Checking Account?\n")
        transfer_input = input()
        if int(transfer_input) > user.sav_bal:
            print('\nYou don\'t have enough in your Saving Account to transfer that much')
            return back_option(user)
        if int(transfer_input) >= 0 and int(transfer_input) <= user.sav_bal:
            user.sav_bal += -int(transfer_input)
            user.check_bal += int(transfer_input)
            balance_display(user)
            return back_option(user)
        if int(transfer_input) < 0:
            print("\ninvalid amount")
            return back_option(user)
    if transfer_account_input == "2":
        print("\nHow much would you like to transfer from your Checking Account to your Saving Account?\n")
        transfer_input = input()
        if int(transfer_input) > user.check_bal:
            print(
                '\nYou don\'t have enough in your Checking Account to transfer that much')
            return back_option(user)
        if int(transfer_input) >= 0 and int(transfer_input) <= user.check_bal:
            user.check_bal += -int(transfer_input)
            user.sav_bal += int(transfer_input)
            balance_display(user)
            return back_option(user)
        if int(transfer_input) < 0:
            print("\ninvalid amount")
            return back_option(user)


def option_ninety_nine(user):
    user.sav_bal += -(user.sav_bal)
    user.check_bal += -(user.check_bal)
    balance_display(user)
    print("You have been locked out\n")
    locked_user.append(user)
    users.pop(users.index(user))
    return acct_pin_verif(users, locked_user)


def balance_display(user):
    print(f'\nCurrent Saving Balance: ${user.sav_bal}\n')
    print(f'Current Checking Balance: ${user.check_bal}\n')


acct_pin_verif(users, locked_user)
