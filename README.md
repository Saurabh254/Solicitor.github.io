# Solicitor

A Discord utility bot and web showcase built with Python (`discord.py`) and modern web technologies.

> [!NOTE]
> Created for personal and educational use.

---

## Features

- **Discord Utility Bot (`main.py`)**:
  - Built with `discord.py` extension commands.
  - Custom command prefix support (`Plz`, `plz`).
  - Automated background cleanup tasks and status presence.
  - Configurable event listeners for message tracking and utilities.
- **Web Landing Page (`index.html`)**:
  - Responsive web showcase styled with SCSS / CSS.
  - Interactive UI components powered by JavaScript.

---

## Project Structure

```
.
├── main.py             # Discord bot entry point
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment process definition
├── index.html          # Web landing page
├── main.js             # Client-side JavaScript
├── scss/               # SCSS stylesheet sources
└── style.css           # Compiled stylesheets
```

---

## Setup & Installation

### 1. Discord Bot Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Saurabh254/Solicitor.github.io.git
   cd Solicitor.github.io
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Discord bot token in `main.py` or via environment variables.
4. Run the bot:
   ```bash
   python main.py
   ```

### 2. Web Landing Page

Open `index.html` in any web browser or serve it locally:
```bash
python -m http.server 8000
```

---

## License

Educational / Personal Use.
