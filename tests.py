from unittest import TestCase, main
from first_task import first_task


class FirstTaskTest (TestCase):

    def test_one (self):
        self.assertEqual(first_task('abcd efgh'), 'dcba hgfe')


    def test_two(self):
        with self.assertRaises(AttributeError):
            first_task(0)


    def test_three(self):
        first_task('a1bcd efg!h')
        self.assertTrue(first_task('d1cba hgf!e'))

if __name__ == '__main__':
    main()