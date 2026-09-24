"""Conferência editorial de exemplos do capítulo 6; não é laboratório ofensivo."""
import unittest


class Chapter6Examples(unittest.TestCase):
    def test_positional_notation(self):
        self.assertEqual(13, int('1101', 2))
        self.assertEqual(13, int('00001101', 2))
        self.assertEqual(173, int('10101101', 2))
        self.assertEqual(173, int('AD', 16))
        self.assertEqual('10101101', format(173, '08b'))
        self.assertEqual(255, int('FF', 16))
        self.assertEqual(256, 2 ** 8)
        self.assertEqual(65535, 2 ** 16 - 1)

    def test_signed_and_unsigned(self):
        self.assertEqual(255, int.from_bytes(b'\xff', 'big', signed=False))
        self.assertEqual(-1, int.from_bytes(b'\xff', 'big', signed=True))
        self.assertEqual(-128, int.from_bytes(b'\x80', 'big', signed=True))
        self.assertEqual(127, int.from_bytes(b'\x7f', 'big', signed=True))
        # Reter oito bits baixos é a regra explícita do exemplo, não de toda linguagem.
        self.assertEqual(0, (255 + 1) & 0xff)

    def test_endianness(self):
        self.assertEqual(4660, int.from_bytes(bytes.fromhex('12 34'), 'big'))
        self.assertEqual(13330, int.from_bytes(bytes.fromhex('12 34'), 'little'))
        self.assertEqual(bytes.fromhex('34 12'), (4660).to_bytes(2, 'little'))

    def test_units(self):
        self.assertEqual(1024, 2 ** 10)
        self.assertEqual(1048576, 2 ** 20)
        self.assertEqual(8000000, 1000000 * 8)
        self.assertEqual(12.5, 100000000 / 8 / 1000000)

    def test_text_encodings(self):
        self.assertEqual(bytes.fromhex('41 42 43'), 'ABC'.encode('ascii'))
        self.assertEqual(bytes.fromhex('34 31'), '41'.encode('ascii'))
        self.assertEqual(bytes.fromhex('41'), 'A'.encode('utf-8'))
        self.assertEqual(bytes.fromhex('C3 A9'), '\u00e9'.encode('utf-8'))
        self.assertEqual(bytes.fromhex('F0 9F 94 92'), '\U0001f512'.encode('utf-8'))
        self.assertEqual(7, len('A\u00e9\U0001f512'.encode('utf-8')))
        self.assertEqual(3, len('A\u00e9\U0001f512'))
        self.assertEqual(2, len('\u00e9'.encode('utf-8')))
        self.assertEqual(bytes.fromhex('65 CC 81'), 'e\u0301'.encode('utf-8'))
        self.assertEqual(3, len('e\u0301'.encode('utf-8')))
        self.assertEqual(4, len('ABCD'.encode('utf-8')))
        self.assertEqual(8, len('\u00e9\u00e9\u00e9\u00e9'.encode('utf-8')))
        with self.assertRaises(UnicodeDecodeError):
            bytes.fromhex('C3').decode('utf-8')


if __name__ == '__main__':
    unittest.main()
