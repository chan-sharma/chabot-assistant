# tests/test_agent.py

import unittest
from chatbot_assistant.agent_orchestrator import AIAgent

class TestAIAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AIAgent()

    def test_get_response(self):
        user_input = "Hello"
        response = self.agent.get_response(user_input)
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()