import fechbase
class Records(fechbase.RecordsBase):
    def __init__(self):
        fechbase.RecordsBase.__init__(self)
        self.fields = [
            {'name': 'FORM TYPE', 'number': '1'},
            {'name': 'FILER FEC CMTE ID (PCC)', 'number': '2'},
            {'name': 'COMMITTEE NAME (PCC)', 'number': '3'},
            {'name': 'Coverage FROM', 'number': '4-'},
            {'name': 'Coverage TO', 'number': '5-'},
            {'name': 'FEC COMMITTEE ID NUMBER (Auth)', 'number': '6'},
            {'name': 'COMMITTEE NAME (Auth)', 'number': '7'},
            {'name': 'individuals total', 'number': '8-(a) 11(a)iii'},
            {'name': 'Political party committees', 'number': '9-(b) 11(b)'},
            {'name': 'other pol committees (PACs)', 'number': '10-(c) 11(c)'},
            {'name': 'the candidate', 'number': '11-(d) 11(d)'},
            {'name': 'total contributions', 'number': '12-(e) 11(e)'},
            {'name': 'Transfers from other auth Committees', 'number': '13-(f) 12'},
            {'name': 'made or guarn by candidate', 'number': '14-(g) 13(a)'},
            {'name': 'all other loans', 'number': '15-(h) 13(b)'},
            {'name': 'total loans', 'number': '16-(i) 13(c)'},
            {'name': 'offsets to operating expend', 'number': '17-(j) 14'},
            {'name': 'Other receipts', 'number': '18-(k) 15'},
            {'name': 'total receipts', 'number': '19-(l) 16'},
            {'name': 'Operating Expenditures', 'number': '20-(m) 17'},
            {'name': 'Transfers to other auth Committees', 'number': '21-(n) 18'},
            {'name': 'made or guaranteed by cand', 'number': '22-(o) 19(a)'},
            {'name': 'all other loans', 'number': '23-(p) 19(b)'},
            {'name': 'total loan repayments', 'number': '24-(q) 19(c)'},
            {'name': 'total refunds individuals', 'number': '25-(r) 20(a)'},
            {'name': 'Refunds Political Party Committees', 'number': '26-(s) 20(b)'},
            {'name': 'Refunds other Political Committees', 'number': '27-(t) 20(c)'},
            {'name': 'total contribution refunds', 'number': '28-(u) 20(d)'},
            {'name': 'Other disbursements', 'number': '29-(v) 21'},
            {'name': 'Total disbursements', 'number': '30-(w) 22'},
            {'name': 'COH beginning reporting period', 'number': '31-(x) 23'},
            {'name': 'COH at close of period', 'number': '32-(y) 27'},
            {'name': 'Debts to', 'number': '33-(z) 9'},
            {'name': 'Debts by', 'number': '34-(aa) 12'},
            {'name': 'net contributions', 'number': '35-(bb) 6(c)'},
            {'name': 'net operating expenditures', 'number': '36-(cc) 7(c)'},
    ]
        self.fields_names = self.hash_names(self.fields)
