import fec.version.v8_1.F1
import fec.version.v8_1.F13
import fec.version.v8_1.F132
import fec.version.v8_1.F133
import fec.version.v8_1.F1M
import fec.version.v8_1.F1S
import fec.version.v8_1.F2
import fec.version.v8_1.F24
import fec.version.v8_1.F2S
import fec.version.v8_1.F3
import fec.version.v8_1.F3L
import fec.version.v8_1.F3P
import fec.version.v8_1.F3P31
import fec.version.v8_1.F3PS
import fec.version.v8_1.F3S
import fec.version.v8_1.F3X
import fec.version.v8_1.F3Z
import fec.version.v8_1.F4
import fec.version.v8_1.F5
import fec.version.v8_1.F56
import fec.version.v8_1.F57
import fec.version.v8_1.F6
import fec.version.v8_1.F65
import fec.version.v8_1.F7
import fec.version.v8_1.F76
import fec.version.v8_1.F9
import fec.version.v8_1.F91
import fec.version.v8_1.F92
import fec.version.v8_1.F93
import fec.version.v8_1.F94
import fec.version.v8_1.F99
import fec.version.v8_1.HRD
import fec.version.v8_1.SA
import fec.version.v8_1.SB
import fec.version.v8_1.SC
import fec.version.v8_1.SC1
import fec.version.v8_1.SC2
import fec.version.v8_1.SD
import fec.version.v8_1.SE
import fec.version.v8_1.SF
import fec.version.v8_1.SH1
import fec.version.v8_1.SH2
import fec.version.v8_1.SH3
import fec.version.v8_1.SH4
import fec.version.v8_1.SH5
import fec.version.v8_1.SH6
import fec.version.v8_1.SL
import fec.version.v8_1.TEXT
import fechbase
class Version(fechbase.VersionBase):
    def __init__(self):
        fechbase.VersionBase.__init__(self)
        self.records = {
            'F1' : fec.version.v8_1.F1.Records,
            'F13' : fec.version.v8_1.F13.Records,
            'F132' : fec.version.v8_1.F132.Records,
            'F133' : fec.version.v8_1.F133.Records,
            'F1M' : fec.version.v8_1.F1M.Records,
            'F1S' : fec.version.v8_1.F1S.Records,
            'F2' : fec.version.v8_1.F2.Records,
            'F24' : fec.version.v8_1.F24.Records,
            'F2S' : fec.version.v8_1.F2S.Records,
            'F3' : fec.version.v8_1.F3.Records,
            'F3L' : fec.version.v8_1.F3L.Records,
            'F3P' : fec.version.v8_1.F3P.Records,
            'F3P31' : fec.version.v8_1.F3P31.Records,
            'F3PS' : fec.version.v8_1.F3PS.Records,
            'F3S' : fec.version.v8_1.F3S.Records,
            'F3X' : fec.version.v8_1.F3X.Records,
            'F3Z' : fec.version.v8_1.F3Z.Records,
            'F4' : fec.version.v8_1.F4.Records,
            'F5' : fec.version.v8_1.F5.Records,
            'F56' : fec.version.v8_1.F56.Records,
            'F57' : fec.version.v8_1.F57.Records,
            'F6' : fec.version.v8_1.F6.Records,
            'F65' : fec.version.v8_1.F65.Records,
            'F7' : fec.version.v8_1.F7.Records,
            'F76' : fec.version.v8_1.F76.Records,
            'F9' : fec.version.v8_1.F9.Records,
            'F91' : fec.version.v8_1.F91.Records,
            'F92' : fec.version.v8_1.F92.Records,
            'F93' : fec.version.v8_1.F93.Records,
            'F94' : fec.version.v8_1.F94.Records,
            'F99' : fec.version.v8_1.F99.Records,
            'HRD' : fec.version.v8_1.HRD.Records,
            'SA' : fec.version.v8_1.SA.Records,
            'SB' : fec.version.v8_1.SB.Records,
            'SC' : fec.version.v8_1.SC.Records,
            'SC1' : fec.version.v8_1.SC1.Records,
            'SC2' : fec.version.v8_1.SC2.Records,
            'SD' : fec.version.v8_1.SD.Records,
            'SE' : fec.version.v8_1.SE.Records,
            'SF' : fec.version.v8_1.SF.Records,
            'SH1' : fec.version.v8_1.SH1.Records,
            'SH2' : fec.version.v8_1.SH2.Records,
            'SH3' : fec.version.v8_1.SH3.Records,
            'SH4' : fec.version.v8_1.SH4.Records,
            'SH5' : fec.version.v8_1.SH5.Records,
            'SH6' : fec.version.v8_1.SH6.Records,
            'SL' : fec.version.v8_1.SL.Records,
            'TEXT' : fec.version.v8_1.TEXT.Records,
        }
        self.field_order = [
            'F1',
            'F13',
            'F132',
            'F133',
            'F1M',
            'F1S',
            'F2',
            'F24',
            'F2S',
            'F3',
            'F3L',
            'F3P',
            'F3P31',
            'F3PS',
            'F3S',
            'F3X',
            'F3Z',
            'F4',
            'F5',
            'F56',
            'F57',
            'F6',
            'F65',
            'F7',
            'F76',
            'F9',
            'F91',
            'F92',
            'F93',
            'F94',
            'F99',
            'HRD',
            'SA',
            'SB',
            'SC',
            'SC1',
            'SC2',
            'SD',
            'SE',
            'SF',
            'SH1',
            'SH2',
            'SH3',
            'SH4',
            'SH5',
            'SH6',
            'SL',
            'TEXT',
        ]
