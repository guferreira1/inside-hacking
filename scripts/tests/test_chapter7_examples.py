"""Check only the explicit arithmetic models in chapter 7, not hardware."""
from fractions import Fraction
import unittest


class Chapter7Examples(unittest.TestCase):
    def test_clock_period(self):
        frequency_hz = 2_000_000_000
        period_seconds = Fraction(1, frequency_hz)
        self.assertEqual(period_seconds * 1_000_000_000, Fraction(1, 2))

    def test_hypothetical_cycles(self):
        self.assertEqual(Fraction(4_000_000, 2_000_000_000), Fraction(2, 1000))

    def test_cache_cost_already_includes_lookup(self):
        hit_cost, additional_miss_cost = 2, 18
        miss_cost = hit_cost + additional_miss_cost
        total = 8 * hit_cost + 2 * miss_cost
        self.assertEqual(total, 56)
        self.assertEqual(Fraction(total, 10), Fraction(28, 5))
        self.assertEqual(Fraction(total, 10), hit_cost + Fraction(2, 10) * additional_miss_cost)

    def test_address_is_not_content(self):
        # An explicitly invented mapping, not the host's memory.
        memory = {0x1000: 0x41, 0x1001: 0x42, 0x1002: 0x43, 0x1003: 0}
        addresses_before = tuple(memory)
        self.assertEqual(bytes(memory[a] for a in addresses_before[:3]), b"ABC")
        memory[0x1000] = 0x5A
        self.assertEqual(tuple(memory), addresses_before)
        self.assertEqual(bytes(memory[a] for a in addresses_before[:3]), b"ZBC")


if __name__ == "__main__":
    unittest.main()
