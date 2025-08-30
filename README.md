# Text2Voice Highlight App

This is a simple Flask web application that converts text into speech
with **highlighted text tracking** while reading.\
It also includes controls to **play, pause, resume, and stop** the
speech.

## Features

-   Enter text and listen with **speech synthesis**.
-   Text is highlighted as it is spoken.
-   Controls: **Speak, Pause, Resume, Stop**.
-   Responsive UI with a clean design.

## Installation

1.  Clone this repository:

    ``` bash
    git clone https://github.com/0xScriptSmith/Text2Voice.git
    cd Text2Voice
    ```

2.  Create a virtual environment and install Flask:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # On Windows use venv\Scripts\activate
    pip install flask
    ```

3.  Run the application:

    ``` bash
    python app.py
    ```

4.  Open your browser and go to:

        http://127.0.0.1:5000

## Project Structure

    text2voice-highlight/
    │── app.py          # Main Flask app
    │── README.md       # Documentation
    │── static/
    │    └── style.css  # Stylesheet

## Dependencies

-   Python 3.7+
-   Flask

## License

This project is licensed under the MIT License.
