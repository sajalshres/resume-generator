"""A resume generator for Microsoft word"""
import json
from docx import Document

class ResumeDocx:
    """A resume generator for Microsoft word"""

    def __init__(self, profile):
        """Initialize ResumeDocx instance"""
        self._document = None
        self._profile = profile
    
    @property
    def document(self):
        if self._document is None:
            self._document = Document()
        return self._document
    

        

    def generate(self):
        print(f"{__name__} called.")
        return True

if __name__ == '__main__':
    with open('./profile.json') as file:
        profile = json.load(file)
    
    resume_docx = ResumeDocx(profile)
    resume_docx.generate()



