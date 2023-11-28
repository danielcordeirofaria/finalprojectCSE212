class BankStatement:
    def __init__(self):
        self.balance = 0
        self.deposits = []

    def invest(self, amount, term):
        annual_interest_rate = 0.12
        period_interest_rate = (1 + annual_interest_rate) ** (term / 365) - 1
        interest_earned = amount * period_interest_rate
        net_amount = amount + interest_earned
        self.balance += net_amount
        self.deposits.append({"amount": net_amount, "term": term, "interest_earned": interest_earned})

    def calculate_tax(self, interest_earned, term):
        if term <= 180:
            return interest_earned * 0.225
        elif 181 <= term <= 360:
            return interest_earned * 0.20
        elif 361 <= term <= 720:
            return interest_earned * 0.175
        else:
            return interest_earned * 0.15

    def withdraw(self, withdrawal_amount):
        if not self.deposits:
            print("Error: No investment to withdraw from.")
            return

        net_amount_total = 0
        tax_total = 0

        while self.deposits and withdrawal_amount > 0:
            deposit = self.deposits.pop()  # Pop the last deposit

            withdrawal_amount += tax_total  # Adjust the withdrawal amount with the accumulated tax

            deposit_amount = deposit["amount"]
            term = deposit["term"]
            interest_earned = deposit["interest_earned"]

            tax = self.calculate_tax(interest_earned, term)
            net_amount = deposit_amount - tax

            if net_amount < withdrawal_amount:
                net_amount_total += net_amount
                tax_total += tax
                withdrawal_amount -= net_amount
            else:
                net_amount_total += withdrawal_amount
                tax_total += withdrawal_amount * (tax / interest_earned)

                # If there is a remainder, add the remaining amount back to the deposits with the same term
                if net_amount - withdrawal_amount > 0:
                    self.deposits.append({"amount": net_amount - withdrawal_amount, "term": term, "interest_earned": interest_earned})

                withdrawal_amount = 0

        # Update the balance
        self.balance -= net_amount_total

        # Return the total net amount and total tax
        return net_amount_total, tax_total

# Example of usage:
statement = BankStatement()

statement.invest(500, 540)
statement.invest(1000, 365)
statement.invest(350, 59)

print("Balance before withdrawal: ${:.2f}".format(statement.balance))

for i, deposit in enumerate(statement.deposits, start=1):
    print(f"Deposit {i}: ${deposit['amount']:.2f} (Term: {deposit['term']} days)")

withdrawn_amount, tax = statement.withdraw(800)
print("Amount withdrawn: ${:.2f} (Tax: ${:.2f})".format(withdrawn_amount, tax))

print("Balance after withdrawal: ${:.2f}".format(statement.balance))
