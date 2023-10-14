import unittest
from modules.llm_interface.context_manager.context_manager import ContextManager  # Replace with the correct import path

class TestContextManager(unittest.TestCase):

    def setUp(self):
        """
        Initializes new ContextManager for each test.
        """
        self.context_manager = ContextManager()

    def test_initialization(self):
        """
        Test if the ContextManager initializes correctly.
        """
        self.assertEqual(self.context_manager.current_context, {})

    def test_update_context(self):
        """
        Test if the update_context method updates the current_context dictionary.
        """
        initial_context = {'key1': 'value1'}
        self.context_manager.update_context(initial_context)
        self.assertEqual(self.context_manager.current_context, initial_context)

        update = {'key2': 'value2'}
        updated_context = {'key1': 'value1', 'key2': 'value2'}
        self.context_manager.update_context(update)
        self.assertEqual(self.context_manager.current_context, updated_context)

    def test_get_methods(self):
        """
        Test if get_methods returns the list of methods.
        """
        methods = self.context_manager.get_methods()
        self.assertIn('update_context', methods)
        self.assertIn('get_methods', methods)

if __name__ == "__main__":
    unittest.main()