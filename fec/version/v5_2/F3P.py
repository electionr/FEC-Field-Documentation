import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEENAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'CHG OF ADDRESS', 'number': '9'},
            {'name': 'ACTIVITY PRIMARY', 'number': '10'},
            {'name': 'ACTIVITY GENERAL', 'number': '11'},
            {'name': 'RPTCODE', 'number': '12'},
            {'name': 'RPTPGI', 'number': '13'},
            {'name': 'Of Election', 'number': '14-'},
            {'name': 'STATE (Of Election)', 'number': '15'},
            {'name': 'Coverage From', 'number': '16-'},
            {'name': 'Coverage To', 'number': '17-'},
            {'name': 'Cash on Hand Beginning Period', 'number': '18-6.'},
            {'name': 'Total Receipts', 'number': '19-7.'},
            {'name': 'SubTotal', 'number': '20-8.'},
            {'name': 'Total Disbursements', 'number': '21-9.'},
            {'name': 'Cash on Hand Close of Period', 'number': '22-10.'},
            {'name': 'Debts to', 'number': '23-11.'},
            {'name': 'Debts by', 'number': '24-12.'},
            {'name': 'Expenditures Subject to Limits', 'number': '25-13.'},
            {'name': 'Net Contributions', 'number': '26-14.'},
            {'name': 'Net Operating Expenditures', 'number': '27-15.'},
            {'name': 'Federal Funds', 'number': '28-16.'},
            {'name': 'Individuals', 'number': '29-17(a)'},
            {'name': 'Political Party Committees', 'number': '30-17(b)'},
            {'name': 'Other Political Committees (PACs)', 'number': '31-17(c)'},
            {'name': 'The Candidate', 'number': '32-17(d)'},
            {'name': 'Total Contributions', 'number': '33-17(e)'},
            {'name': 'Transfers From Aff/Other Party Committees', 'number': '34-18.'},
            {'name': 'Received from or Guaranteed by Candidate', 'number': '35-19(a)'},
            {'name': 'Other Loans', 'number': '36-19(b)'},
            {'name': 'Total Loans', 'number': '37-19(c)'},
            {'name': 'Operating', 'number': '38-20(a)'},
            {'name': 'Fundraising', 'number': '39-20(b)'},
            {'name': 'Legal and Accounting', 'number': '40-20(c)'},
            {'name': 'Total offsets to Expenditures', 'number': '41-20(d)'},
            {'name': 'Other Receipts', 'number': '42-21.'},
            {'name': 'Total Receipts', 'number': '43-22.'},
            {'name': 'Operating Expenditures', 'number': '44-23.'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '45-24.'},
            {'name': 'Fundraising Disbursements', 'number': '46-25.'},
            {'name': 'Exempt Legal and Accounting Disbursements', 'number': '47-26.'},
            {'name': 'Made or guaranteed by Candidate', 'number': '48-27(a)'},
            {'name': 'Other Repayments', 'number': '49-27(b)'},
            {'name': 'Total Loan Repayments Made', 'number': '50-27(c)'},
            {'name': 'Individuals', 'number': '51-28(a)'},
            {'name': 'Political Party Committees', 'number': '52-28(b)'},
            {'name': 'Other Political Committees', 'number': '53-28(c)'},
            {'name': 'Total Contributions Refunds', 'number': '54-28(d)'},
            {'name': 'Other Disbursements', 'number': '55-29.'},
            {'name': 'Total Disbursements', 'number': '56-30.'},
            {'name': 'Items on Hand to be Liquidated', 'number': '57-31.'},
            {'name': 'ALABAMA', 'number': '58'},
            {'name': 'ALASKA', 'number': '59'},
            {'name': 'ARIZONA', 'number': '60'},
            {'name': 'ARKANSAS', 'number': '61'},
            {'name': 'CALIFORNIA', 'number': '62'},
            {'name': 'COLORADO', 'number': '63'},
            {'name': 'CONNECTICUT', 'number': '64'},
            {'name': 'DELAWARE', 'number': '65'},
            {'name': 'DIST OF COLUMBIA', 'number': '66'},
            {'name': 'FLORIDA', 'number': '67'},
            {'name': 'GEORGIA', 'number': '68'},
            {'name': 'HAWAII', 'number': '69'},
            {'name': 'IDAHO', 'number': '70'},
            {'name': 'ILLINOIS', 'number': '71'},
            {'name': 'INDIANA', 'number': '72'},
            {'name': 'IOWA', 'number': '73'},
            {'name': 'KANSAS', 'number': '74'},
            {'name': 'KENTUCKY', 'number': '75'},
            {'name': 'LOUISIANA', 'number': '76'},
            {'name': 'MAINE', 'number': '77'},
            {'name': 'MARYLAND', 'number': '78'},
            {'name': 'MASSACHUSETTS', 'number': '79'},
            {'name': 'MICHIGAN', 'number': '80'},
            {'name': 'MINNESOTA', 'number': '81'},
            {'name': 'MISSISSIPPI', 'number': '82'},
            {'name': 'MISSOURI', 'number': '83'},
            {'name': 'MONTANA', 'number': '84'},
            {'name': 'NEBRASKA', 'number': '85'},
            {'name': 'NEVADA', 'number': '86'},
            {'name': 'NEW HAMPSHIRE', 'number': '87'},
            {'name': 'NEW JERSEY', 'number': '88'},
            {'name': 'NEW MEXICO', 'number': '89'},
            {'name': 'NEW YORK', 'number': '90'},
            {'name': 'NORTH CAROLINA', 'number': '91'},
            {'name': 'NORTH DAKOTA', 'number': '92'},
            {'name': 'OHIO', 'number': '93'},
            {'name': 'OKLAHOMA', 'number': '94'},
            {'name': 'OREGON', 'number': '95'},
            {'name': 'PENNSYLVANIA', 'number': '96'},
            {'name': 'RHODE ISLAND', 'number': '97'},
            {'name': 'SOUTH CAROLINA', 'number': '98'},
            {'name': 'SOUTH DAKOTA', 'number': '99'},
            {'name': 'TENNESSEE', 'number': '100'},
            {'name': 'TEXAS', 'number': '101'},
            {'name': 'UTAH', 'number': '102'},
            {'name': 'VERMONT', 'number': '103'},
            {'name': 'VIRGINIA', 'number': '104'},
            {'name': 'WASHINGTON', 'number': '105'},
            {'name': 'WEST VIRGINIA', 'number': '106'},
            {'name': 'WISCONSIN', 'number': '107'},
            {'name': 'WYOMING', 'number': '108'},
            {'name': 'PUERTO RICO', 'number': '109'},
            {'name': 'GUAM', 'number': '110'},
            {'name': 'VIRGIN ISLANDS', 'number': '111'},
            {'name': 'TOTALS', 'number': '112'},
            {'name': 'Federal Funds', 'number': '113-16.'},
            {'name': 'Individuals', 'number': '114-17(a)'},
            {'name': 'Political Party Committees', 'number': '115-17(b)'},
            {'name': 'Other Political Committees (PACs)', 'number': '116-17(c)'},
            {'name': 'The Candidate', 'number': '117-17(d)'},
            {'name': 'Total contributions (Other than Loans)', 'number': '118-17(e)'},
            {'name': 'Transfers From Aff/Other Party Committees', 'number': '119-18.'},
            {'name': 'Received from or Guaranteed by Candidate', 'number': '120-19(a)'},
            {'name': 'Other Loans', 'number': '121-19(b)'},
            {'name': 'Total Loans', 'number': '122-19(c)'},
            {'name': 'Operating', 'number': '123-20(a)'},
            {'name': 'Fundraising', 'number': '124-20(b)'},
            {'name': 'Legal and Accounting', 'number': '125-20(c)'},
            {'name': 'Total Offsets to Operating Expenditures', 'number': '126-20(d)'},
            {'name': 'Other Receipts', 'number': '127-21.'},
            {'name': 'Total Receipts', 'number': '128-22.'},
            {'name': 'Operating Expenditures', 'number': '129-23.'},
            {'name': 'Transfers to Other Authorized Committees', 'number': '130-24.'},
            {'name': 'Fundraising Disbursements', 'number': '131-25.'},
            {'name': 'Exempt Legal and Accounting Disbursements', 'number': '132-26.'},
            {'name': 'Made or Guaranteed by the Candidate', 'number': '133-27(a)'},
            {'name': 'Other Repayments', 'number': '134-27(b)'},
            {'name': 'Total Loan Repayments Made', 'number': '135-27(c)'},
            {'name': 'Individuals', 'number': '136-28(a)'},
            {'name': 'Political Party Committees', 'number': '137-28(b)'},
            {'name': 'Other Political Committees', 'number': '138-28(c)'},
            {'name': 'Total Contributions Refunds', 'number': '139-28(d)'},
            {'name': 'Other Disbursements', 'number': '140-29.'},
            {'name': 'Total Disbursements', 'number': '141-30.'},
            {'name': 'ALABAMA', 'number': '142'},
            {'name': 'ALASKA', 'number': '143'},
            {'name': 'ARIZONA', 'number': '144'},
            {'name': 'ARKANSAS', 'number': '145'},
            {'name': 'CALIFORNIA', 'number': '146'},
            {'name': 'COLORADO', 'number': '147'},
            {'name': 'CONNECTICUT', 'number': '148'},
            {'name': 'DELAWARE', 'number': '149'},
            {'name': 'DIST OF COLUMBIA', 'number': '150'},
            {'name': 'FLORIDA', 'number': '151'},
            {'name': 'GEORGIA', 'number': '152'},
            {'name': 'HAWAII', 'number': '153'},
            {'name': 'IDAHO', 'number': '154'},
            {'name': 'ILLINOIS', 'number': '155'},
            {'name': 'INDIANA', 'number': '156'},
            {'name': 'IOWA', 'number': '157'},
            {'name': 'KANSAS', 'number': '158'},
            {'name': 'KENTUCKY', 'number': '159'},
            {'name': 'LOUISIANA', 'number': '160'},
            {'name': 'MAINE', 'number': '161'},
            {'name': 'MARYLAND', 'number': '162'},
            {'name': 'MASSACHUSETTS', 'number': '163'},
            {'name': 'MICHIGAN', 'number': '164'},
            {'name': 'MINNESOTA', 'number': '165'},
            {'name': 'MISSISSIPPI', 'number': '166'},
            {'name': 'MISSOURI', 'number': '167'},
            {'name': 'MONTANA', 'number': '168'},
            {'name': 'NEBRASKA', 'number': '169'},
            {'name': 'NEVADA', 'number': '170'},
            {'name': 'NEW HAMPSHIRE', 'number': '171'},
            {'name': 'NEW JERSEY', 'number': '172'},
            {'name': 'NEW MEXICO', 'number': '173'},
            {'name': 'NEW YORK', 'number': '174'},
            {'name': 'NORTH CAROLINA', 'number': '175'},
            {'name': 'NORTH DAKOTA', 'number': '176'},
            {'name': 'OHIO', 'number': '177'},
            {'name': 'OKLAHOMA', 'number': '178'},
            {'name': 'OREGON', 'number': '179'},
            {'name': 'PENNSYLVANIA', 'number': '180'},
            {'name': 'RHODE ISLAND', 'number': '181'},
            {'name': 'SOUTH CAROLINA', 'number': '182'},
            {'name': 'SOUTH DAKOTA', 'number': '183'},
            {'name': 'TENNESSEE', 'number': '184'},
            {'name': 'TEXAS', 'number': '185'},
            {'name': 'UTAH', 'number': '186'},
            {'name': 'VERMONT', 'number': '187'},
            {'name': 'VIRGINIA', 'number': '188'},
            {'name': 'WASHINGTON', 'number': '189'},
            {'name': 'WEST VIRGINIA', 'number': '190'},
            {'name': 'WISCONSIN', 'number': '191'},
            {'name': 'WYOMING', 'number': '192'},
            {'name': 'PUERTO RICO', 'number': '193'},
            {'name': 'GUAM', 'number': '194'},
            {'name': 'VIRGIN ISLANDS', 'number': '195'},
            {'name': 'TOTALS', 'number': '196'},
            {'name': 'NAME/TREASURER (as signed)', 'number': '197'},
            {'name': 'Signed', 'number': '198-'},
    ]
        self.fields_names = self.hash_names(self.fields)
