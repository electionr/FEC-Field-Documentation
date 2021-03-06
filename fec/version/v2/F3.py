import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET1', 'number': '4'},
            {'name': 'STREET2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'Net Operating Expenditures', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'CHG OF ADDRESS', 'number': '10'},
            {'name': 'ELECTION STATE', 'number': '11'},
            {'name': 'ELECTION DISTRICT', 'number': '12'},
            {'name': 'RPTCODE', 'number': '13'},
            {'name': 'RPTPGI', 'number': '14'},
            {'name': 'DATE(Of Election)', 'number': '15'},
            {'name': 'STATE (Of Election)', 'number': '16'},
            {'name': 'PRIMARY ELECTION', 'number': '17'},
            {'name': 'GENERAL ELECTION', 'number': '18'},
            {'name': 'SPECIAL ELECTION', 'number': '19'},
            {'name': 'RUNOFF ELECTION', 'number': '20'},
            {'name': 'Coverage From', 'number': '21-'},
            {'name': 'Coverage To', 'number': '22-'},
            {'name': 'Total Contributions (NO Loans)', 'number': '23-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '24-(6b)'},
            {'name': 'Net Contributions', 'number': '25-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '26-(7a)'},
            {'name': 'Total Offset to Operating Expenditures', 'number': '27-(7b)'},
            {'name': 'NET Operating Expenditures', 'number': '28-(7c)'},
            {'name': 'CASH ON HAND AT CLOSE OF REPORTING PD:', 'number': '29-8'},
            {'name': 'DEBTS TO ( Totals from SCH C and/or D)', 'number': '30-9'},
            {'name': 'DEBTS BY (Totals from SCH C and/or D)', 'number': '31-10'},
            {'name': 'Individuals Itemized', 'number': '32-11(a i)'},
            {'name': 'Individuals Unitemized', 'number': '33-11(aii)'},
            {'name': 'Individual Contribution Total', 'number': '34-11(aiii)'},
            {'name': 'Political Party Committees', 'number': '35-11(b)'},
            {'name': 'Other Political Committees', 'number': '36-11(c)'},
            {'name': 'The Candidate', 'number': '37-11(d)'},
            {'name': 'Total Contributions', 'number': '38-11(e)'},
            {'name': 'TransfersFrom Other Authorized Committees', 'number': '39-12'},
            {'name': 'Loans made or guarnby the Candidate', 'number': '40-13(a)'},
            {'name': 'All Other Loans', 'number': '41-13(b)'},
            {'name': 'Total Loans', 'number': '42-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '43-14'},
            {'name': 'Other Receipts', 'number': '44-15'},
            {'name': 'Total Receipts', 'number': '45-16'},
            {'name': 'Operating Expenditures', 'number': '46-17'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '47-18'},
            {'name': 'Of Loans made or guarby the Candidate', 'number': '48-19(a)'},
            {'name': 'Loan Repayments, All Other Loans', 'number': '49-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '50-19(c)'},
            {'name': 'Refund/Individuals Other than PolCmtes', 'number': '51-20(a)'},
            {'name': 'Refund/Political Party Committees', 'number': '52-20(b)'},
            {'name': 'Refund/Other Political Committees', 'number': '53-20(c)'},
            {'name': 'Total Contribution Refunds', 'number': '54-20(d)'},
            {'name': 'Other Disbursements', 'number': '55-21'},
            {'name': 'Total Disbursements', 'number': '56-22'},
            {'name': 'Cash Beginning Reporting Period', 'number': '57-23'},
            {'name': 'Total Receipts this Period', 'number': '58-24'},
            {'name': 'SubTotal)', 'number': '59-25'},
            {'name': 'Total Disbursements this Period', 'number': '60-26'},
            {'name': 'Cash on hand at Close Period', 'number': '61-27'},
            {'name': 'Total Contributions (No Loans)', 'number': '62-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '63-(6b)'},
            {'name': 'Net Contributions', 'number': '64-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '65-(7a)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '66-(7b)'},
            {'name': 'NET Operating Expenditures', 'number': '67-(7c)'},
            {'name': 'Individuals Itemized', 'number': '68-11(ai)'},
            {'name': 'Individuals Unitemized', 'number': '69-11(aii)'},
            {'name': 'Individuals Total', 'number': '70-11(aiii)'},
            {'name': 'Political Party Committees', 'number': '71-11(b)'},
            {'name': 'All Other Political Committees (PACS)', 'number': '72-11(c)'},
            {'name': 'The Candidate', 'number': '73-11(d)'},
            {'name': 'Total Contributions', 'number': '74-11(e)'},
            {'name': 'Transfers From Other AUTH Committees', 'number': '75-12'},
            {'name': 'Loans made or guarnby the Candidate', 'number': '76-13(a)'},
            {'name': 'All Other Loans', 'number': '77-13(b)'},
            {'name': 'Total Loans', 'number': '78-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '79-14'},
            {'name': 'Other Receipts', 'number': '80-15'},
            {'name': 'Total Receipts', 'number': '81-16'},
            {'name': 'Operating Expenditures', 'number': '82-17'},
            {'name': 'Transfers To Other AUTH Committees', 'number': '83-18'},
            {'name': 'Loan Repayment By Candidate', 'number': '84-19(a)'},
            {'name': 'Loan Repayments,ALL Other Loans', 'number': '85-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '86-19(c)'},
            {'name': 'Refund/Individuals Other than PolCmtes', 'number': '87-20(a)'},
            {'name': 'Refund, Political Party Committees', 'number': '88-20(b)'},
            {'name': 'Refund, Other Political Committees', 'number': '89-20(c)'},
            {'name': 'Total Contributions Refunds', 'number': '90-20(d)'},
            {'name': 'Other Disbursements', 'number': '91-21'},
            {'name': 'Total Disbursements', 'number': '92-22'},
            {'name': 'Treasurer', 'number': '93-'},
            {'name': 'Signed', 'number': '94-'},
    ]
        self.fields_names = self.hash_names(self.fields)
