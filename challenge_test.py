import unittest
from challenge import *

# Test case provided
example_scenario = {'Manager': 'A',
'Subordinates': [{'Manager': 'B',
'Subordinates': [{'Developer': 'C'},{'QA Tester': 'D'}]}]}

sample_department = {'Manager': 'Tom',
 'Subordinates': [{'Developer': 'Chris'}, {'QA Tester': 'Will'}, {'Manager': 'Sarah',
 'Subordinates': [{'Developer': 'Tim'}, {'QA Tester': 'Jackie'}, {'QA Tester': 'Matt'}, {'Manager': 'Alice',
 'Subordinates': [{'QA Tester': 'Steve'}]}]}]}

starship_enterprise = {'Manager': 'Picard',
 'Subordinates': [{'Manager': 'Riker',
 'Subordinates': [{'Developer': 'Troi'}, {'Developer': "Crusher"}, {'QA Tester': 'Data'}, {'Manager': 'Worf',
 'Subordinates': [{'Developer': 'Yar'}, {'QA Tester': 'O brien'}, {'Manager': 'La Forge', 
 'Subordinates': [{'Manager': 'Wesley',
 'Subordinates': [{'QA Tester': 'Red Shirt'}]}]}]}]}]}

class MyTest(unittest.TestCase):
    
    def test_getAllocation_on_example(self):
        self.assertEqual(getAllocation(example_scenario), 2100)
        self.assertEqual(getAllocation(sample_department), 4900)
        self.assertEqual(getAllocation(starship_enterprise), 6000)
        
    def test_sliceDepartment(self):
        self.assertEqual(sliceDepartment(starship_enterprise, 'Worf')['Manager'], 'Worf')
        
if __name__ == "__main__":
    unittest.main()




