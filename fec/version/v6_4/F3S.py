import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'Date - General Election', 'number': '3'},
            {'name': 'Date - Day after General Election', 'number': '4'},
            {'name': 'Total Contributions (No Loans)', 'number': '5-(6a)'},
            {'name': 'Total Contribution Refunds', 'number': '6-(6b)'},
            {'name': 'Net Contributions', 'number': '7-(6c)'},
            {'name': 'Total Operating Expenditures', 'number': '8-(7a)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '9-(7b)'},
            {'name': 'NET Operating Expenditures.', 'number': '10-(7c)'},
            {'name': 'Individuals Itemized', 'number': '11-11(a i.)'},
            {'name': 'Individuals Unitemized', 'number': '12-11(a.ii)'},
            {'name': 'Individuals Total', 'number': '13-11(a.iii)'},
            {'name': 'Political Party Committees', 'number': '14-11(b)'},
            {'name': 'All Other Political Committees (PACS)', 'number': '15-11(c)'},
            {'name': 'The Candidate', 'number': '16-11(d)'},
            {'name': 'Total Contributions', 'number': '17-11(e)'},
            {'name': 'Transfers From Other AUTH Committees', 'number': '18-12.'},
            {'name': 'Loans made or guarn. by the Candidate', 'number': '19-13(a)'},
            {'name': 'All Other Loans', 'number': '20-13(b)'},
            {'name': 'Total Loans', 'number': '21-13(c)'},
            {'name': 'Offsets to Operating Expenditures', 'number': '22-14.'},
            {'name': 'Other Receipts', 'number': '23-15.'},
            {'name': 'Total Receipts', 'number': '24-16.'},
            {'name': 'Operating Expenditures', 'number': '25-17'},
            {'name': 'Transfers To Other AUTH Committees', 'number': '26-18.'},
            {'name': 'Loan Repayment By Candidate', 'number': '27-19(a)'},
            {'name': 'Loan Repayments, ALL Other Loans', 'number': '28-19(b)'},
            {'name': 'Total Loan Repayments', 'number': '29-19(c)'},
            {'name': 'Refund/Individuals Other than Pol. Cmtes', 'number': '30-20(a)'},
            {'name': 'Refund, Political Party Committees', 'number': '31-20(b)'},
            {'name': 'Refund, Other Political Committees', 'number': '32-20(c)'},
            {'name': 'Total Contributions Refunds', 'number': '33-20(d)'},
            {'name': 'Other Disbursements', 'number': '34-21.'},
            {'name': 'Total Disbursements', 'number': '35-22.'},
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'Date - General Election', 'number': '3'},
            {'name': 'Date - Day after General Election', 'number': '4'},
            {'name': 'Net Contributions', 'number': '5-14.'},
            {'name': 'Net Expenditures', 'number': '6-15.'},
            {'name': 'Federal Funds', 'number': '7-16.'},
            {'name': 'Individuals', 'number': '8-17(a)'},
            {'name': 'Political Party Committees', 'number': '9-17(b)'},
            {'name': 'Other Political Committees (PACs)', 'number': '10-17(c)'},
            {'name': 'The Candidate', 'number': '11-17(d)'},
            {'name': 'Total contributions (Other than Loans)', 'number': '12-17(e)'},
            {'name': 'Transfers From Aff/Other Party Committees', 'number': '13-18.'},
            {'name': 'Received from or Guaranteed by Candidate', 'number': '14-19(a)'},
            {'name': 'Other Loans', 'number': '15-19(b)'},
            {'name': 'Total Loans', 'number': '16-19(c)'},
            {'name': 'Operating', 'number': '17-20(a)'},
            {'name': 'Fundraising', 'number': '18-20(b)'},
            {'name': 'Legal and Accounting', 'number': '19-20(c)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '20-20(d)'},
            {'name': 'Other Receipts', 'number': '21-21.'},
            {'name': 'Total Receipts', 'number': '22-22.'},
            {'name': 'Operating Expenditures', 'number': '23-23.'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '24-24.'},
            {'name': 'Fundraising Disbursements', 'number': '25-25.'},
            {'name': 'Exempt Legal and Accounting Disbursements', 'number': '26-26.'},
            {'name': 'Made or Guaranteed by the Candidate', 'number': '27-27(a)'},
            {'name': 'Other Repayments', 'number': '28-27(b)'},
            {'name': 'Total Loan Repayments Made', 'number': '29-27(c)'},
            {'name': 'Individuals', 'number': '30-28(a)'},
            {'name': 'Political Party Committees', 'number': '31-28(b)'},
            {'name': 'Other Political Committees', 'number': '32-28(c)'},
            {'name': 'Total Contributions Refunds', 'number': '33-28(d)'},
            {'name': 'Other Disbursements', 'number': '34-29.'},
            {'name': 'Total Disbursements', 'number': '35-30.'},
            {'name': 'ALABAMA', 'number': '36'},
            {'name': 'ALASKA', 'number': '37'},
            {'name': 'ARIZONA', 'number': '38'},
            {'name': 'ARKANSAS', 'number': '39'},
            {'name': 'CALIFORNIA', 'number': '40'},
            {'name': 'COLORADO', 'number': '41'},
            {'name': 'CONNECTICUT', 'number': '42'},
            {'name': 'DELAWARE', 'number': '43'},
            {'name': 'DIST OF COLUMBIA', 'number': '44'},
            {'name': 'FLORIDA', 'number': '45'},
            {'name': 'GEORGIA', 'number': '46'},
            {'name': 'HAWAII', 'number': '47'},
            {'name': 'IDAHO', 'number': '48'},
            {'name': 'ILLINOIS', 'number': '49'},
            {'name': 'INDIANA', 'number': '50'},
            {'name': 'IOWA', 'number': '51'},
            {'name': 'KANSAS', 'number': '52'},
            {'name': 'KENTUCKY', 'number': '53'},
            {'name': 'LOUISIANA', 'number': '54'},
            {'name': 'MAINE', 'number': '55'},
            {'name': 'MARYLAND', 'number': '56'},
            {'name': 'MASSACHUSETTS', 'number': '57'},
            {'name': 'MICHIGAN', 'number': '58'},
            {'name': 'MINNESOTA', 'number': '59'},
            {'name': 'MISSISSIPPI', 'number': '60'},
            {'name': 'MISSOURI', 'number': '61'},
            {'name': 'MONTANA', 'number': '62'},
            {'name': 'NEBRASKA', 'number': '63'},
            {'name': 'NEVADA', 'number': '64'},
            {'name': 'NEW HAMPSHIRE', 'number': '65'},
            {'name': 'NEW JERSEY', 'number': '66'},
            {'name': 'NEW MEXICO', 'number': '67'},
            {'name': 'NEW YORK', 'number': '68'},
            {'name': 'NORTH CAROLINA', 'number': '69'},
            {'name': 'NORTH DAKOTA', 'number': '70'},
            {'name': 'OHIO', 'number': '71'},
            {'name': 'OKLAHOMA', 'number': '72'},
            {'name': 'OREGON', 'number': '73'},
            {'name': 'PENNSYLVANIA', 'number': '74'},
            {'name': 'RHODE ISLAND', 'number': '75'},
            {'name': 'SOUTH CAROLINA', 'number': '76'},
            {'name': 'SOUTH DAKOTA', 'number': '77'},
            {'name': 'TENNESSEE', 'number': '78'},
            {'name': 'TEXAS', 'number': '79'},
            {'name': 'UTAH', 'number': '80'},
            {'name': 'VERMONT', 'number': '81'},
            {'name': 'VIRGINIA', 'number': '82'},
            {'name': 'WASHINGTON', 'number': '83'},
            {'name': 'WEST VIRGINIA', 'number': '84'},
            {'name': 'WISCONSIN', 'number': '85'},
            {'name': 'WYOMING', 'number': '86'},
            {'name': 'PUERTO RICO', 'number': '87'},
            {'name': 'GUAM', 'number': '88'},
            {'name': 'VIRGIN ISLANDS', 'number': '89'},
            {'name': 'TOTALS', 'number': '90'},
    ]
        self.fields_names = self.hash_names(self.fields)
