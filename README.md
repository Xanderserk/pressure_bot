# Pressure Measurement Telegram Bot

This is a Telegram bot written in Python that allows users to track their blood pressure measurements. The bot receives pressure measurements in text format (e.g., systolic, diastolic, and pulse values), processes them using regex pattern matching, and forwards the data to a backend API for storage.

## Features

- **User Registration**: Automatically registers users when they start the bot with `/start`
- **Pressure Measurement Processing**: Processes text messages to extract blood pressure readings (systolic, diastolic, pulse) via regex pattern matching
- **Data Forwarding**: Sends extracted measurements to a backend API for storage
- **Flexible Input**: Supports various formats for blood pressure readings (e.g., "120 80 70", "120 80")

## Technologies Used

- **Python 3.12+**: Main programming language
- **Aiogram 3.22+**: Telegram bot framework
- **HTTPX**: For asynchronous HTTP requests to the backend API
- **Pytest**: For testing
- **Ruff**: For linting and formatting
- **Pyright**: For type checking

## Architecture

- **Main Bot Logic**: Located in `src/bot/main.py`
- **Service Layer**: Handles API communication in `src/bot/service_layer/services.py`
- **Regex Processing**: Text processing for extracting pressure measurements
- **Backend Integration**: Communicates with a REST API at `http://127.0.0.1:8000`

## Setup and Installation

### Prerequisites

- Python 3.12+
- UV package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root with your Telegram bot token:
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   ```

4. Ensure the backend API is running at `http://127.0.0.1:8000`

### Running the Bot

Once everything is set up, you can run the bot using one of these methods:

```bash
# Run directly with uv
uv run bot

# Or using the command defined in pyproject.toml
uv run python -c "from bot.main import run; run()"
```

## Development Commands

The project includes a Makefile with common development tasks:

```bash
# Run all checks (linting, formatting, type checking, tests)
make check

# Run linter (Ruff)
make lint

# Check code formatting (Ruff)
make format

# Run type checking (Pyright)
make type-check

# Run tests (pytest)
make tests

# Lock dependencies
make lock
```

## Regex Pattern Matching

The bot's text processing functionality matches:

- Three numbers representing systolic, diastolic, and pulse pressure (e.g., "120 80 70")
- Two numbers representing systolic and diastolic pressure (e.g., "120 80")
- Various separators between numbers (spaces, commas, semicolons)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the checks (`make check`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request