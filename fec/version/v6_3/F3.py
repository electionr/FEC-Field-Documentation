import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'CHANGE OF ADDRESS', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ELECTION STATE', 'number': '10'},
            {'name': 'ELECTION DISTRICT', 'number': '11'},
            {'name': 'REPORT CODE', 'number': '12'},
            {'name': 'ELECTION CODE', 'number': '13'},
            {'name': 'DATE OF ELECTION', 'number': '14'},
            {'name': 'STATE OF ELECTION', 'number': '15'},
            {'name': 'COVERAGE FROM DATE', 'number': '16'},
            {'name': 'COVERAGE THROUGH DATE', 'number': '17'},
            {'name': 'TREASURER LAST NAME', 'number': '18'},
            {'name': 'TREASURER FIRST NAME', 'number': '19'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '20'},
            {'name': 'TREASURER PREFIX', 'number': '21'},
            {'name': 'TREASURER SUFFIX', 'number': '22'},
            {'name': 'DATE SIGNED', 'number': '23'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '24'},
            {'name': 'CANDIDATE LAST NAME', 'number': '25'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '26'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '27'},
            {'name': 'CANDIDATE PREFIX', 'number': '28'},
            {'name': 'CANDIDATE SUFFIX', 'number': '29'},
            {'name': 'F3Z-1 REPORT TYPE', 'number': '30'},
            {'name': 'Total Contributions (NO Loans)', 'number': '31-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '32-(6b)'},
            {'name': 'Net Contributions', 'number': '33-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '34-(7a)'},
            {'name': 'Total Offset to Operating Expenditures', 'number': '35-(7b)'},
            {'name': 'NET Operating Expenditures.', 'number': '36-(7c)'},
            {'name': 'CASH ON HAND AT CLOSE ...', 'number': '37-8.'},
            {'name': 'DEBTS TO ( Totals from SCH C and/or D)', 'number': '38-9.'},
            {'name': 'DEBTS BY (Totals from SCH C and/or D)', 'number': '39-10.'},
            {'name': 'Individuals Itemized', 'number': '40-11(a i.)'},
            {'name': 'Individuals Unitemized', 'number': '41-11(a.ii)'},
            {'name': 'Individual Contribution Total', 'number': '42-11(a.iii)'},
            {'name': 'Political Party Committees', 'number': '43-11(b)'},
            {'name': 'Other Political Committees', 'number': '44-11(c)'},
            {'name': 'The Candidate', 'number': '45-11(d)'},
            {'name': 'Total Contributions', 'number': '46-11(e)'},
            {'name': 'Transfers From Other Authorized Committees', 'number': '47-12.'},
            {'name': 'Loans made or guarn. by the Candidate', 'number': '48-13(a)'},
            {'name': 'All Other Loans', 'number': '49-13(b)'},
            {'name': 'Total Loans', 'number': '50-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '51-14.'},
            {'name': 'Other Receipts', 'number': '52-15.'},
            {'name': 'Total Receipts', 'number': '53-16.'},
            {'name': 'Operating Expenditures', 'number': '54-17.'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '55-18.'},
            {'name': 'Of Loans made or guar. by the Cand.', 'number': '56-19(a)'},
            {'name': 'Loan Repayments, All Other Loans', 'number': '57-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '58-19(c)'},
            {'name': 'Refund/Individuals Other than Political Committees', 'number': '59-20(a)'},
            {'name': 'Refund/Political Party Committees', 'number': '60-20(b)'},
            {'name': 'Refund/Other Political Committees', 'number': '61-20(c)'},
            {'name': 'Total Contribution Refunds', 'number': '62-20(d)'},
            {'name': 'Other Disbursements', 'number': '63-21.'},
            {'name': 'Total Disbursements', 'number': '64-22.'},
            {'name': 'Cash Beginning Reporting Period', 'number': '65-23.'},
            {'name': 'Total Receipts this Period', 'number': '66-24.'},
            {'name': 'SubTotal', 'number': '67-25.'},
            {'name': 'Total Disbursements this Period', 'number': '68-26.'},
            {'name': 'Cash on hand at Close Period', 'number': '69-27.'},
            {'name': 'Total Contributions (No Loans)', 'number': '70-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '71-(6b)'},
            {'name': 'Net Contributions', 'number': '72-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '73-(7a)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '74-(7b)'},
            {'name': 'NET Operating Expenditures.', 'number': '75-(7c)'},
            {'name': 'Individuals Itemized', 'number': '76-11(a i.)'},
            {'name': 'Individuals Unitemized', 'number': '77-11(a.ii)'},
            {'name': 'Individuals Total', 'number': '78-11(a.iii)'},
            {'name': 'Political Party Committees', 'number': '79-11(b)'},
            {'name': 'All Other Political Committees (PACS)', 'number': '80-11(c)'},
            {'name': 'The Candidate', 'number': '81-11(d)'},
            {'name': 'Total Contributions', 'number': '82-11(e)'},
            {'name': 'Transfers From Other AUTH Committees', 'number': '83-12.'},
            {'name': 'Loans made or guarn. by the Candidate', 'number': '84-13(a)'},
            {'name': 'All Other Loans', 'number': '85-13(b)'},
            {'name': 'Total Loans', 'number': '86-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '87-14.'},
            {'name': 'Other Receipts', 'number': '88-15.'},
            {'name': 'Total Receipts', 'number': '89-16.'},
            {'name': 'Operating Expenditures', 'number': '90-17'},
            {'name': 'Transfers To Other AUTH Committees', 'number': '91-18.'},
            {'name': 'Loan Repayment By Candidate', 'number': '92-19(a)'},
            {'name': 'Loan Repayments, ALL Other Loans', 'number': '93-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '94-19(c)'},
            {'name': 'Refund/Individuals Other than Political Committees', 'number': '95-20(a)'},
            {'name': 'Refund, Political Party Committees', 'number': '96-20(b)'},
            {'name': 'Refund, Other Political Committees', 'number': '97-20(c)'},
            {'name': 'Total Contributions Refunds', 'number': '98-20(d)'},
            {'name': 'Other Disbursements', 'number': '99-21.'},
            {'name': 'Total Disbursements', 'number': '100-22.'},
            {'name': 'Gross Receipts of Authorized Committees (primary)', 'number': '101'},
            {'name': 'Aggregate Amount from Personal Funds (primary)', 'number': '102'},
            {'name': 'Gross Receipts Minus Personal from Candidate (primary)', 'number': '103'},
            {'name': 'Gross Receipts of Authorized Committees (general)', 'number': '104'},
            {'name': 'Aggregate Amount from Personal Funds (general)', 'number': '105'},
            {'name': 'Gross Receipts Minus Personal from Candidate (general)', 'number': '106'},
    ]
        self.fields_names = self.hash_names(self.fields)
