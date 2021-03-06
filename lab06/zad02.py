import unittest


def roman(n):
    def ones(nn):
        if nn == 1:
            return "I"
        elif nn == 2:
            return "II"
        elif nn == 3:
            return "III"
        elif nn == 4:
            return "IV"
        elif nn == 5:
            return "V"
        elif nn == 6:
            return "VI"
        elif nn == 7:
            return "VII"
        elif nn == 8:
            return "VIII"
        elif nn == 9:
            return "IX"
        else:
            return ""

    def tens(nt):
        if nt == 1:
            return "X"
        elif nt == 2:
            return "XX"
        elif nt == 3:
            return "XXX"
        elif nt == 4:
            return "XL"
        elif nt == 5:
            return "L"
        elif nt == 6:
            return "LX"
        elif nt == 7:
            return "LXX"
        elif nt == 8:
            return "LXXX"
        elif nt == 9:
            return "XC"
        else:
            return ""

    def hundrets(nh):
        if nh == 1:
            return "C"
        elif nh == 2:
            return "CC"
        elif nh == 3:
            return "CCC"
        elif nh == 4:
            return "CD"
        elif nh == 5:
            return "D"
        elif nh == 6:
            return "DC"
        elif nh == 7:
            return "DCC"
        elif nh == 8:
            return "DCCC"
        elif nh == 9:
            return "CM"
        else:
            return ""

    def thousands(nt):
        if nt == 1:
            return "M"
        elif nt == 2:
            return "MM"
        elif nt == 3:
            return "MMM"
        else:
            return ""

    number = ""
    if n >= 1000:
        number += thousands(n // 1000)
    if n >= 100:
        number += hundrets(n // 100 % 10)
    if n >= 10:
        number += tens((n // 10) % 10)
    if n % 10 > 0:
        number += ones(n % 10)
    return number


class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")