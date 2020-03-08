"""Unit tests for Resume generator"""

import unittest
import json

from resume.resume import Resume
from resume.docx import ResumeDocx
from resume.pdf import ResumePdf
from resume.markdown import ResumeMarkDown

class ResumeTestCase(unittest.TestCase):
    """Resume test case"""

    def setUp(self):
        self.resume = Resume(['docx'] ,profile=self.get_profile())
    
    def get_profile(self):
        with open('./profile.json') as file:
            profile = json.load(file)
        return profile
    
    def test_resume_inheritance(self):
        self.assertIsInstance(self.resume, Resume)
    
    def test_generate_method(self):
        self.resume._mode = ['docx', 'pdf', 'markdown']
        self.resume.generate()


class ResumeDocx(unittest.TestCase):
    
    def test_resume_docx_instance(self):
        with open('./profile.json') as file:
            profile = json.load(file)
        print(profile)
class ResumePdf(unittest.TestCase):
    pass

class ResumeMarkDown(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
