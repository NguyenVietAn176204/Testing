import unittest
def GiamGia(a , b):
    if a < 0 or b < 0:
        return -1
    if a <= 120 and b <= 6:
        return 100
    if a > 120 and b <= 6:
        return 70
    if a <= 120 and b > 6:
        return 50
    return 0
    
class GiamGiaTestBien(unittest.TestCase):
    def test_giam_gia_1(self):
        result = GiamGia(119,7)
        self.assertEqual(result, 50)

    def test_giam_gia_2(self):
        result = GiamGia(119,0)
        self.assertEqual(result, 100)

    def test_giam_gia_3(self):
        result = GiamGia(119,1)
        self.assertEqual(result, 100)

    def test_giam_gia_4(self):
        result = GiamGia(119,9)
        self.assertEqual(result, 50)

    def test_giam_gia_5(self):
        result = GiamGia(119, 100)
        self.assertEqual(result, 50)

    def test_giam_gia_6(self):
        result = GiamGia(30,7)
        self.assertEqual(result, 50)

    def test_giam_gia_7(self):
        result = GiamGia(31, 7)
        self.assertEqual(result, 50)

    def test_giam_gia_8(self):
        result = GiamGia(199,7)
        self.assertEqual(result, 0)

    def test_giam_gia_9(self):
        result = GiamGia(200,7)
        self.assertEqual(result, 0)


class GiamGiaTestBangQD(unittest.TestCase):
    def test_giam_gia_1(self):
        result = GiamGia(110,5)
        self.assertEqual(result, 100)

    def test_giam_gia_2(self):
        result = GiamGia(130,5)
        self.assertEqual(result, 70)

    def test_giam_gia_3(self):
        result = GiamGia(110,7)
        self.assertEqual(result, 50)

    def test_giam_gia_4(self):
        result = GiamGia(150,9)
        self.assertEqual(result, 0)

    def test_giam_gia_5(self):
        result = GiamGia(-1, -1)
        self.assertEqual(result, -1)


class GiamGiaTestC2(unittest.TestCase):
    def test_giam_gia_1(self):
        result = GiamGia(-2,-2)
        self.assertEqual(result, -1)

    def test_giam_gia_2(self):
        result = GiamGia(119,5)
        self.assertEqual(result, 100)
        
    def test_giam_gia_3(self):
        result = GiamGia(121,5)
        self.assertEqual(result, 70)

    def test_giam_gia_4(self):
        result = GiamGia(119,70)
        self.assertEqual(result, 50)
    def test_giam_gia_5(self):
        result = GiamGia(121,7)
        self.assertEqual(result, 0)

    class GiamGiaTestAllUse(unittest.TestCase):
        def test_giam_gia_1(self):
            result = GiamGia(122,9)
            self.assertEqual(result,0)
if __name__ =='__main__':
    unittest.main()

