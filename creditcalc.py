import argparse
import math


if __name__ == "__main__":
    def calculate_diff_payment(principal, periods, interest):
        total_p = 0
        i = interest / (100 * 12)
        for month in range(1, periods + 1):
            diff_p = math.ceil(principal / periods + i * (principal - principal * (month - 1) / periods))
            total_p += diff_p
            print(f"Month {month}: payment is {diff_p}")

        overpayment = total_p - principal
        print(f"\nOverpayment = {int(overpayment)}")


    def calculate_monthly_payment(principal, periods, interest):
        i = interest / (100 * 12)
        dividend = i * (1 + i) ** periods
        divisor = (1 + i) ** periods - 1
        payment = math.ceil(principal * dividend / divisor)
        message = f"Your annuity payment = {payment}"
        print(message + "!")

        overpayment = periods * payment - principal
        print(f"Overpayment = {int(overpayment)}")


    def calculate_principal(payment, periods, interest):
        i = interest / (100 * 12)
        divisor = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
        principal = payment / divisor
        print(f"Your loan principal = {round(principal)}!")

        overpayment = periods * payment - principal
        print(f"Overpayment = {int(overpayment)}")


    def calculate_number_of_months(principal, payment, interest):
        i = interest / (100 * 12)
        x = payment / (payment - i * principal)
        periods = math.ceil(math.log(x, 1 + i))
        years, months = divmod(periods, 12)
        message = f"It will take "
        if years:
            message += f"{years} year{'s' if years > 1 else ''} {'and ' if months else ''}"
        if months:
            message += f"{months} month{'s' if months > 1 else ''}"
        message += "to repay this loan!"
        print(message)
        overpayment = periods * payment - principal
        print(f"Overpayment = {int(overpayment)}")


    def contain_negative_value(args):
        for arg in vars(args):
            if getattr(args, arg) and not isinstance(getattr(args, arg), str) and getattr(args, arg) < 0:
                return True


    parser = argparse.ArgumentParser(description="Welcome to Loan Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"])
    parser.add_argument("--payment", type=float, help="Monthly payment")  # monthly payment
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
    parser.add_argument("--interest", type=float, help="Nominal interest rate [%]")

    args = parser.parse_args()
    if (args.type == "diff" and args.payment) or \
            len(vars(args)) < 4 or \
            contain_negative_value(args) or \
            not args.type or \
            not args.interest:
        print("Incorrect parameters")
    else:
        if not args.payment:
            if args.type == "diff":
                calculate_diff_payment(args.principal, args.periods, args.interest)
            else:
                calculate_monthly_payment(args.principal, args.periods, args.interest)
        elif not args.principal:
            calculate_principal(args.payment, args.periods, args.interest)
        elif not args.periods:
            calculate_number_of_months(args.principal, args.payment, args.interest)
