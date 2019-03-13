# ----------------------------------------------------------------------
# Name:        testhw4
# Purpose:     Unit Testing for Homework 4
#
# Date:       3/9/2019
# ----------------------------------------------------------------------
"""
Unit Testing for Homework 4.

Test cases for top_students, extra_credit, adjusted_grade,
sum_of_inverse_odd and same_length functions in hw4.
"""

import unittest
import homework4 as hw4

class TestQ1(unittest.TestCase):
    """
    Test case for the normal execution of the top_students function.
    """

    def setUp(self):
        """Create dictionaries for testing."""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_top_students_default(self):
        """Test the top_students function default parameter."""
        self.assertEqual(len(hw4.top_students(self.cs122)), 3)

    def test_top_students_empty(self):
        """Test the top_students function with empty dictionary."""
        self.assertEqual(hw4.top_students(self.empty_class, 6),[])

    def test_top_students_2(self):
        """Test the top_students function with n = 2."""
        self.assertEqual(hw4.top_students(self.cs122, 2),
                         ['Anna', 'Alex'])
        self.assertEqual(self.cs122,
                         {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

    def test_top_students_10(self):
        """Test the top_students function with n=10."""
        self.assertEqual(hw4.top_students(self.cs122, 10),
                         ['Anna', 'Alex', 'Zoe', 'Dan'])
        self.assertEqual(self.cs122,
                         {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

class TestQ2(unittest.TestCase):
    """
    Test case for the normal execution of the extra_credit function.
    """

    def setUp(self):
        """Create dictionaries for testing."""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_extra_credit_default(self):
        """Test the extra_credit function default parameter."""
        self.assertEqual(hw4.extra_credit(self.cs122),
                        {'Zoe': 91, 'Alex': 94, 'Dan': 80, 'Anna': 101})
        self.assertEqual(self.cs122,
                        {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

    def test_extra_credit_empty(self):
        """Test the extra_credit function with empty dictionary."""
        self.assertEqual(hw4.extra_credit(self.empty_class, 5), {})

    def test_extra_credit_2(self):
        """Test the extra_credit function with point = 2."""
        self.assertEqual(hw4.extra_credit(self.cs122, 2),
                        {'Zoe': 92, 'Alex': 95, 'Dan': 81, 'Anna': 102})
        self.assertEqual(self.cs122,
                        {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

class TestQ3(unittest.TestCase):
    """
    Test case for the normal execution of the adjusted_grade function.
    """
    def setUp(self):
        """Create dictionaries for testing."""
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100,
                         'Anna': 110, 'Bryan': 2, 'Andrea': 110}
        self.exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
                     'Bryan': 95, 'Andrea': 86}

    def test_adjusted_grade(self):
        """Test the adjusted_grade function."""
        self.assertEqual(hw4.adjusted_grade(self.iclicker, self.exam),
                         {'Bryan': 95, 'Zoe': 0, 'Anna': 65,
                          'Alex': 96, 'Ryan': 90, 'Andrea': 87,
                          'Dan': 89})
        self.assertEqual(self.iclicker, {'Zoe': 46, 'Alex': 121,
                                         'Ryan': 100, 'Anna': 110,
                                         'Bryan': 2, 'Andrea': 110})
        self.assertEqual(self.exam, {'Dan': 89, 'Ryan': 89, 'Alex': 95,
                                     'Anna': 64, 'Bryan': 95, 'Andrea': 86})

    def test_adjusted_grade_empty_iclicker(self):
        """Test the adjusted_grade function with empty iclicker."""
        self.assertEqual(hw4.adjusted_grade({}, self.exam),
                    {'Ryan': 89, 'Andrea': 86, 'Bryan': 95,
                     'Anna': 64, 'Dan': 89, 'Alex': 95})
        self.assertEqual(self.iclicker, {'Zoe': 46, 'Alex': 121,
                                         'Ryan': 100, 'Anna': 110,
                                         'Bryan': 2, 'Andrea': 110})
        self.assertEqual(self.exam, {'Dan': 89, 'Ryan': 89, 'Alex': 95,
                                     'Anna': 64, 'Bryan': 95, 'Andrea': 86})

    def test_adjusted_grade_empty_exam(self):
        """Test the adjusted_grade function with empty exam."""
        self.assertEqual(hw4.adjusted_grade(self.iclicker, {}),
                        {'Ryan': 1, 'Andrea': 1, 'Bryan': 0,
                         'Zoe': 0, 'Anna': 1, 'Alex': 1})
        self.assertEqual(self.iclicker, {'Zoe': 46, 'Alex': 121,
                                         'Ryan': 100, 'Anna': 110,
                                         'Bryan': 2, 'Andrea': 110})
        self.assertEqual(self.exam, {'Dan': 89, 'Ryan': 89, 'Alex': 95,
                                     'Anna': 64, 'Bryan': 95, 'Andrea': 86})

    def test_adjusted_grade_both_empty(self):
        """Test the adjusted_grade function with empty dictionaries."""
        self.assertEqual(hw4.adjusted_grade({}, {}), {})

class TestQ4(unittest.TestCase):
    """
    Test case for the normal execution of
    the sum_of_inverse_odd function.
    """

    def test_sum_of_inverse_odd_0(self):
        """Test the sum_of_inverse_odd function with n = 0."""
        self.assertEqual(hw4.sum_of_inverse_odd(0), 0)

    def test_sum_of_inverse_odd_1(self):
        """Test the sum_of_inverse_odd function with n = 1."""
        self.assertEqual(hw4.sum_of_inverse_odd(1), 1.0)

    def test_sum_of_inverse_odd_2(self):
        """Test the sum_of_inverse_odd function with n = 2."""
        self.assertEqual(hw4.sum_of_inverse_odd(2), 1.0)

    def test_sum_of_inverse_odd_3(self):
        """Test the sum_of_inverse_odd function with n = 3."""
        self.assertAlmostEqual(hw4.sum_of_inverse_odd(3), 1.333333333333)

    def test_sum_of_inverse_odd_2000(self):
        """Test the sum_of_inverse_odd function with n = 2000."""
        self.assertAlmostEqual(hw4.sum_of_inverse_odd(2000),
                                          4.435632673335106)

class TestQ5(unittest.TestCase):
    """
    Test case for the normal execution of the same_length function.
    """

    def test_same_length_empty(self):
        """Test the same_length with empty argument."""
        self.assertTrue(hw4.same_length())

    def test_same_length_1(self):
        """Test the same_length with 1 argument."""
        self.assertTrue(hw4.same_length('Spartan'))

    def test_same_length_3_same(self):
        """Test the same_length with 3 same length arguments."""
        self.assertTrue(hw4.same_length('hi', 'ha', 'it'))

    def test_same_length_4_not_same_1(self):
        """Test the same_length with 4 different length arguments."""
        self.assertFalse(hw4.same_length('hi', 'ha', 'it', 'quiet'))

    def test_same_length_4_not_same_2(self):
        """Test the same_length with 4 different length arguments."""
        self.assertFalse(hw4.same_length('hello', 'ha', 'it', 'ok'))
    def test_same_length_empty_strings_1(self):
        """Test the same_length with empty strings"""
        self.assertTrue(hw4.same_length('','',''))
    def test_same_length_emtpy_strings_2(self):
        """Test the same length with 1 non empty string"""
        self.assertFalse(hw4.same_length('','a',''))

if __name__ == '__main__':
    unittest.main()
