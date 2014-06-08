import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'JOINT FUND PARTICIPANT CMTTE NAME', 'number': '3-5.'},
            {'name': 'JOINT FUND PARTICIPANT CMTTE FEC-ID', 'number': '4-5.'},
            {'name': 'AFFILIATED CMTTE ID NUM', 'number': '5-6.'},
            {'name': 'AFFILIATED CMTTE NAME', 'number': '6-6.'},
            {'name': 'AFFILIATED CANDIDATE ID NUM', 'number': '7-6.'},
            {'name': 'AFFILIATED LAST NAME', 'number': '8-6.'},
            {'name': 'AFFILIATED FIRST NAME', 'number': '9-6.'},
            {'name': 'AFFILIATED MIDDLE NAME', 'number': '10-6.'},
            {'name': 'AFFILIATED PREFIX', 'number': '11-6.'},
            {'name': 'AFFILIATED SUFFIX', 'number': '12-6.'},
            {'name': 'AFFILIATED STREET 1', 'number': '13-6.'},
            {'name': 'AFFILIATED STREET 2', 'number': '14-6.'},
            {'name': 'AFFILIATED CITY', 'number': '15-6.'},
            {'name': 'AFFILIATED STATE', 'number': '16-6.'},
            {'name': 'AFFILIATED ZIP', 'number': '17-6.'},
            {'name': 'AFFILIATED RELATIONSHIP CODE (with Filing Committee named in field #4)', 'number': '18-6.'},
            {'name': 'AGENT LAST NAME', 'number': '19-8.'},
            {'name': 'AGENT FIRST NAME', 'number': '20-8.'},
            {'name': 'AGENT MIDDLE NAME', 'number': '21-8.'},
            {'name': 'AGENT PREFIX', 'number': '22-8.'},
            {'name': 'AGENT SUFFIX', 'number': '23-8.'},
            {'name': 'AGENT STREET 1', 'number': '24-8.'},
            {'name': 'AGENT STREET 2', 'number': '25-8.'},
            {'name': 'AGENT CITY', 'number': '26-8.'},
            {'name': 'AGENT STATE', 'number': '27-8.'},
            {'name': 'AGENT ZIP', 'number': '28-8.'},
            {'name': 'AGENT TITLE', 'number': '29-8.'},
            {'name': 'AGENT TELEPHONE', 'number': '30-8.'},
            {'name': 'BANK NAME', 'number': '31-9.'},
            {'name': 'BANK STREET 1', 'number': '32-9.'},
            {'name': 'BANK STREET 2', 'number': '33-9.'},
            {'name': 'BANK CITY', 'number': '34-9.'},
            {'name': 'BANK STATE', 'number': '35-9.'},
            {'name': 'BANK ZIP', 'number': '36-9.'},
    ]
        self.fields_names = self.hash_names(self.fields)