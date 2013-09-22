from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'DATE OF EXPENDITURE', 'number': '3'},
            {'name': 'ITEM ELECT CD', 'number': '4'},
            {'name': 'ITEM ELECT OTHER', 'number': '5'},
            {'name': 'AMOUNT', 'number': '6'},
            {'name': 'LOAN CHECK', 'number': '7'},
            {'name': 'AMENDED CD', 'number': '8'},
            {'name': 'TRAN ID', 'number': '9'},
    ]