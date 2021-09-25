class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommate:
    """
    Creates a roommate who lives in the apartment and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, roommate2):
        weight = self.days_in_house/(self.days_in_house + roommate2.days_in_house )
        return bill.amount * weight


class PdfReport:
    """
    Create a PDF file that contains data about the roommate, such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


bill = Bill(120, "March 2021")
john = Roommate("John", 20)
marry = Roommate("Mary", 25)
print(john.pays(bill, marry))
print(marry.pays(bill, john))


