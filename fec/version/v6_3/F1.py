import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER COMMITTEE ID NUMBER', 'number': '2'},
            {'name': 'CHANGE OF COMMITTEE NAME', 'number': '3'},
            {'name': 'COMMITTEE NAME', 'number': '4'},
            {'name': 'CHANGE OF ADDRESS', 'number': '5'},
            {'name': 'STREET 1', 'number': '6'},
            {'name': 'STREET 2', 'number': '7'},
            {'name': 'CITY', 'number': '8'},
            {'name': 'STATE', 'number': '9'},
            {'name': 'ZIP', 'number': '10'},
            {'name': 'CHANGE OF COMMITTEE EMAIL', 'number': '11'},
            {'name': 'COMMITTEE EMAIL', 'number': '12'},
            {'name': 'CHANGE OF COMMITTEE WEB URL', 'number': '13'},
            {'name': 'COMMITTEE WEB URL', 'number': '14'},
            {'name': 'SUBMISSION DATE', 'number': '15'},
            {'name': 'SIGNATURE LAST NAME', 'number': '16'},
            {'name': 'SIGNATURE FIRST NAME', 'number': '17'},
            {'name': 'SIGNATURE MIDDLE NAME', 'number': '18'},
            {'name': 'SIGNATURE PREFIX', 'number': '19'},
            {'name': 'SIGNATURE SUFFIX', 'number': '20'},
            {'name': 'DATE SIGNED', 'number': '21'},
            {'name': 'COMMITTEE TYPE', 'number': '22-5.'},
            {'name': 'CANDIDATE ID NUMBER', 'number': '23-5.'},
            {'name': 'CANDIDATE LAST NAME', 'number': '24-5.'},
            {'name': 'CANDIDATE FIRST NAME', 'number': '25-5.'},
            {'name': 'CANDIDATE MIDDLE NAME', 'number': '26-5.'},
            {'name': 'CANDIDATE PREFIX', 'number': '27-5.'},
            {'name': 'CANDIDATE SUFFIX', 'number': '28-5.'},
            {'name': 'CANDIDATE OFFICE', 'number': '29-5.'},
            {'name': 'CANDIDATE STATE', 'number': '30-5.'},
            {'name': 'CANDIDATE DISTRICT', 'number': '31-5.'},
            {'name': 'PARTY CODE', 'number': '32-5.'},
            {'name': 'PARTY TYPE', 'number': '33-5.'},
            {'name': 'ORGANIZATION TYPE', 'number': '34-5 (e).'},
            {'name': 'LOBBYIST/REGISTRANT PAC', 'number': '35-5 (e).'},
            {'name': 'LOBBYIST/REGISTRANT PAC', 'number': '36-5 (f).'},
            {'name': 'LEADERSHIP PAC', 'number': '37-5 (f).'},
            {'name': 'AFFILIATED CMTTE ID NUM', 'number': '38-6.'},
            {'name': 'AFFILIATED CMTTE NAME', 'number': '39-6.'},
            {'name': 'AFFILIATED CANDIDATE ID NUM', 'number': '40-6.'},
            {'name': 'AFFILIATED LAST NAME', 'number': '41-6.'},
            {'name': 'AFFILIATED FIRST NAME', 'number': '42-6.'},
            {'name': 'AFFILIATED MIDDLE NAME', 'number': '43-6.'},
            {'name': 'AFFILIATED PREFIX', 'number': '44-6.'},
            {'name': 'AFFILIATED SUFFIX', 'number': '45-6.'},
            {'name': 'AFFILIATED STREET 1', 'number': '46-6.'},
            {'name': 'AFFILIATED STREET 2', 'number': '47-6.'},
            {'name': 'AFFILIATED CITY', 'number': '48-6.'},
            {'name': 'AFFILIATED STATE', 'number': '49-6.'},
            {'name': 'AFFILIATED ZIP', 'number': '50-6.'},
            {'name': 'AFFILIATED RELATIONSHIP CODE (with Filing Committe named in field #4)', 'number': '51-6.'},
            {'name': 'CUSTODIAN LAST NAME', 'number': '52-7.'},
            {'name': 'CUSTODIAN FIRST NAME', 'number': '53-7.'},
            {'name': 'CUSTODIAN MIDDLE NAME', 'number': '54-7.'},
            {'name': 'CUSTODIAN PREFIX', 'number': '55-7.'},
            {'name': 'CUSTODIAN SUFFIX', 'number': '56-7.'},
            {'name': 'CUSTODIAN STREET 1', 'number': '57-7.'},
            {'name': 'CUSTODIAN STREET 2', 'number': '58-7.'},
            {'name': 'CUSTODIAN CITY', 'number': '59-7.'},
            {'name': 'CUSTODIAN STATE', 'number': '60-7.'},
            {'name': 'CUSTODIAN ZIP', 'number': '61-7.'},
            {'name': 'CUSTODIAN TITLE', 'number': '62-7.'},
            {'name': 'CUSTODIAN TELEPHONE', 'number': '63-7.'},
            {'name': 'TREASURER LAST NAME', 'number': '64-8.'},
            {'name': 'TREASURER FIRST NAME', 'number': '65-8.'},
            {'name': 'TREASURER MIDDLE NAME', 'number': '66-8.'},
            {'name': 'TREASURER PREFIX', 'number': '67-8.'},
            {'name': 'TREASURER SUFFIX', 'number': '68-8.'},
            {'name': 'TREASURER STREET 1', 'number': '69-8.'},
            {'name': 'TREASURER STREET 2', 'number': '70-8.'},
            {'name': 'TREASURER CITY', 'number': '71-8.'},
            {'name': 'TREASURER STATE', 'number': '72-8.'},
            {'name': 'TREASURER ZIP', 'number': '73-8.'},
            {'name': 'TREASURER TITLE', 'number': '74-8.'},
            {'name': 'TREASURER TELEPHONE', 'number': '75-8.'},
            {'name': 'AGENT LAST NAME', 'number': '76-8.'},
            {'name': 'AGENT FIRST NAME', 'number': '77-8.'},
            {'name': 'AGENT MIDDLE NAME', 'number': '78-8.'},
            {'name': 'AGENT PREFIX', 'number': '79-8.'},
            {'name': 'AGENT SUFFIX', 'number': '80-8.'},
            {'name': 'AGENT STREET 1', 'number': '81-8.'},
            {'name': 'AGENT STREET 2', 'number': '82-8.'},
            {'name': 'AGENT CITY', 'number': '83-8.'},
            {'name': 'AGENT STATE', 'number': '84-8.'},
            {'name': 'AGENT ZIP', 'number': '85-8.'},
            {'name': 'AGENT TITLE', 'number': '86-8.'},
            {'name': 'AGENT TELEPHONE', 'number': '87-8.'},
            {'name': 'BANK NAME', 'number': '88-9. a)'},
            {'name': 'BANK STREET 1', 'number': '89-9. a)'},
            {'name': 'BANK STREET 2', 'number': '90-9. a)'},
            {'name': 'BANK CITY', 'number': '91-9. a)'},
            {'name': 'BANK STATE', 'number': '92-9. a)'},
            {'name': 'BANK ZIP', 'number': '93-9. a)'},
            {'name': 'BANK NAME', 'number': '94-9. b)'},
            {'name': 'BANK STREET 1', 'number': '95-9. b)'},
            {'name': 'BANK STREET 2', 'number': '96-9. b)'},
            {'name': 'BANK CITY', 'number': '97-9. b)'},
            {'name': 'BANK STATE', 'number': '98-9. b)'},
            {'name': 'BANK ZIP', 'number': '99-9. b)'},
    ]
        self.fields_names = self.hash_names(self.fields)
