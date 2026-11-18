def calculate_simple_intrest(principal,rate,time_year):
    """calculate simple intrest"""
    intrest=principal*rate*time_year
    return intrest
#----usu=ing the function----
loan_amount=100000
annual_rate=0.05
loan_duration=3
intrest_payable=calculate_simple_intrest(loan_amount,annual_rate,loan_duration)
print(f"loan intrest payable:Rs.{intrest_payable:,.2f}")
#another example
deposit_amount=50000
deposit_rate=0.03
deposite_time=1
earned_intrest=calculate_simple_intrest(deposit_amount,deposit_rate,deposite_time)
print(f"Deposit intrest Earned : Rs.{earned_intrest:,.2f}")