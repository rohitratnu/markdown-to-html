# Markdown to HTML Converter with Flask

This is a simple Flask web application that converts Markdown text into HTML. It uses a custom Markdown-to-HTML converter function to process Markdown input and render the resulting HTML on a web page.

## Project Structure

- `app.py`: The main Flask application file.
- `src/markdown_to_html.py`: Contains the `markdown_to_html` class for converting Markdown text to HTML.
- `templates/index.html`: The HTML template used to render the input form and the converted HTML output.

## Features

- **Markdown to HTML Conversion**: Converts Markdown headers, links, and paragraphs into HTML.
- **Web Interface**: A web form for users to input Markdown text and see the HTML output.

## Installation

Installation can be done via running the project locally on through docker

### Installing and running on Machine using python

 1. **Prerequisite must have python 3.10 or higher version**:
 2. cd in to `markdown-to-html`.
 3. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate
  ``` 
4. **Install Dependencies**:
```bash
pip install requirements.txt 
```

## Usage

 1. Run the Flask Application: 
```bash 
python app.py
```
 1. Open Your Web Browser and go to `http://127.0.0.1:3000/`. You should see a web form where you can enter Markdown text.
 2. Submit Markdown:
   - Enter your Markdown text in the form.
   - Open the Network Tab to check the api request and response
   - Click the "Convert" button to see the HTML output.
   - Check the response in Network Tab in browser to see the html response body as output under `<h2>HTML Output</h2>`

## Code Explanation

- `app.py`:
  - Defines the Flask application and routes.
  - Handles GET and POST requests to display and process Markdown text.
- `src/markdown_to_html.py`:
  - Contains the markdown_to_html class that converts Markdown text into HTML.
  - replace_header(match) method converts Markdown headers to HTML tags.
  - Handles conversion of links and paragraphs.

## Testing

 1. Run Tests with Coverage:
```bash
coverage run -m unittest discover
```
 2. Generate Coverage Report on Terminal:
```bash
coverage report
```
  - The above commands will generate a report on Terminal
 3. Generate Coverage Report on Terminal:
```bash
coverage html
```
  - The above commands will generate an HTML report in an `htmlcov` directory. Open `index.html` in your browser to see the coverage details.


### Installing and running using docker
 1. **Prerequisit must have Docker version 25 or higher**:
2. Run the following command  to run the application `docker compose -f docker-compose.yml up`
   - this downloads python image and install all dependencies from Docker file and run the app.
3. Open Your Web Browser and go to `http://0.0.0.0:3000/`. You should see a web form where you can enter Markdown text.
4. Submit Markdown:
   - Enter your Markdown text in the form.
   - Click the "Convert" button to see the HTML output.
5. To close the app on docker run `docker compose -f docker-compose.yml down`
6. To delete the image `docker rmi markdown-to-html-main-web`
