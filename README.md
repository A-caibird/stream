# AI Chat with Streaming Response

A simple yet elegant chat application that demonstrates real-time AI response streaming, similar to ChatGPT's interface. This application shows responses character by character, creating a more engaging and interactive user experience.

![AI Chat Demo](https://via.placeholder.com/800x400?text=AI+Chat+Demo)

## Features

- ✨ Real-time streaming responses
- 🚀 Fast and lightweight implementation
- 💬 Clean and intuitive chat interface
- 🔄 Simulated AI response generation
- 🌐 Single-server architecture (backend serves frontend)

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **API**: RESTful with streaming response
- **Deployment**: Local development server

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository or download the source code:

```bash
git clone https://github.com/yourusername/ai-chat-streaming.git
cd ai-chat-streaming
```

2. Install the required Python packages:

```bash
pip install fastapi uvicorn pydantic
```

3. Make sure your project structure looks like this:

```
project-directory/
  ├── main.py
  └── static/
      └── index.html
```

### Running the Application

1. Start the server:

```bash
python main.py
```

2. Open your browser and navigate to:

```
http://localhost:8000
```

## How It Works

### Backend (FastAPI)

- Creates a streaming response endpoint at `/api/chat`
- Simulates AI processing with timed chunks of text
- Serves the static frontend files
- Handles API requests from the frontend

### Frontend (HTML/JS)

- Provides a user-friendly chat interface
- Sends user queries to the backend API
- Processes the streaming response
- Updates the UI in real-time as responses arrive

## Customization

### Modifying the AI Response

Edit the `fake_ai_processing` function in `main.py` to change the simulated AI responses:

```python
chunks = [
    "Your custom ",
    "response here, ",
    "broken into chunks ",
    "for streaming effect."
]
```

### Styling the Interface

The CSS styles are embedded in the `index.html` file. Modify them to match your design preferences.

## Integration with Real AI

To connect this application with a real AI service:

1. Replace the `fake_ai_processing` function with API calls to your preferred AI provider
2. Ensure your AI provider supports streaming responses
3. Update the response format to match your AI service

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by modern AI chat interfaces
- Built with FastAPI's excellent streaming response capabilities
- Designed for educational purposes

---

*Note: This is a demonstration project and not intended for production use without further security enhancements.*
