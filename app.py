import logging
from flask import Flask, render_template, request
from src.markdown_to_html import MarkdownToHtml

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        markdown_text = request.form.get('markdown', '')
        app.logger.info('Received POST request with markdown text.')

        try:
            html_output = MarkdownToHtml.markdown_to_html(markdown_text)
            app.logger.debug(f'Converted Markdown to HTML: {html_output}')
        except Exception as e:
            app.logger.error(f'Error during Markdown to HTML conversion: {e}', exc_info=True)
            html_output = 'An error occurred during conversion.'

        return render_template('index.html', markdown=markdown_text, html_output=html_output)

    app.logger.info('Rendering index page for GET request.')
    return render_template('index.html')


if __name__ == '__main__':
    app.logger.info('Starting the Flask application.')
    app.run(host="0.0.0.0", port=3000, debug=True)
