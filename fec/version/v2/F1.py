import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'COMMITTEE NAME', 'number': '3'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'Submitted', 'number': '9-'},
            {'name': 'CHG OF COMMITTEE NAME', 'number': '10'},
            {'name': 'CHG OF ADDRESS', 'number': '11'},
            {'name': 'COMMITTEE TYPE', 'number': '12'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '13'},
            {'name': 'CANDIDATE NAME', 'number': '14'},
            {'name': 'CAN / OFFICE', 'number': '15'},
            {'name': 'CAN / STATE (of Election)', 'number': '16'},
            {'name': 'CAN / DISTRICT', 'number': '17'},
            {'name': 'PARTY CODE', 'number': '18'},
            {'name': 'PARTY TYPE', 'number': '19'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '20'},
            {'name': 'COMMITTEE NAME', 'number': '21'},
            {'name': 'STREET 1', 'number': '22'},
            {'name': 'STREET 2', 'number': '23'},
            {'name': 'CITY', 'number': '24'},
            {'name': 'STATE', 'number': '25'},
            {'name': 'ZIP', 'number': '26'},
            {'name': 'w/ Above Cmte)', 'number': '27'},
            {'name': 'ORGANIZATION', 'number': '28'},
            {'name': 'Custodian Name', 'number': '29-'},
            {'name': 'STREET 1', 'number': '30'},
            {'name': 'STREET 2', 'number': '31'},
            {'name': 'CITY', 'number': '32'},
            {'name': 'STATE', 'number': '33'},
            {'name': 'ZIP', 'number': '34'},
            {'name': 'TITLE', 'number': '35'},
            {'name': 'TELEPHONE', 'number': '36'},
            {'name': 'Treasurer', 'number': '37-'},
            {'name': 'STREET 1', 'number': '38'},
            {'name': 'STREET 2', 'number': '39'},
            {'name': 'CITY', 'number': '40'},
            {'name': 'STATE', 'number': '41'},
            {'name': 'ZIP', 'number': '42'},
            {'name': 'TITLE', 'number': '43'},
            {'name': 'TELEPHONE', 'number': '44'},
            {'name': 'Designated Agent', 'number': '45-'},
            {'name': 'STREET 1', 'number': '46'},
            {'name': 'STREET 2', 'number': '47'},
            {'name': 'CITY', 'number': '48'},
            {'name': 'STATE', 'number': '49'},
            {'name': 'ZIP', 'number': '50'},
            {'name': 'TITLE', 'number': '51'},
            {'name': 'TELEPHONE', 'number': '52'},
            {'name': 'Bank/Other', 'number': '53-'},
            {'name': 'STREET 1', 'number': '54'},
            {'name': 'STREET 2', 'number': '55'},
            {'name': 'CITY', 'number': '56'},
            {'name': 'STATE', 'number': '57'},
            {'name': 'ZIP', 'number': '58'},
            {'name': 'Treasurer', 'number': '59-'},
            {'name': 'Signed', 'number': '60-'},
    ]
        self.fields_names = self.hash_names(self.fields)
