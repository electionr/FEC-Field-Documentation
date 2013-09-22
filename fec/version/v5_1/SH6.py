from fec.version.records_base import RecordsBase
class Records(RecordsBase):
    def __init__(self):
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID', 'number': '2'},
            {'name': 'ENTITY TYPE', 'number': '3'},
            {'name': 'NAME (Payee)', 'number': '4'},
            {'name': 'STREET 1', 'number': '5'},
            {'name': 'STREET 2', 'number': '6'},
            {'name': 'CITY', 'number': '7'},
            {'name': 'STATE', 'number': '8'},
            {'name': 'ZIP', 'number': '9'},
            {'name': 'CATEGORY CODE', 'number': '10'},
            {'name': 'TRANS CODE', 'number': '11'},
            {'name': 'TRANS Purpose DESCRIP', 'number': '12'},
            {'name': 'DATE', 'number': '13'},
            {'name': 'TOTAL AMOUNT', 'number': '14'},
            {'name': 'FEDERAL SHARE', 'number': '15'},
            {'name': 'LEVIN SHARE', 'number': '16'},
            {'name': 'Activity Is Voter Registration', 'number': '17-'},
            {'name': 'Activity Is Voter ID', 'number': '18-'},
            {'name': 'Activity GOTV', 'number': '19-'},
            {'name': 'Activity is Generic Campaign', 'number': '20-'},
            {'name': 'ACTIVITY/EVENT YEAR-TO-DATE', 'number': '21'},
            {'name': 'ADDITIONAL DESCRIPTION', 'number': '22'},
            {'name': 'FEC COMMITTEE ID NUMBER', 'number': '23'},
            {'name': 'FEC CANDIDATE ID NUMBER', 'number': '24'},
            {'name': 'CANDIDATE NAME', 'number': '25'},
            {'name': 'CAN/OFFICE', 'number': '26'},
            {'name': 'CAN/STATE', 'number': '27'},
            {'name': 'CAN/DIST', 'number': '28'},
            {'name': 'CONDUIT COMMITTEE ID', 'number': '29'},
            {'name': 'CONDUIT NAME', 'number': '30'},
            {'name': 'CONDUIT STREET 1', 'number': '31'},
            {'name': 'CONDUIT STREET 2', 'number': '32'},
            {'name': 'CONDUIT CITY', 'number': '33'},
            {'name': 'CONDUIT STATE', 'number': '34'},
            {'name': 'CONDUIT ZIP', 'number': '35'},
            {'name': 'MEMO CODE', 'number': '36'},
            {'name': 'MEMO TEXT', 'number': '37'},
            {'name': 'AMENDED CD', 'number': '38'},
            {'name': 'TRAN ID', 'number': '39'},
            {'name': 'BACK REF TRAN ID', 'number': '40'},
            {'name': 'BACK REF SCHED NAME', 'number': '41'},
    ]