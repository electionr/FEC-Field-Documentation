import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'QUALIFIED CMTE blank or X', 'number': '10'},
            {'name': 'RPTCODE', 'number': '11'},
            {'name': 'RPTPGI', 'number': '12'},
            {'name': 'OF ELECTION', 'number': '13-'},
            {'name': 'STATE (OF ELECTION)', 'number': '14'},
            {'name': 'COVERAGE FROM', 'number': '15-'},
            {'name': 'COVERAGE TO', 'number': '16-'},
            {'name': 'Cash on Hand beginning', 'number': '17-6(b)'},
            {'name': 'total receipts', 'number': '18-6(c)'},
            {'name': 'subtotal', 'number': '19-6(d)'},
            {'name': 'total disbursements', 'number': '20-7.'},
            {'name': 'Cash on Hand at Close', 'number': '21-8.'},
            {'name': 'Debts to', 'number': '22-9.'},
            {'name': 'Debts by', 'number': '23-10.'},
            {'name': 'itemized', 'number': '24-11(a)i'},
            {'name': 'unitemized', 'number': '25-11(a)ii'},
            {'name': 'total', 'number': '26-11(a)iii'},
            {'name': 'Political party committees', 'number': '27-11(b)'},
            {'name': 'Other Political Committees (PACs)', 'number': '28-11(c)'},
            {'name': 'total contributions', 'number': '29-11(d)'},
            {'name': 'Transfers from Affiliated/Other Party Committees', 'number': '30-12.'},
            {'name': 'All loans Received', 'number': '31-13.'},
            {'name': 'loan repayments received', 'number': '32-14.'},
            {'name': 'offsets to Operating Expenditures (refunds ...)', 'number': '33-15.'},
            {'name': 'Refunds of Federal contributions', 'number': '34-16.'},
            {'name': 'Other Federal Receipts (dividends)', 'number': '35-17.'},
            {'name': 'transfers from Nonfederal Account', 'number': '36-18.'},
            {'name': 'Total Receipts', 'number': '37-19.'},
            {'name': 'Total Federal Receipts', 'number': '38-20.'},
            {'name': 'Federal Share', 'number': '39-21(a)i'},
            {'name': 'non-federal share', 'number': '40-21(a)ii'},
            {'name': 'other Federal operating expenditures', 'number': '41-21(b)'},
            {'name': 'total operating expenditures', 'number': '42-21(c)'},
            {'name': 'Transfers to Affiliated/Other Party Committees', 'number': '43-22.'},
            {'name': 'Contributions to Federal Candidates/Committees', 'number': '44-23.'},
            {'name': 'Independent expenditures', 'number': '45-24.'},
            {'name': 'Coordinated Expenditures made by party Committees', 'number': '46-25.'},
            {'name': 'Loan repayments', 'number': '47-26.'},
            {'name': 'Loans Made', 'number': '48-27.'},
            {'name': 'Individuals/Persons', 'number': '49-28(a)'},
            {'name': 'Political Party Committees', 'number': '50-28(b)'},
            {'name': 'Other Political Committees', 'number': '51-28(c)'},
            {'name': 'Total contributions refunds', 'number': '52-28(d)'},
            {'name': 'Other disbursements', 'number': '53-29.'},
            {'name': 'Total disbursements', 'number': '54-30.'},
            {'name': 'Total Federal Disbursements', 'number': '55-31.'},
            {'name': 'Total contributions', 'number': '56-32.'},
            {'name': 'Total Contribution Refunds', 'number': '57-33.'},
            {'name': 'Net Contributions', 'number': '58-34.'},
            {'name': 'Total Federal Operating Expenditures', 'number': '59-35.'},
            {'name': 'Offsets to operating Expenditures', 'number': '60-36.'},
            {'name': 'Net operating Expenditures', 'number': '61-37.'},
            {'name': 'cash on hand Jan 1, 19', 'number': '62-6(a)'},
            {'name': 'Year for above', 'number': '63'},
            {'name': 'total receipts', 'number': '64-6(c)'},
            {'name': 'subtotal', 'number': '65-6(d)'},
            {'name': 'Total disbursements', 'number': '66-7.'},
            {'name': 'Cash on Hand Close', 'number': '67-8.'},
            {'name': 'itemized', 'number': '68-11(a)i'},
            {'name': 'unitemized', 'number': '69-11(a)ii'},
            {'name': 'Total', 'number': '70-11(a)iii'},
            {'name': 'Politial Party committees', 'number': '71-11(b)'},
            {'name': 'Other Political Committees(PACs)', 'number': '72-11(c)'},
            {'name': 'Total contributions', 'number': '73-11(d)'},
            {'name': 'Transfers from Affiliated/Other Party Committees', 'number': '74-12.'},
            {'name': 'All loans Received', 'number': '75-13.'},
            {'name': 'loan repayments received', 'number': '76-14.'},
            {'name': 'offsets to Operating Expenditures (refunds)', 'number': '77-15.'},
            {'name': 'Refunds of Federal contributions', 'number': '78-16.'},
            {'name': 'Other Federal Receipts (dividends)', 'number': '79-17.'},
            {'name': 'transfers from Nonfederal Account', 'number': '80-18.'},
            {'name': 'Total receipts', 'number': '81-19.'},
            {'name': 'Total federal receipts', 'number': '82-20'},
            {'name': 'Federal Share', 'number': '83-21(a)i'},
            {'name': 'non-federal share', 'number': '84-21(a)ii'},
            {'name': 'other Federal operating expenditures', 'number': '85-21(b)'},
            {'name': 'Total operating Expenditures', 'number': '86-21(c)'},
            {'name': 'Transfers to Affiliated/OtherParty Committees', 'number': '87-22.'},
            {'name': 'Contributions to Federal Candidates/Committees', 'number': '88-23.'},
            {'name': 'Independent Expenditures', 'number': '89-24.'},
            {'name': 'Coordinated Expenditures made by party Committees', 'number': '90-25.'},
            {'name': 'Loan repayments Made', 'number': '91-26.'},
            {'name': 'Loans Made', 'number': '92-27.'},
            {'name': 'individuals/Persons', 'number': '93-28(a)'},
            {'name': 'Political Party Committees', 'number': '94-28(b)'},
            {'name': 'Other Political Committees', 'number': '95-28(c)'},
            {'name': 'Total contributions refunds', 'number': '96-28(d)'},
            {'name': 'Other Disbursements', 'number': '97-29.'},
            {'name': 'Total Disbursements', 'number': '98-30.'},
            {'name': 'Total Federal Disbursements', 'number': '99-31.'},
            {'name': 'Total Contributions', 'number': '100-. 32.'},
            {'name': 'Total Contribution Refunds', 'number': '101-33.'},
            {'name': 'Net contributions', 'number': '102-34.'},
            {'name': 'Total Federal Operating Expenditures', 'number': '103-35.'},
            {'name': 'Offsets to Operating Expenditures', 'number': '104-36.'},
            {'name': 'Net Operating Expenditures', 'number': '105-37.'},
            {'name': 'TREASURER', 'number': '106-'},
            {'name': 'SIGNED', 'number': '107-'},
    ]
        self.fields_names = self.hash_names(self.fields)
