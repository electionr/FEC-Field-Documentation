from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'NAME OF ACCOUNT', 'number': '3'},
            {'name': 'System code for account named in Field #3', 'number': '4'},
            {'name': 'Coverage From', 'number': '5-'},
            {'name': 'Coverage To', 'number': '6-'},
            {'name': 'Itemized Receipts From Persons', 'number': '7-1a.'},
            {'name': 'Unitemized Receipts From Persons', 'number': '8-1b.'},
            {'name': 'Total Receipts From Persons', 'number': '9-1c.'},
            {'name': 'Other Receipts', 'number': '10-2.'},
            {'name': 'Total Receipts', 'number': '11-3.'},
            {'name': 'Voter Registration DISBURSEMENTS', 'number': '12-4(a).'},
            {'name': 'Voter ID DISBURSEMENTS', 'number': '13-4(b).'},
            {'name': 'GOTV DISBURSEMENTS', 'number': '14-4(c).'},
            {'name': 'Generic Campaign DISBURSEMENTS', 'number': '15-4(d).'},
            {'name': 'Line 4 Total', 'number': '16-4(e)'},
            {'name': 'Other Disbursements', 'number': '17-5.'},
            {'name': 'Total Disbursements', 'number': '18-6.'},
            {'name': 'Cash on Hand beginning', 'number': '19-7.'},
            {'name': 'Receipts', 'number': '20-8.'},
            {'name': 'Subtotal', 'number': '21-9.'},
            {'name': 'Disbursements', 'number': '22-10.'},
            {'name': 'Itemized Receipts From Persons', 'number': '23-1a.'},
            {'name': 'Unitemized Receipts From Persons', 'number': '24-1b.'},
            {'name': 'Total Receipts From Persons', 'number': '25-1c.'},
            {'name': 'Other Receipts', 'number': '26-2.'},
            {'name': 'Total Receipts', 'number': '27-3.'},
            {'name': 'Voter Registration DISBURSEMENTS', 'number': '28-4(a).'},
            {'name': 'Voter ID DISBURSEMENTS', 'number': '29-4(b).'},
            {'name': 'GOTV DISBURSEMENTS', 'number': '30-4(c).'},
            {'name': 'Generic Campaign DISBURSEMENTS', 'number': '31-4(d).'},
            {'name': 'Line 4 Total', 'number': '32-4(e)'},
            {'name': 'Other Disbursements', 'number': '33-5.'},
            {'name': 'Total Disbursements', 'number': '34-6.'},
            {'name': 'Cash on Hand Jan 1, 19', 'number': '35-7.'},
            {'name': 'Receipts', 'number': '36-8.'},
            {'name': 'Subtotal', 'number': '37-9.'},
            {'name': 'Disbursements', 'number': '38-10.'},
            {'name': 'ENDING CASH ON HAND', 'number': '39-11.'},
            {'name': 'AMENDED CODE', 'number': '40'},
            {'name': 'TRAN ID', 'number': '41'},
    ]