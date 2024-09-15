import re


class MarkdownToHtml:
    @staticmethod
    def __replace_header(match):
        # method to convert headers (h1 to h6) and replace headers
        level = len(match.group(1))  # Number of '#' symbols determines header level
        content = match.group(2)  # Header content
        if level == 1:
            return f'<h1>{content}</h1>'
        elif level == 2:
            return f'<h2>{content}</h2>'
        elif level == 3:
            return f'<h3>{content}</h3>'
        elif level == 4:
            return f'<h4>{content}</h4>'
        elif level == 5:
            return f'<h5>{content}</h5>'
        elif level == 6:
            return f'<h6>{content}</h6>'

    @staticmethod
    def markdown_to_html(markdown_text: str) -> str:

        # convert headers (h1 to h6)
        markdown_text = re.sub(r'^(#{1,6}) (.*)', MarkdownToHtml.__replace_header, markdown_text, flags=re.MULTILINE)

        # Convert links [Link text](https://www.example.com)
        markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_text)

        # Convert paragraphs
        # Split the text into lines and process them
        lines = markdown_text.split('\n')
        html_lines = []
        paragraph_buffer = []

        for line in lines:
            if re.match(r'<h[1-6]>', line):  # Line is a header
                html_lines.append(line)
            elif line.strip():  # Non-empty line (part of a paragraph)
                paragraph_buffer.append(line)
            else:  # Empty line, ends a paragraph
                if paragraph_buffer:
                    # Join the buffered lines as a paragraph
                    html_lines.append(f"<p>{' '.join(paragraph_buffer).strip()}</p>")
                    paragraph_buffer = []

        # Handle any remaining text in the buffer
        if paragraph_buffer:
            html_lines.append(f"<p>{' '.join(paragraph_buffer).strip()}</p>")

        # Join all HTML lines together
        html = '\n\n'.join(html_lines)

        return html
