import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'COMMITTEE/ORG TYPE', 'number': '9'},
            {'name': 'COMMITTEE/ORG TYPE - OTHER DESCRIPTION', 'number': '10'},
            {'name': 'REPORT CODE', 'number': '11'},
            {'name': 'COVERAGE FROM DATE', 'number': '12'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '13'},
            {'name': 'TREASURER LAST NAME', 'number': '14'},
            {'name': 'TREASURER FIRST NAME', 'number': '15'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '16'},
            {'name': 'TREASURER PREFIX', 'number': '17'},
            {'name': 'TREASURER SUFFIX', 'number': '18'},
            {'name': 'DATE SIGNED', 'number': '19'},
            {'name': 'cash on hand beg. report per.', 'number': '20-6.(b)'},
            {'name': 'Total receipts', 'number': '21-6.(c)'},
            {'name': 'Subtotal', 'number': '22-6.(d)'},
            {'name': 'Total disbursements', 'number': '23-7.'},
            {'name': 'COH CLOSE (COL A)', 'number': '24-8.'},
            {'name': 'Debts to', 'number': '25-9.'},
            {'name': 'Debts by', 'number': '26-10.'},
            {'name': 'Convention expenditures', 'number': '27-11.'},
            {'name': 'refunds/rebates/returns relating to conv exp.', 'number': '28-12.'},
            {'name': 'Expenditures subject to limits', 'number': '29-12(a)'},
            {'name': 'expend. from prior years subject to limits', 'number': '30-12(b)'},
            {'name': 'Federal Funds SCH A', 'number': '31-13.'},
            {'name': 'Itemized', 'number': '32-14(a)'},
            {'name': 'unitemized', 'number': '33-14(b)'},
            {'name': 'subtotal', 'number': '34-14(c)'},
            {'name': 'Transfers from affiliated Committees.', 'number': '35-15.'},
            {'name': 'loans received', 'number': '36-16(a)'},
            {'name': 'loan repayments received', 'number': '37-16(b)'},
            {'name': 'subtotal loans/repayments', 'number': '38-16(c)'},
            {'name': 'Itemized', 'number': '39-17(a)'},
            {'name': 'unitemized', 'number': '40-17(b)'},
            {'name': 'subtotal', 'number': '41-17(c)'},
            {'name': 'Itemized', 'number': '42-18(a)'},
            {'name': 'unitemized', 'number': '43-18(b)'},
            {'name': 'subtotal', 'number': '44-18(c)'},
            {'name': 'Itemized', 'number': '45-19(a)'},
            {'name': 'unitemized', 'number': '46-19(b)'},
            {'name': 'subtotal', 'number': '47-19(c)'},
            {'name': 'total receipts', 'number': '48-20.'},
            {'name': 'Itemized', 'number': '49-21(a)'},
            {'name': 'unitemized', 'number': '50-21(b)'},
            {'name': 'subtotal', 'number': '51-21(c)'},
            {'name': 'Transfers to Affiliated Committees', 'number': '52-22.'},
            {'name': 'loans made', 'number': '53-23(a)'},
            {'name': 'loan repayments made', 'number': '54-23(b)'},
            {'name': 'subtotal', 'number': '55-23(c)'},
            {'name': 'Itemized', 'number': '56-24(a)'},
            {'name': 'unitemized', 'number': '57-24(b)'},
            {'name': 'subtotal', 'number': '58-24(c)'},
            {'name': 'Total disbursements', 'number': '59-25.'},
            {'name': 'Cash on Hand', 'number': '60-6.(a)'},
            {'name': 'YEAR', 'number': '61-6.(a) 19'},
            {'name': 'Total receipts', 'number': '62-6.(c)'},
            {'name': 'Subtotal', 'number': '63-6.(d)'},
            {'name': 'Total disbursements', 'number': '64-7.'},
            {'name': 'COH CLOSE (COL B)', 'number': '65-8.'},
            {'name': 'Convention expenditures', 'number': '66-11.'},
            {'name': 'refunds/rebates/returns relating to conv exp.', 'number': '67-12.'},
            {'name': 'Expenditures subject to limits', 'number': '68-12(a)'},
            {'name': 'expend. from prior years subject to limits', 'number': '69-12(b)'},
            {'name': 'total expenditures subject to limits', 'number': '70-12(c)'},
            {'name': 'Federal Funds', 'number': '71-13.'},
            {'name': 'subtotal', 'number': '72-14(c)'},
            {'name': 'Transfers from affiliated Committees.', 'number': '73-15.'},
            {'name': 'subtotal loans/repayments', 'number': '74-16(c)'},
            {'name': 'subtotal', 'number': '75-17(c)'},
            {'name': 'subtotal', 'number': '76-18(c)'},
            {'name': 'subtotal', 'number': '77-19(c)'},
            {'name': 'total receipts', 'number': '78-20.'},
            {'name': 'subtotal', 'number': '79-21(c)'},
            {'name': 'Transfers to Affiliated Committees', 'number': '80-22.'},
            {'name': 'subtotal', 'number': '81-23(c)'},
            {'name': 'subtotal', 'number': '82-24(c)'},
            {'name': 'Total disbursements', 'number': '83-25.'},
    ]
        self.fields_names = self.hash_names(self.fields)
