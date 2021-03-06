import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'TRANSACTION ID NUMBER', 'number': '3'},
            {'name': 'ENTITY TYPE', 'number': '4'},
            {'name': 'CONTRIBUTOR ORGANIZATION NAME', 'number': '5'},
            {'name': 'CONTRIBUTOR LAST NAME', 'number': '6'},
            {'name': 'CONTRIBUTOR FIRST NAME', 'number': '7'},
            {'name': 'CONTRIBUTOR MIDDLE NAME', 'number': '8'},
            {'name': 'CONTRIBUTOR PREFIX', 'number': '9'},
            {'name': 'CONTRIBUTOR SUFFIX', 'number': '10'},
            {'name': 'CONTRIBUTOR STREET 1', 'number': '11'},
            {'name': 'CONTRIBUTOR STREET 2', 'number': '12'},
            {'name': 'CONTRIBUTOR CITY', 'number': '13'},
            {'name': 'CONTRIBUTOR STATE', 'number': '14'},
            {'name': 'CONTRIBUTOR ZIP', 'number': '15'},
            {'name': 'ELECTION CODE {was RPTPGI}', 'number': '16'},
            {'name': 'ITEM DESCRIPTION', 'number': '17'},
            {'name': 'ITEM CONTRIBUTION/AQUIRED DATE', 'number': '18'},
            {'name': 'ITEM FAIR MARKET VALUE', 'number': '19'},
            {'name': 'CONTRIBUTOR EMPLOYER', 'number': '20'},
            {'name': 'CONTRIBUTOR OCCUPATION', 'number': '21'},
            {'name': 'MEMO CODE', 'number': '22'},
            {'name': 'MEMO TEXT/DESCRIPTION', 'number': '23'},
    ]
        self.fields_names = self.hash_names(self.fields)
