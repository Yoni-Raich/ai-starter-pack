# Gemini Chat Example

A simple example of using Google's Gemini Pro API for text generation.

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file and add your Google API key:
```
GOOGLE_API_KEY=your-api-key-here
```

You can get an API key from: https://makersuite.google.com/app/apikey

## Usage

```python
from simple_gemini_chat import chat_with_gemini

# Ask a question
question = "What is the capital of France?"
answer = chat_with_gemini(question)
print(answer)
```

## Features

- Simple function to query Gemini Pro
- Error handling
- Environment variable support
- Multi-language support

## System Requirements

- Python 3.7+
- Internet connection
- Google API key
