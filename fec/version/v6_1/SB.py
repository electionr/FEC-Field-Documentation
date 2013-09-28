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
            {'name': 'EXPENDITURE PURPOSE CODE', 'number': '22'},
            {'name': 'EXPENDITURE PURPOSE DESCRIP', 'number': '23'},
            {'name': 'CATEGORY CODE', 'number': '24'},
            {'name': 'REFUND OR DISPOSAL OF EXCESS', 'number': '25'},
            {'name': 'COMMUNICATION DATE', 'number': '26'},
            {'name': 'PAYEE COMMITTEE FEC ID', 'number': '27'},
            {'name': 'PAYEE CANDIDATE FEC ID', 'number': '28'},
            {'name': 'PAYEE CANDIDATE LAST NAME', 'number': '29'},
            {'name': 'PAYEE CANDIDATE FIRST NAME', 'number': '30'},
            {'name': 'PAYEE CANDIDATE MIDDLE NAME', 'number': '31'},
            {'name': 'PAYEE CANDIDATE PREFIX', 'number': '32'},
            {'name': 'PAYEE CANDIDATE SUFFIX', 'number': '33'},
            {'name': 'PAYEE CANDIDATE OFFICE', 'number': '34'},
            {'name': 'PAYEE CANDIDATE STATE', 'number': '35'},
            {'name': 'PAYEE CANDIDATE DISTRICT', 'number': '36'},
            {'name': 'CONDUIT NAME', 'number': '37'},
            {'name': 'CONDUIT STREET 1', 'number': '38'},
            {'name': 'CONDUIT STREET 2', 'number': '39'},
            {'name': 'CONDUIT CITY', 'number': '40'},
            {'name': 'CONDUIT STATE', 'number': '41'},
            {'name': 'CONDUIT ZIP', 'number': '42'},
            {'name': 'MEMO CODE', 'number': '43'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '44'},
            {'name': 'Reference to SI or SL system code that identifies the Account', 'number': '45'},
    ]
        self.fields_names = self.hash_names(self.fields)
