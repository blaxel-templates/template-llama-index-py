# Blaxel LlamaIndex Agent

<p align="center">
  <img src="https://blaxel.ai/logo.png" alt="Blaxel" width="200"/>
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-powered-brightgreen.svg)](https://www.llamaindex.ai/)
[![GPT-4](https://img.shields.io/badge/GPT--4-enabled-orange.svg)](https://openai.com/gpt-4)

</div>

A template implementation of a conversational agent using LlamaIndex and GPT-4. This agent demonstrates the power of LlamaIndex for building interactive AI agents with advanced document processing, retrieval-augmented generation (RAG), and tool integration capabilities.

## 📑 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-the-server-locally)
  - [Testing](#testing-your-agent)
  - [Deployment](#deploying-to-blaxel)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## ✨ Features

- Interactive conversational interface with document understanding
- Advanced retrieval-augmented generation (RAG) capabilities
- Tool integration support (including weather and search capabilities)
- Streaming responses for real-time interaction
- Built on LlamaIndex for sophisticated document processing and indexing
- Vector store integration for semantic search
- Easy deployment and integration with Blaxel platform

## 🚀 Quick Start

For those who want to get up and running quickly:

```bash
# Clone the repository
git clone https://github.com/blaxel-ai/template-llama-index-py.git

# Navigate to the project directory
cd template-llama-index-py

# Install dependencies
uv sync

# Start the server
bl serve --hotreload

# In another terminal, test the agent
bl chat --local blaxel-agent
```

## 📋 Prerequisites

- **Python:** 3.10 or later
- **[UV](https://github.com/astral-sh/uv):** An extremely fast Python package and project manager, written in Rust
- **Blaxel Platform Setup:** Complete Blaxel setup by following the [quickstart guide](https://docs.blaxel.ai/Get-started#quickstart)
  - **[Blaxel CLI](https://docs.blaxel.ai/Get-started):** Ensure you have the Blaxel CLI installed. If not, install it globally:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=/usr/local/bin sudo -E sh
    ```
  - **Blaxel login:** Login to Blaxel platform
    ```bash
    bl login YOUR-WORKSPACE
    ```

## 💻 Installation

**Clone the repository and install dependencies:**

```bash
git clone https://github.com/blaxel-ai/template-llama-index-py.git
cd template-llama-index-py
uv sync
```
## 🔧 Usage

### Running Locally

Start the development server with hot reloading:

```bash
bl serve --hotreload
```

For production run:

```bash
bl serve
```

_Note:_ The development server automatically restarts when you make changes to the source code.

### Testing

You can test your LlamaIndex agent locally:

```bash
# Using the Blaxel CLI chat interface
bl chat --local blaxel-agent
```

Example queries you can test:

```
What information do you have about renewable energy?
```

```
Can you search through the documents for climate change data?
```

```
Summarize the key points from the uploaded documents
```

You can also run it directly with specific input:

```bash
bl run agent blaxel-agent --local --data '{"input": "What is the weather in Paris?"}'
```

### Deployment

When you are ready to deploy your agent:

```bash
bl deploy
```

This command uses your code and the configuration files under the `.blaxel` directory to deploy your LlamaIndex agent on the Blaxel platform.

## 📁 Project Structure

- **src/main.py** - Application entry point and FastAPI server setup
- **src/agent.py** - Core agent implementation with LlamaIndex integration
- **src/server/** - Server implementation and routing
  - **router.py** - API route definitions
  - **middleware.py** - Request/response middleware
- **src/data/** - Document storage and processing utilities
- **src/indices/** - Vector store and index configurations
- **pyproject.toml** - UV package manager configuration with dependencies
- **blaxel.toml** - Blaxel deployment configuration
- **LICENSE** - MIT license file

## ❓ Troubleshooting

### Common Issues

1. **Blaxel Platform Issues**:
   - Ensure you're logged in to your workspace: `bl login MY-WORKSPACE`
   - Verify models are available: `bl get models`
   - Check that functions exist: `bl get functions`

2. **Python Environment Issues**:
   - Make sure you have Python 3.10+
   - Try `uv sync --refresh --force-reinstall` to refresh dependencies
   - Check for conflicting package versions
   - Verify virtual environment activation with UV

For more help, please [submit an issue](https://github.com/blaxel-templates/template-llama-index-py/issues) on GitHub.

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Submit** a Pull Request

Please make sure to update tests as appropriate and follow the code style of the project.

## 🆘 Support

If you need help with this template:

- [Submit an issue](https://github.com/blaxel-templates/template-llama-index-py/issues) for bug reports or feature requests
- Visit the [Blaxel Documentation](https://docs.blaxel.ai) for platform guidance
- Check the [LlamaIndex Documentation](https://docs.llamaindex.ai/) for framework-specific help
- Join our [Discord Community](https://discord.gg/G3NqzUPcHP) for real-time assistance

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
