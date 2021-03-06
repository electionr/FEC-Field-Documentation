import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'Date - General Election', 'number': '3'},
            {'name': 'Date - Day after General Election', 'number': '4'},
            {'name': 'Net Contributions', 'number': '5-14.'},
            {'name': 'Net Expenditures', 'number': '6-15.'},
            {'name': 'Federal Funds', 'number': '7-16.'},
            {'name': 'Individuals Itemized', 'number': '8-17(a.i)'},
            {'name': 'Individuals Unitemized', 'number': '9-17(a.ii)'},
            {'name': 'Individual Contribution Total', 'number': '10-17(a.iii)'},
            {'name': 'Political Party Committees', 'number': '11-17(b)'},
            {'name': 'Other Political Committees (PACs)', 'number': '12-17(c)'},
            {'name': 'The Candidate', 'number': '13-17(d)'},
            {'name': 'Total contributions  (Other than Loans)', 'number': '14-17(e)'},
            {'name': 'Transfers From Aff/Other Party Committees', 'number': '15-18.'},
            {'name': 'Received from or Guaranteed  by Candidate', 'number': '16-19(a)'},
            {'name': 'Other Loans', 'number': '17-19(b)'},
            {'name': 'Total Loans', 'number': '18-19(c)'},
            {'name': 'Operating', 'number': '19-20(a)'},
            {'name': 'Fundraising', 'number': '20-20(b)'},
            {'name': 'Legal and Accounting', 'number': '21-20(c)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '22-20(d)'},
            {'name': 'Other Receipts', 'number': '23-21.'},
            {'name': 'Total Receipts', 'number': '24-22.'},
            {'name': 'Operating Expenditures', 'number': '25-23.'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '26-24.'},
            {'name': 'Fundraising Disbursements', 'number': '27-25.'},
            {'name': 'Exempt Legal and Accounting Disbursements', 'number': '28-26.'},
            {'name': 'Made or Guaranteed by the Candidate', 'number': '29-27(a)'},
            {'name': 'Other Repayments', 'number': '30-27(b)'},
            {'name': 'Total Loan Repayments Made', 'number': '31-27(c)'},
            {'name': 'Individuals', 'number': '32-28(a)'},
            {'name': 'Political Party Committees', 'number': '33-28(b)'},
            {'name': 'Other Political Committees', 'number': '34-28(c)'},
            {'name': 'Total Contributions Refunds', 'number': '35-28(d)'},
            {'name': 'Other Disbursements', 'number': '36-29.'},
            {'name': 'Total Disbursements', 'number': '37-30.'},
            {'name': 'ALABAMA', 'number': '38'},
            {'name': 'ALASKA', 'number': '39'},
            {'name': 'ARIZONA', 'number': '40'},
            {'name': 'ARKANSAS', 'number': '41'},
            {'name': 'CALIFORNIA', 'number': '42'},
            {'name': 'COLORADO', 'number': '43'},
            {'name': 'CONNECTICUT', 'number': '44'},
            {'name': 'DELAWARE', 'number': '45'},
            {'name': 'DIST OF COLUMBIA', 'number': '46'},
            {'name': 'FLORIDA', 'number': '47'},
            {'name': 'GEORGIA', 'number': '48'},
            {'name': 'HAWAII', 'number': '49'},
            {'name': 'IDAHO', 'number': '50'},
            {'name': 'ILLINOIS', 'number': '51'},
            {'name': 'INDIANA', 'number': '52'},
            {'name': 'IOWA', 'number': '53'},
            {'name': 'KANSAS', 'number': '54'},
            {'name': 'KENTUCKY', 'number': '55'},
            {'name': 'LOUISIANA', 'number': '56'},
            {'name': 'MAINE', 'number': '57'},
            {'name': 'MARYLAND', 'number': '58'},
            {'name': 'MASSACHUSETTS', 'number': '59'},
            {'name': 'MICHIGAN', 'number': '60'},
            {'name': 'MINNESOTA', 'number': '61'},
            {'name': 'MISSISSIPPI', 'number': '62'},
            {'name': 'MISSOURI', 'number': '63'},
            {'name': 'MONTANA', 'number': '64'},
            {'name': 'NEBRASKA', 'number': '65'},
            {'name': 'NEVADA', 'number': '66'},
            {'name': 'NEW HAMPSHIRE', 'number': '67'},
            {'name': 'NEW JERSEY', 'number': '68'},
            {'name': 'NEW MEXICO', 'number': '69'},
            {'name': 'NEW YORK', 'number': '70'},
            {'name': 'NORTH CAROLINA', 'number': '71'},
            {'name': 'NORTH DAKOTA', 'number': '72'},
            {'name': 'OHIO', 'number': '73'},
            {'name': 'OKLAHOMA', 'number': '74'},
            {'name': 'OREGON', 'number': '75'},
            {'name': 'PENNSYLVANIA', 'number': '76'},
            {'name': 'RHODE ISLAND', 'number': '77'},
            {'name': 'SOUTH CAROLINA', 'number': '78'},
            {'name': 'SOUTH DAKOTA', 'number': '79'},
            {'name': 'TENNESSEE', 'number': '80'},
            {'name': 'TEXAS', 'number': '81'},
            {'name': 'UTAH', 'number': '82'},
            {'name': 'VERMONT', 'number': '83'},
            {'name': 'VIRGINIA', 'number': '84'},
            {'name': 'WASHINGTON', 'number': '85'},
            {'name': 'WEST VIRGINIA', 'number': '86'},
            {'name': 'WISCONSIN', 'number': '87'},
            {'name': 'WYOMING', 'number': '88'},
            {'name': 'PUERTO RICO', 'number': '89'},
            {'name': 'GUAM', 'number': '90'},
            {'name': 'VIRGIN ISLANDS', 'number': '91'},
            {'name': 'TOTALS', 'number': '92'},
    ]
        self.fields_names = self.hash_names(self.fields)
