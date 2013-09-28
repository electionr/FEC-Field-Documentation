import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID', 'number': '3'},
            {'name': 'BACK REFERENCE TRAN ID NUMBER', 'number': '4'},
            {'name': 'BACK REFERENCE SCHED NAME', 'number': '5'},
            {'name': 'ENTITY TYPE', 'number': '6'},
            {'name': 'CONTRIBUTOR ORGANIZATION NAME', 'number': '7'},
            {'name': 'CONTRIBUTOR LAST NAME', 'number': '8'},
            {'name': 'CONTRIBUTOR FIRST NAME', 'number': '9'},
            {'name': 'CONTRIBUTOR MIDDLE NAME', 'number': '10'},
            {'name': 'CONTRIBUTOR PREFIX', 'number': '11'},
            {'name': 'CONTRIBUTOR SUFFIX', 'number': '12'},
            {'name': 'CONTRIBUTOR STREET 1', 'number': '13'},
            {'name': 'CONTRIBUTOR STREET 2', 'number': '14'},
            {'name': 'CONTRIBUTOR CITY', 'number': '15'},
            {'name': 'CONTRIBUTOR STATE', 'number': '16'},
            {'name': 'CONTRIBUTOR ZIP', 'number': '17'},
            {'name': 'ELECTION CODE', 'number': '18'},
            {'name': 'ELECTION OTHER DESCRIPTION', 'number': '19'},
            {'name': 'CONTRIBUTION DATE', 'number': '20'},
            {'name': 'CONTRIBUTION AMOUNT (F3L Bundled)', 'number': '21'},
            {'name': 'CONTRIBUTION AGGREGATE F3L Semi-annual Bundled', 'number': '22'},
            {'name': 'CONTRIBUTION PURPOSE DESCRIP', 'number': '23'},
            {'name': 'CONTRIBUTOR EMPLOYER', 'number': '24'},
            {'name': 'CONTRIBUTOR OCCUPATION', 'number': '25'},
            {'name': 'DONOR COMMITTEE FEC ID', 'number': '26'},
            {'name': 'DONOR COMMITTEE NAME', 'number': '27'},
            {'name': 'DONOR CANDIDATE FEC ID', 'number': '28'},
            {'name': 'DONOR CANDIDATE LAST NAME', 'number': '29'},
            {'name': 'DONOR CANDIDATE FIRST NAME', 'number': '30'},
            {'name': 'DONOR CANDIDATE MIDDLE NAME', 'number': '31'},
            {'name': 'DONOR CANDIDATE PREFIX', 'number': '32'},
            {'name': 'DONOR CANDIDATE SUFFIX', 'number': '33'},
            {'name': 'DONOR CANDIDATE OFFICE', 'number': '34'},
            {'name': 'DONOR CANDIDATE STATE', 'number': '35'},
            {'name': 'DONOR CANDIDATE DISTRICT', 'number': '36'},
            {'name': 'CONDUIT NAME', 'number': '37'},
            {'name': 'CONDUIT STREET1', 'number': '38'},
            {'name': 'CONDUIT STREET2', 'number': '39'},
            {'name': 'CONDUIT CITY', 'number': '40'},
            {'name': 'CONDUIT STATE', 'number': '41'},
            {'name': 'CONDUIT ZIP', 'number': '42'},
            {'name': 'MEMO CODE', 'number': '43'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '44'},
            {'name': 'Reference to SI or SL system code that identifies the Account', 'number': '45'},
    ]
        self.fields_names = self.hash_names(self.fields)
