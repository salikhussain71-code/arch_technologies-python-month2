class ATM:
    """Stores account data and handles banking operations."""

    def __init__(self, owner, pin, balance=0.0):
        self.owner = owner
        self.__pin = pin
        self.__balance = balance
        self.transactions = []

    def verify_pin(self, pin):
        return pin == self.__pin

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."

        self.__balance += amount

        self.transactions.append(
            ("Deposit", amount, self.__balance)
        )

        return True, f"Successfully deposited ${amount:,.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."

        if amount > self.__balance:
            return False, "Insufficient funds. Transaction cancelled."

        self.__balance -= amount

        self.transactions.append(
            ("Withdrawal", amount, self.__balance)
        )

        return True, f"Please collect your cash: ${amount:,.2f}."


class ATMController:
    """Handles user interaction."""

    def __init__(self, atm):
        self.atm = atm

    def read_amount(self, prompt):
        try:
            return float(input(prompt).strip())

        except ValueError:
            print("Invalid amount. Please enter a number.")
            return None

    def login(self):
        for attempt in range(1, 4):

            pin = input("Enter your 4-digit PIN: ").strip()

            if self.atm.verify_pin(pin):
                print(f"\nWelcome, {self.atm.owner}!")
                return True

            print(f"Incorrect PIN. Attempts left: {3 - attempt}")

        print("Too many wrong attempts. Card blocked.")
        return False

    def show_menu(self):
        print("\n========== ATM MENU ==========")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Mini statement")
        print("5. Exit")

    def show_statement(self):

        if not self.atm.transactions:
            print("No transactions yet.")
            return

        print("\n--- Mini Statement ---")

        for kind, amount, balance in self.atm.transactions[-5:]:
            print(
                f"{kind:<11} ${amount:>10,.2f}   "
                f"Balance: ${balance:,.2f}"
            )

    def run(self):
        print("====== WELCOME TO PYTHON BANK ATM ======")

        if not self.login():
            return

        while True:

            self.show_menu()

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":

                print(
                    f"Your current balance is "
                    f"${self.atm.check_balance():,.2f}"
                )

            elif choice == "2":

                amount = self.read_amount(
                    "Enter amount to deposit: $"
                )

                if amount is not None:
                    print(self.atm.deposit(amount)[1])

            elif choice == "3":

                amount = self.read_amount(
                    "Enter amount to withdraw: $"
                )

                if amount is not None:
                    print(self.atm.withdraw(amount)[1])

            elif choice == "4":
                self.show_statement()

            elif choice == "5":

                print(
                    "Thank you for using Python Bank ATM. Goodbye!"
                )
                break

            else:
                print(
                    "Invalid option. Please choose 1, 2, 3, 4, or 5."
                )


if __name__ == "__main__":

    account = ATM(
        "Salik Hussain",
        "1234",
        balance=1000.0
    )

    controller = ATMController(account)
    controller.run()