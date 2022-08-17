'''
    A financial institution provides professional services to banks and claims charges from
    the customers based on the number of man-days provided. Internally, it has set a scheme
    to motivate and reward staf to meet and exceed targeted billable utilization and revenues
    by paying a bonus for each day claimed from customers in excess of a threshold target.
    This quarterly scheme is calculated with a threshold target of 32 days per quarter, and
    the incentive payment for each billable day in excess of such threshold target is shown
    as follows:
    >> 0 to 32 days - zero bonus
    >> 33 to 40 days - SGD $325 per billable day
    >> 41 to 48 days - SGD $550 per billable day
    >> greater than 48 days - SGD $600 per billable day
    Incentive payment is calculated progressively. eg - if an employee reached total billable
    days of 45 in a quarter, his/her incentive payment is computed as follows :
    32 * 0 + 8 * 325 + 5 * 550 = 5350
    Write a function to read the billable days of an employee and return the bonus he/she
    has obtained in that quarter.
    bonus(15) - 0, bonus(37) - 1625, bonus(50) - 8200
'''
def bonus(num_of_days):
    if num_of_days > 32:
        a = 32
        if num_of_days > 40:
            b = 40 - a
            if num_of_days > 48:
                c = 48 - (a + b)
                total = a * 0 + b * 325 + c * 550 + (num_of_days - 48) * 600
            else:
                total = a * 0 + b * 325 + (num_of_days - 40) * 550
        else:
            total = a * 0 + (num_of_days - 32) * 325
    else:
        total = num_of_days * 0
    print(total)

bonus(50)
print(325 * 8 + 8 * 550 + 2 * 600)