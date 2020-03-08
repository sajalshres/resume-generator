"""Unit tests for Resume generator"""

import unittest
import json

from resume.resume import Resume
from resume.docx import ResumeDocx
from resume.pdf import ResumePdf
from resume.markdown import ResumeMarkDown
from resume.utils import get_profile

class ResumeTestCase(unittest.TestCase):
    """Resume test case"""

    def setUp(self):
        profile = get_profile("./profile.json")
        mode = ['docx']
        self.resume = Resume(mode ,profile=profile)
    
    def test_resume_inheritance(self):
        self.assertIsInstance(self.resume, Resume)
    
    def test_generate_method(self):
        pass


class ResumeDocxTestCase(unittest.TestCase):

    def setUp(self):
        profile = get_profile("./profile.json")
        self.resume_docx = ResumeDocx(profile=profile)
    
    def test_resume_docx_instance(self):
        self.assertIsInstance(self.resume_docx, ResumeDocx)
        self.assertIsInstance(self.resume_docx, object)
        self.resume_docx.generate()

class ResumePdf(unittest.TestCase):
    pass

class ResumeMarkDown(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
