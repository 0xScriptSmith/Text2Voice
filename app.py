from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Text2Voice Highlight</title>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <h2>Text2Voice with Highlight & Controls</h2>
  <textarea id="textInput" placeholder="Enter text..."></textarea><br><br>
  <button onclick="speak()">Speak</button>
  <button onclick="pause()">Pause</button>
  <button onclick="resume()">Resume</button>
  <button onclick="stop()">Stop</button>

  <div id="output"></div>

<script>
let utterance;

function speak() {
  stop();
  const text = document.getElementById('textInput').value.trim();
  if (!text) return;

  const outputDiv = document.getElementById('output');
  outputDiv.innerHTML = "";
  for (let i = 0; i < text.length; i++) {
    const span = document.createElement('span');
    span.textContent = text[i];
    outputDiv.appendChild(span);
  }

  utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 1;

  utterance.onboundary = function(event) {
    if (event.name === 'word') {
      const spans = document.querySelectorAll('#output span');
      spans.forEach(span => span.classList.remove('highlight'));
      for (let i = event.charIndex; i < event.charIndex + event.charLength && i < spans.length; i++) {
        spans[i].classList.add('highlight');
      }
    }
  };

  utterance.onend = function() {
    document.querySelectorAll('#output span').forEach(span => span.classList.remove('highlight'));
  };

  speechSynthesis.speak(utterance);
}

function pause() {
  speechSynthesis.pause();
}

function resume() {
  speechSynthesis.resume();
}

function stop() {
  speechSynthesis.cancel();
  document.querySelectorAll('#output span').forEach(span => span.classList.remove('highlight'));
}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

# Route to serve style.css from project root
@app.route("/style.css")
def css():
    return send_from_directory(os.path.dirname(__file__), "style.css")

if __name__ == "__main__":
    app.run(debug=True)
