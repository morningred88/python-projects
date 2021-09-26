import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Create a PDF file that contains data about the roommate, such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        due_roommate1 = "$" + str(round(roommate1.pays(bill, roommate2),2))
        due_roommate2 = "$" + str(round(roommate2.pays(bill, roommate1), 2))
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add icon, set the width and height
        pdf.image("files/house.png", w=50, h=50)

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

        # Change the directory to files, generate and open PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)