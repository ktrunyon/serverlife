# tip calculator v1.1


class Bill(object):  # defines Bill as an object
    def __init__(self, bill_total):
        self.total = bill_total

    def calculate_tip(self, tip_pct):  # multiplies the bill total by the users desired tip percentage
        return self.total * tip_pct

    def calculate_total(self, tip_pct):  # adds tip amount to the total
        return self.total * (1 + tip_pct)


while True:
    total = float(input('\nPlease enter the total shown on your bill:'))  # prompts user to enter total shown on bill
    b = Bill(total)

    tip_percentage = float(input('\nTip percent (example: 15% --> 0.15): '))  # prompts user for desired tip percentage
    tip_amt = b.calculate_tip(tip_percentage)

    grand_total = b.calculate_total(tip_percentage)  # adds total and tip amount for a grand total

    print('\nYour meal will costs: ' + str(grand_total))  # prints grand total
