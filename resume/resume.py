"""A simple resume module"""

from resume.docx import ResumeDocx
from resume.pdf import ResumePdf
from resume.markdown import ResumeMarkDown

class Resume(ResumeDocx, ResumePdf, ResumeMarkDown):
    """A simple Resume class to generate resume in docx, markdown and pdf"""

    def __init__(self, *mode, **profile):
        """Initialize Resume instance"""
        self._mode = mode
        self._profile = profile
        self._generator = {
            'docx': ResumeDocx,
            'pdf': ResumePdf,
            'markdown': ResumeMarkDown
        }

    def generate(self):
        for key in self._generator.keys():
            if key in self._mode:
                self._generator[self._mode].generate()


    