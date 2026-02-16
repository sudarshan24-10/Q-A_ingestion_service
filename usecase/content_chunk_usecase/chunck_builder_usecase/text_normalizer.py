import re

def normalize_text(text: str) -> str:

    text = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", text)

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{3,}", "\n\n", text)


    text = re.sub(
        r"(●[^\n]+)\n\n([^\n●])",
        r"\1 \2",
        text
    )

    return text.strip()
