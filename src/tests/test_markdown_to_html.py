import unittest
from app import MarkdownToHtml


class TestMarkdownToHtml(unittest.TestCase):

    def test_header_conversion(self):
        self.assertEqual(MarkdownToHtml.markdown_to_html('# Header one'), '<h1>Header one</h1>')
        self.assertEqual(MarkdownToHtml.markdown_to_html('## Header two'), '<h2>Header two</h2>')
        self.assertEqual(MarkdownToHtml.markdown_to_html('### Header three'), '<h3>Header three</h3>')
        self.assertEqual(MarkdownToHtml.markdown_to_html('#### Header four'), '<h4>Header four</h4>')
        self.assertEqual(MarkdownToHtml.markdown_to_html('##### Header five'), '<h5>Header five</h5>')
        self.assertEqual(MarkdownToHtml.markdown_to_html('###### Header six'), '<h6>Header six</h6>')

    def test_paragraph_conversion(self):
        self.assertEqual(MarkdownToHtml.markdown_to_html('This is a paragraph.'), '<p>This is a paragraph.</p>')

    def test_multiple_paragraphs(self):
        input_text = 'First paragraph.\n\nSecond paragraph.'
        expected_output = '<p>First paragraph.</p>\n\n<p>Second paragraph.</p>'
        self.assertEqual(MarkdownToHtml.markdown_to_html(input_text), expected_output)

    def test_link_conversion(self):
        self.assertEqual(MarkdownToHtml.markdown_to_html('[OpenAI](https://www.openai.com)'),
                         '<p><a href="https://www.openai.com">OpenAI</a></p>')

    def test_complex_markdown(self):
        input_text = '''
# Header one

Hello there

How are you?
What's going on?

## Another Header

This is a paragraph [with an inline link](http://google.com). Neat, eh?

## This is a header [with a link](http://yahoo.com)'''
        expected_output = (
            '<h1>Header one</h1>\n\n'
            '<p>Hello there</p>\n\n'
            "<p>How are you? What's going on?</p>\n\n"
            '<h2>Another Header</h2>\n\n'
            '<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>\n\n'
            '<h2>This is a header <a href="http://yahoo.com">with a link</a></h2>'
        )
        self.assertEqual(MarkdownToHtml.markdown_to_html(input_text.strip()), expected_output)
