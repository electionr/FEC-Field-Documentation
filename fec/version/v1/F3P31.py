import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'CONTRIB/LENDER', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'ITEM-PG', 'number': '9'},
            {'name': 'INDEMP', 'number': '10'},
            {'name': 'INDOCC', 'number': '11'},
            {'name': 'OF CONTRIBUTION', 'number': '12-'},
            {'name': 'FAIR MARKET VALUE OF ITEM', 'number': '13'},
            {'name': 'TRANSACTION CODE', 'number': '14'},
            {'name': 'TRANSDESC', 'number': '15'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '16'},
            {'name': 'COMMITTEE NAME', 'number': '17'},
            {'name': 'STREET 1', 'number': '18'},
            {'name': 'STREET 2', 'number': '19'},
            {'name': 'CITY', 'number': '20'},
            {'name': 'STATE', 'number': '21'},
            {'name': 'ZIP', 'number': '22'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '23'},
            {'name': 'CANDIDATE NAME', 'number': '24'},
            {'name': 'CAN/OFF', 'number': '25'},
            {'name': 'STATE (OF ELECTION)', 'number': '26'},
            {'name': 'CAN/DIST', 'number': '27'},
            {'name': 'MEMO CODE', 'number': '28'},
            {'name': 'MEMO-TEXT', 'number': '29'},
            {'name': 'AMENDED', 'number': '30'},
    ]
        self.fields_names = self.hash_names(self.fields)
