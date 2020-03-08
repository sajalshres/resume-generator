"""A resume generator for Microsoft word"""
import json
from docx import Document

class ResumeDocx:
    """A resume generator for Microsoft word"""

    def __init__(self, profile=None):
        """Initialize ResumeDocx instance"""
        self._document = None
        self._profile = profile
    
    @property
    def document(self):
        if self._document is None:
            self._document = Document()
        return self._document
    
    def generate(self):
        # Add Heading
        self.document.add_heading("Sajal Narayan Shrestha", level=0)
        self.document.save("resume.docx")
