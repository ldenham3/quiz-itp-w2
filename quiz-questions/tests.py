import unittest
from question_1 import question_1
from question_2 import number_of_customers_per_state
from question_3 import eldest_customer_per_state

# QUESTION 1
class QuestionsTestCase(unittest.TestCase):
    def test_question_1(self):
        self.assertEqual(question_1(), 30, "Question 1 answer FAILED")

# QUESTION 2
class NumberOfCustomersPerStateTestCase(unittest.TestCase):
    def test_number_of_customers_per_state(self):
        """Should return the correct number of customers per state."""
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }, {
                'name': 'Robert',
                'age': 16
            }],
            'NY': [{
                'name': 'Linda',
                'age': 71
            }],
            'CA': [{
                'name': 'Barbara',
                'age': 15
            }, {
                'name': 'Paul',
                'age': 18
            }]
        }
        expected_result = {
            'UT': 3,
            'NY': 1,
            'CA': 2
        }
        self.assertEqual(
            number_of_customers_per_state(customers), expected_result)

    def test_number_of_customers_per_state_with_blank_state(self):
        """Should return the correct number of customers per state."""
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }, {
                'name': 'Robert',
                'age': 16
            }],
            'NY': None,  # Be Careful! NY value is None
            'CA': [{
                'name': 'Barbara',
                'age': 15
            }, {
                'name': 'Paul',
                'age': 18
            }]
        }
        expected_result = {
            'UT': 3,
            'NY': 0,
            'CA': 2
        }
        self.assertEqual(
            number_of_customers_per_state(customers), expected_result)

# QUESTION 3
class EldestCustomerTestCase(unittest.TestCase):
    def test_eldest_customers(self):
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }, {
                'name': 'Robert',
                'age': 16
            }],
            'NY': [{
                'name': 'Linda',
                'age': 71
            }, {
                'name': 'Lisa',
                'age': 25
            }, {
                'name': 'Daniel',
                'age': 45
            }],
            'CA': [{
                'name': 'Barbara',
                'age': 15
            }, {
                'name': 'Paul',
                'age': 18
            }, {
                'name': 'Helen',
                'age': 29
            }]
        }
        expected_result = {
            'UT': {
                'name': 'John',
                'age': 31
            },
            'NY': {
                'name': 'Linda',
                'age': 71
            },
            'CA': {
                'name': 'Helen',
                'age': 29
            }
        }
        self.assertEqual(eldest_customer_per_state(customers), expected_result)

    def test_eldest_customers_with_empty_states(self):
        customers = {
            'UT': [{
                'name': 'Mary',
                'age': 28
            }, {
                'name': 'John',
                'age': 31
            }],
            'NY': []
        }
        expected_result = {
            'UT': {
                'name': 'John',
                'age': 31
            },
            'NY': None
        }
        self.assertEqual(eldest_customer_per_state(customers), expected_result)