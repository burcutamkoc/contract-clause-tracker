import re
from typing import List


def split_into_sentences(text: str) -> List[str]:
        """
        Split contract content into clean sentences.
        """

        # remove RTF header if exists
        if text.startswith("{\\rtf"):
            text = re.sub(r"{\\.*?}", "", text)

        # normalize new lines
        text = text.replace("\n", " ")

        # split sentences
        sentences = re.split(r'[.!?]+', text)

        # clean
        return [
            s.strip()
            for s in sentences
            if s.strip()
        ]