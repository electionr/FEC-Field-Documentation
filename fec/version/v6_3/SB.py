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
            {'name': 'BENEFICIARY COMMITTEE FEC ID', 'number': '27'},
            {'name': 'BENEFICIARY COMMITTEE NAME', 'number': '28'},
            {'name': 'BENEFICIARY CANDIDATE FEC ID', 'number': '29'},
            {'name': 'BENEFICIARY CANDIDATE LAST NAME', 'number': '30'},
            {'name': 'BENEFICIARY CANDIDATE FIRST NAME', 'number': '31'},
            {'name': 'BENEFICIARY CANDIDATE MIDDLE NAME', 'number': '32'},
            {'name': 'BENEFICIARY CANDIDATE PREFIX', 'number': '33'},
            {'name': 'BENEFICIARY CANDIDATE SUFFIX', 'number': '34'},
            {'name': 'BENEFICIARY CANDIDATE OFFICE', 'number': '35'},
            {'name': 'BENEFICIARY CANDIDATE STATE', 'number': '36'},
            {'name': 'BENEFICIARY CANDIDATE DISTRICT', 'number': '37'},
            {'name': 'CONDUIT NAME', 'number': '38'},
            {'name': 'CONDUIT STREET 1', 'number': '39'},
            {'name': 'CONDUIT STREET 2', 'number': '40'},
            {'name': 'CONDUIT CITY', 'number': '41'},
            {'name': 'CONDUIT STATE', 'number': '42'},
            {'name': 'CONDUIT ZIP', 'number': '43'},
            {'name': 'MEMO CODE', 'number': '44'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '45'},
            {'name': 'Reference to SI or SL system code that identifies the Account', 'number': '46'},
    ]
        self.fields_names = self.hash_names(self.fields)
