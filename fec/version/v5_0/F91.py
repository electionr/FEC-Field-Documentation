import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'Share/Exer Control', 'number': '3-'},
            {'name': 'STREET 1', 'number': '4'},
            {'name': 'STREET 2', 'number': '5'},
            {'name': 'CITY', 'number': '6'},
            {'name': 'STATE', 'number': '7'},
            {'name': 'ZIP', 'number': '8'},
            {'name': 'EMPLOYER', 'number': '9'},
            {'name': 'OCCUPATION', 'number': '10'},
            {'name': 'AMENDED CD', 'number': '11'},
            {'name': 'TRAN ID', 'number': '12'},
    ]
        self.fields_names = self.hash_names(self.fields)
