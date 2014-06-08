import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID NUMBER', 'number': '4'},
            {'name': 'BACK REFERENCE SCHED NAME', 'number': '5'},
            {'name': 'ENTITY TYPE', 'number': '6'},
            {'name': 'PAYEE ORGANIZATION NAME', 'number': '7'},
            {'name': 'PAYEE LAST NAME', 'number': '8'},
            {'name': 'PAYEE FIRST NAME', 'number': '9'},
            {'name': 'PAYEE MIDDLE NAME', 'number': '10'},
            {'name': 'PAYEE PREFIX', 'number': '11'},
            {'name': 'PAYEE SUFFIX', 'number': '12'},
            {'name': 'PAYEE STREET 1', 'number': '13'},
            {'name': 'PAYEE STREET 2', 'number': '14'},
            {'name': 'PAYEE CITY', 'number': '15'},
            {'name': 'PAYEE STATE', 'number': '16'},
            {'name': 'PAYEE ZIP', 'number': '17'},
            {'name': 'ELECTION CODE', 'number': '18'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '19'},
            {'name': 'EXPENDITURE DATE', 'number': '20'},
            {'name': 'EXPENDITURE AMOUNT', 'number': '21'},
            {'name': 'CALENDAR Y-T-D (per election/office)', 'number': '22'},
            {'name': 'EXPENDITURE PURPOSE DESCRIP', 'number': '23'},
            {'name': 'CATEGORY CODE', 'number': '24'},
            {'name': 'PAYEE CMTTE FEC ID NUMBER', 'number': '25'},
            {'name': 'SUPPORT/OPPOSE CODE', 'number': '26'},
            {'name': 'S/O CANDIDATE ID NUMBER', 'number': '27'},
            {'name': 'S/O CANDIDATE LAST NAME', 'number': '28'},
            {'name': 'S/O CANDIDATE FIRST NAME', 'number': '29'},
            {'name': 'S/O CANDINATE MIDDLE NAME', 'number': '30'},
            {'name': 'S/O CANDIDATE PREFIX', 'number': '31'},
            {'name': 'S/O CANDIDATE SUFFIX', 'number': '32'},
            {'name': 'S/O CANDIDATE OFFICE', 'number': '33'},
            {'name': 'S/O CANDIDATE STATE', 'number': '34'},
            {'name': 'S/O CANDIDATE DISTRICT', 'number': '35'},
            {'name': 'COMPLETING LAST NAME', 'number': '36'},
            {'name': 'COMPLETING FIRST NAME', 'number': '37'},
            {'name': 'COMPLETING MIDDLE NAME', 'number': '38'},
            {'name': 'COMPLETING PREFIX', 'number': '39'},
            {'name': 'COMPLETING SUFFIX', 'number': '40'},
            {'name': 'DATE SIGNED', 'number': '41'},
            {'name': 'MEMO CODE', 'number': '42'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '43'},
    ]
        self.fields_names = self.hash_names(self.fields)
