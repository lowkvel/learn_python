# testing classes

class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_question(self):
        print(self.question)
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

import unittest

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

class TestAnonymousSurvey_v2(unittest.TestCase):    # use setUp() to simplify the test initiation
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)    


if __name__ == '__main__':
    unittest.main()

