from unittest import TestCase, main
from reverse_text import reverse_text


class ReverseTextTest(TestCase):
    def setUp(self):
            self.cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            (" ", " "),   (0, None)]


    def test_normal_behevior(self):
        for expected_value, input_value in self.cases:
            self.assertEqual(reverse_text(input_value), expected_value)


    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            reverse_text(0)


if __name__ == '__main__':
    main()
    