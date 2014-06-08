import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ENTITY TYPE', 'number': '4'},
            {'name': 'PAYEE ORGANIZATION NAME', 'number': '5'},
            {'name': 'PAYEE LAST NAME', 'number': '6'},
            {'name': 'PAYEE FIRST NAME', 'number': '7'},
            {'name': 'PAYEE MIDDLE NAME', 'number': '8'},
            {'name': 'PAYEE PREFIX', 'number': '9'},
            {'name': 'PAYEE SUFFIX', 'number': '10'},
            {'name': 'PAYEE STREET 1', 'number': '11'},
            {'name': 'PAYEE STREET 2', 'number': '12'},
            {'name': 'PAYEE CITY', 'number': '13'},
            {'name': 'PAYEE STATE', 'number': '14'},
            {'name': 'PAYEE ZIP', 'number': '15'},
            {'name': 'ELECTION CODE', 'number': '16'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '17'},
            {'name': 'EXPENDITURE DATE', 'number': '18'},
            {'name': 'EXPENDITURE AMOUNT', 'number': '19'},
            {'name': 'CALENDAR Y-T-D (per election/office)', 'number': '20'},
            {'name': 'EXPENDITURE PURPOSE CODE', 'number': '21'},
            {'name': 'EXPENDITURE PURPOSE DESCRIP', 'number': '22'},
            {'name': 'CATEGORY CODE', 'number': '23'},
            {'name': 'PAYEE CMTTE FEC ID NUMBER', 'number': '24'},
            {'name': 'SUPPORT/OPPOSE CODE', 'number': '25'},
            {'name': 'S/O CANDIDATE ID NUMBER', 'number': '26'},
            {'name': 'S/O CANDIDATE LAST NAME', 'number': '27'},
            {'name': 'S/O CANDIDATE FIRST NAME', 'number': '28'},
            {'name': 'S/O CANDINATE MIDDLE NAME', 'number': '29'},
            {'name': 'S/O CANDIDATE PREFIX', 'number': '30'},
            {'name': 'S/O CANDIDATE SUFFIX', 'number': '31'},
            {'name': 'S/O CANDIDATE OFFICE', 'number': '32'},
            {'name': 'S/O CANDIDATE STATE', 'number': '33'},
            {'name': 'S/O CANDIDATE DISTRICT', 'number': '34'},
    ]
        self.fields_names = self.hash_names(self.fields)
