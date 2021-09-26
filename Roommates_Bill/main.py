from fpdf import FPDF


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
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        return bill.amount * weight


class PdfReport:
    """
    Create a PDF file that contains data about the roommate, such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        due_roommate1 = str(round(roommate1.pays(bill, roommate2),2))
        due_roommate2 = str(round(roommate2.pays(bill, roommate1), 2))
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add icon, set the width and height
        pdf.image("house.png", w=50, h=50)

        # Insert title, set the style to bold
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)

        # Insert period
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=200, h=25, txt=due_roommate1, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=200, h=25, txt=due_roommate2, border=0, ln=1)

        pdf.output(self.filename)


bill = Bill(120, "September 2021")
john = Roommate("John", 20)
marry = Roommate("Mary", 25)
print(f'John pays {john.pays(bill, marry)}')
print(f'Marry pays {marry.pays(bill, john)}')

pdf_report = PdfReport("Bill.pdf")
pdf_report.generate(john, marry, bill)
