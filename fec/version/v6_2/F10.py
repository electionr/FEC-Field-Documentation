import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'FILER {Principal Campaign} COMMITTEE NAME', 'number': '3'},
            {'name': 'COMMITTEE STREET 1', 'number': '4'},
            {'name': 'COMMITTEE STREET 2', 'number': '5'},
            {'name': 'COMMITTEE CITY', 'number': '6'},
            {'name': 'COMMITTEE STATE', 'number': '7'},
            {'name': 'COMMITTEE ZIP', 'number': '8'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '9'},
            {'name': 'CANDIDATE LAST NAME', 'number': '10'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '11'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '12'},
            {'name': 'CANDIDATE PREFIX', 'number': '13'},
            {'name': 'CANDIDATE SUFFIX', 'number': '14'},
            {'name': 'CANDIDATE OFFICE', 'number': '15'},
            {'name': 'CANDIDATE STATE', 'number': '16'},
            {'name': 'CANDIDATE DIST', 'number': '17'},
            {'name': 'PREVIOUS EXPENDITURE AGGREGATE', 'number': '18'},
            {'name': 'EXPENDITURE TOTAL THIS REPORT', 'number': '19'},
            {'name': 'EXPENDITURE TOTAL CYCLE-TO-DATE', 'number': '20'},
            {'name': 'MEETS F6 FILING FILING REQUIREMENTS', 'number': '21'},
            {'name': 'CANDIDATE EMPLOYER', 'number': '22'},
            {'name': 'CANDIDATE OCCUPATION', 'number': '23'},
            {'name': 'TREASURER LAST NAME', 'number': '24'},
            {'name': 'TREASURER FIRST NAME', 'number': '25'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '26'},
            {'name': 'TREASURER PREFIX', 'number': '27'},
            {'name': 'TREASURER SUFFIX', 'number': '28'},
            {'name': 'DATE SIGNED', 'number': '29'},
    ]
        self.fields_names = self.hash_names(self.fields)
