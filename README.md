# 🚀 Mini-RAG: Lightweight Retrieval-Augmented Generation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **A minimal yet powerful implementation of Retrieval-Augmented Generation (RAG) using the LLM Factory Pattern for efficient semantic search and intelligent question answering.**

## 📋 Overview

Mini-RAG is a lightweight implementation of the Retrieval-Augmented Generation model optimized for question answering tasks. It combines document retrieval with language model generation using a factory pattern for flexible LLM integration, making it easy to swap between different language models while maintaining clean architecture.

## ✨ Key Features

- **Lightweight Architecture**: Minimal dependencies, easy to understand and extend
- **LLM Factory Pattern**: Flexible language model integration (OpenAI, HuggingFace, local models)
- **Semantic Search**: Efficient document retrieval using embeddings
- **Question Answering**: Generate context-aware answers from retrieved documents
- **Configurable Pipeline**: Customize retrieval and generation strategies
- **Production Ready**: Clean code structure suitable for deployment

## 📦 Requirements

- Python 3.8 or later
- pip or conda package manager

### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)

2) Create a new environment using the following command:
```bash
conda create -n mini-rag python=3.8
```

3) Activate the environment:
```bash
conda activate mini-rag
```

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Elkadeem1/Mini-RAG.git
cd Mini-RAG

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Quick Start

```python
from mini_rag import RAGSystem

# Initialize RAG system
rag = RAGSystem()

# Add documents
rag.add_documents([
    "Python is a high-level programming language.",
    "Machine learning is a subset of artificial intelligence."
])

# Ask questions
response = rag.answer("What is Python?")
print(response)
```

## 📁 Project Structure

```
Mini-RAG/
├── src/
│   ├── llm_factory.py        # LLM factory pattern implementation
│   ├── retriever.py          # Document retrieval logic
│   ├── generator.py          # Response generation logic
│   └── utils.py              # Utility functions
├── examples/
│   ├── basic_qa.py           # Basic question answering example
│   └── advanced_usage.py      # Advanced usage patterns
├── tests/
│   └── test_rag.py           # Unit tests
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## 🏗️ Architecture

```
User Query
    ↓
[Retriever] → Semantic Search → Top-K Documents
    ↓
[Generator] → LLM Processing → Final Answer
    ↓
Response
```

## 🔌 Configuration

Configure the RAG system via `config.yaml` or programmatically:

```python
config = {
    'model_name': 'gpt-3.5-turbo',
    'embedding_model': 'text-embedding-ada-002',
    'retrieval_top_k': 5,
    'max_tokens': 500
}
```

## 📚 Dependencies

Key dependencies (see `requirements.txt` for complete list):
- `python-dotenv` - Environment variable management
- `requests` - HTTP library
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning utilities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions and support:
- Email: mahmoudelkadeem32@gmail.com
- GitHub Issues: [Report Issues](https://github.com/Elkadeem1/Mini-RAG/issues)

## 🙏 Acknowledgments

- Inspired by leading RAG research and implementations
- Built with modern Python best practices
- Community-driven improvements welcome

---


