from unittest import TestCase, main
from reverse_text import reverse_text


class ReverseTextTest (TestCase):
    def setUp(self):
            self.cases = [
            ("abcd efgh", "dcba hgfe"),
            ("a1bcd efg!h", "d1cba hgf!e"),
            (" ", " ")]


    def test_normal_behevior (self):
        self.assertEqual(reverse_text('abcd efgh'), 'dcba hgfe')


    def test_wrong_type(self):
        with self.assertRaises(AttributeError):
            reverse_text(0)


    def test_is_true(self):
        reverse_text('a1bcd efg!h')
        self.assertTrue(reverse_text('d1cba hgf!e'))


if __name__ == '__main__':
    main()
    