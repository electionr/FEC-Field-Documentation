import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'CONTRIBUTOR NAME', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'ITEM ELECT CD', 'number': '10'},
            {'name': 'ITEM ELECT OTHER', 'number': '11'},
            {'name': 'INDEMP', 'number': '12'},
            {'name': 'INDOCC', 'number': '13'},
            {'name': 'AGGREGATE AMT Y-T-D', 'number': '14'},
            {'name': 'DATE RECEIVED', 'number': '15'},
            {'name': 'AMOUNT RECEIVED', 'number': '16'},
            {'name': 'TRANS CODE', 'number': '17'},
            {'name': 'SPACE HOLDER', 'number': '18'},
            {'name': 'SPACE HOLDER', 'number': '19'},
            {'name': 'SPACE HOLDER', 'number': '20'},
            {'name': 'SPACE HOLDER', 'number': '21'},
            {'name': 'SPACE HOLDER', 'number': '22'},
            {'name': 'SPACE HOLDER', 'number': '23'},
            {'name': 'SPACE HOLDER', 'number': '24'},
            {'name': 'SPACE HOLDER', 'number': '25'},
            {'name': 'SPACE HOLDER', 'number': '26'},
            {'name': 'SPACE HOLDER', 'number': '27'},
            {'name': 'SPACE HOLDER', 'number': '28'},
            {'name': 'SPACE HOLDER', 'number': '29'},
            {'name': 'SPACE HOLDER', 'number': '30'},
            {'name': 'SPACE HOLDER', 'number': '31'},
            {'name': 'SPACE HOLDER', 'number': '32'},
            {'name': 'SPACE HOLDER', 'number': '33'},
            {'name': 'TRAN ID', 'number': '34'},
            {'name': 'BACK REF TRAN ID', 'number': '35'},
            {'name': 'BACK REF SCHED NAME', 'number': '36'},
            {'name': 'SPACE HOLDER', 'number': '37'},
            {'name': 'SPACE HOLDER', 'number': '38'},
            {'name': 'CONTRIB ORGANIZATION NAME', 'number': '39'},
            {'name': 'CONTRIBUTOR LAST NAME', 'number': '40'},
            {'name': 'CONTRIBUTOR FIRST NAME', 'number': '41'},
            {'name': 'CONTRIBUTOR MIDDLE NAME', 'number': '42'},
            {'name': 'CONTRIBUTOR PREFIX', 'number': '43'},
            {'name': 'CONTRIBUTOR SUFFIX', 'number': '44'},
    ]
        self.fields_names = self.hash_names(self.fields)
