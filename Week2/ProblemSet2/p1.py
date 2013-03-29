total_paid = 0
monthly_interest_rate = annualInterestRate / 12

for month in range(1, 13):
    minimum_monthly_payment = monthlyPaymentRate * balance
    total_paid += minimum_monthly_payment
    balance -= minimum_monthly_payment
    balance += balance * monthly_interest_rate
    print """Month: %s
Minimum monthly payment: %s
Remaining balance: %s""" % (month, round(minimum_monthly_payment, 2), round(balance, 2))

print """Total paid: %s
Remaining balance: %s""" % (round(total_paid, 2), round(balance, 2))
