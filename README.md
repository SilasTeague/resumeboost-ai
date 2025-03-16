# ResumeBoost AI

ResumeBoost AI is a Flask-based web application that leverages OpenAI's API to analyze resumes and suggest industry-relevant keywords and optimizations based on job descriptions. The application provides an intuitive interface for users to upload their resumes and receive tailored improvements to enhance their job prospects.

## Getting Started

Follow these instructions to set up ResumeBoost AI on your local machine for development and testing. See the Deployment section for notes on deploying the project in a live environment.

### Prerequisites

Before installing, ensure you have the following:
- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI API Key](https://platform.openai.com/signup/)
- [pip (Python Package Installer)](https://pip.pypa.io/en/stable/)

### Installing

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/resumeboost-ai.git
cd resumeboost-ai
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows, use set instead of export
```

Run the Flask application:

```bash
flask run
```

Visit `http://127.0.0.1:5000/` in your browser to access the app.

## Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [OpenAI API](https://platform.openai.com/) - Resume optimization engine


## Authors

- **Silas Teague** - *Initial Development* - (https://github.com/SilasTeague)
