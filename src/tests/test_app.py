import unittest
from unittest.mock import patch
from app import app  # Import the Flask app from the main application file


class TestMarkdownToHtml(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.MarkdownToHtml.markdown_to_html')
    def test_index_get(self, mock_markdown_to_html):
        # Test the GET request to the index page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form', response.data)  # Check if the form is in the response

    @patch('app.MarkdownToHtml.markdown_to_html')
    def test_index_post(self, mock_markdown_to_html):
        # Test the POST request to the index page which calls markdown down function and return rendered html
        # Mock the markdown_to_html function to return a fake HTML output
        mock_markdown_to_html.return_value = '<p>Mocked HTML output</p>'

        # Send a POST request to the index page
        response = self.app.post('/', data={'markdown': '# Header'}, follow_redirects=True)

        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the mocked HTML output is in the response
        self.assertIn(b'<p>Mocked HTML output</p>', response.data)

        # Ensure that the markdown_to_html was called with the correct argument
        mock_markdown_to_html.assert_called_once_with('# Header')
