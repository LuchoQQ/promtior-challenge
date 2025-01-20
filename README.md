# Promtior Chatbot

A RAG-based (Retrieval-Augmented Generation) chatbot implementation for Promtior company, powered by OpenAI's GPT-4 and FastAPI.

## Project Overview

This chatbot serves as an intelligent assistant for Promtior, capable of answering questions by combining information from the company's website and predefined context. The solution uses a RAG architecture to provide accurate, context-aware responses.

DEMO DEPLOY URL: https://promtior-challenge-production.up.railway.app/chat/invoke

![promtior](https://github.com/user-attachments/assets/cc0ed923-770a-45e4-88fc-99b5034db32f)



### Key Features

- RAG-based knowledge retrieval
- Integration with Promtior's website content
- Custom manual context integration
- FastAPI-based REST API
- Vector similarity search using FAISS
- OpenAI GPT-4 for response generation

## Technical Architecture

### Components

1. **FastAPI Application**
   - Provides REST API endpoints
   - Handles request/response processing
   - Implements input validation using Pydantic

2. **Knowledge Base**
   - Web Loader: Fetches content from Promtior's website
   - Text Splitter: Segments documents into manageable chunks
   - FAISS Vector Store: Enables efficient similarity search
   - Manual Context: Incorporates predefined company information

3. **RAG Pipeline**
   - Retrieval Chain: Manages document retrieval process
   - Document Chain: Combines retrieved documents with queries
   - Prompt Template: Structures context for the LLM
   - GPT-4 Integration: Generates natural language responses

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd promtior-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi langchain-openai langchain-community faiss-cpu uvicorn python-dotenv
```

4. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the server:
```bash
python server.py
```

2. The API will be available at `http://localhost:8000`

3. Send POST requests to `/chat/invoke` endpoint:
```bash
curl -X POST "http://localhost:8000/chat/invoke" \
     -H "Content-Type: application/json" \
     -d '{"input": "When was Promtior founded?"}'
```
4. You can also run this command while server is running, change client.py input string get differents answers
```bash
python client.py
```

## API Documentation

### POST /chat/invoke

Endpoint for chatbot interactions.

**Request Body:**
```json
{
    "input": "string"  // The user's question
}
```

**Response:**
```json
{
    "answer": "string"  // The chatbot's response
}
```

## Implementation Challenges and Solutions

1. **Content Integration**
   - Challenge: Combining web content with manual context effectively
   - Solution: Implemented a unified document processing pipeline that handles both sources

2. **Response Quality**
   - Challenge: Ensuring accurate and relevant responses
   - Solution: Fine-tuned prompt templates and implemented chunk overlap in text splitting

3. **Performance Optimization**
   - Challenge: Minimizing response latency
   - Solution: Utilized FAISS for efficient vector search and implemented proper chunking strategies

## Development Considerations

- The system uses GPT-4 for optimal response quality. For cost optimization, consider using GPT-3.5-turbo
- Vector store is initialized on startup; consider implementing periodic updates
- Text splitting parameters can be adjusted based on content characteristics

## Future Improvements

1. Implement caching for frequently asked questions
2. Add periodic website content updates
3. Implement conversation history
4. Add monitoring and logging
5. Enhance error handling and rate limiting

## License

[Add your license information here]
