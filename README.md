# Python Backend Testing Framework

[![Branch Protection](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml/badge.svg)](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml)

A comprehensive Python automation framework for backend testing practice, including API testing, database operations, web scraping, SSH connectivity demos, and BDD scenarios.  
It now also includes a modernized **pytest** layer focused on resilient API contracts and config-driven behavior.

> **Note**: This repository implements branch protection via CI workflows and governance files. See [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md) for details.

## 🚀 Features

- **API Automation**: REST API testing with `requests`
  - GET, POST, PUT, DELETE operations
  - Authentication handling
  - Response validation and parsing

- **Pytest Test Layer (modernized)**
  - Contract-style checks in `tests/test_api_contracts.py`
  - Config and payload behavior tests in `tests/test_payloads_and_config.py`
  - Better handling for network instability and fallback behavior

- **Database Testing**: MySQL connectivity and operations
  - CRUD operations on database tables
  - Multiple result set handling
  - Database-driven test data management

- **BDD Framework**: Behavior-driven development with `behave`
  - Feature files with Gherkin syntax
  - Step definitions and scenarios

- **File Processing**
  - JSON parsing and manipulation
  - CSV file reading and writing
  - Dynamic payload generation

- **SSH Automation (demo scripts)**
  - SSH connection via Paramiko
  - Remote command execution
  - File upload/download operations

- **Web Scraping (demo scripts)**
  - BeautifulSoup integration
  - HTML parsing and content extraction

## 🛠️ Technologies Used

- **Python 3.x**
- **pytest** - modern test runner for API contracts/config tests
- **requests** - HTTP library for API testing
- **mysql-connector-python** - MySQL database connectivity
- **paramiko** - SSH protocol implementation
- **beautifulsoup4** - Web scraping and HTML parsing
- **behave** - BDD framework for Python
- **configparser** - Configuration file management

## 📋 Prerequisites

- Python 3.8+
- MySQL Server (for database testing demos)
- SSH server access (for SSH demos)

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/apadlo/PythonBackendTesting.git
cd PythonBackendTesting
```

2. Install required dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure your environment:
   - Recommended: set environment variables
     - `API_ENDPOINT`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`
     - for GitHub API scenario: `GITHUB_USERNAME`, `GITHUB_TOKEN`
   - Or copy `utilities/properties.ini.example` to `utilities/properties.ini` and fill local values

> `utilities/properties.ini` is gitignored by default and should not be committed.

## 📁 Project Structure

```text
PythonBackendTesting/
├── tests/                     # pytest tests (contract + config/payload)
├── features/                  # behave features and steps
├── utilities/                 # config + helper modules
├── apiValidations.py          # script-style API validation examples
├── postAPIexample.py          # API POST/DELETE example
├── dbDemo.py                  # Database demo
├── csvDemo.py                 # CSV parsing demo
├── jsonParser.py              # JSON parsing demo
├── webScrapping.py            # Web scraping demo
├── sshConnectDemo.py          # SSH demo
├── payLoad.py                 # Dynamic payload helper
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
└── BRANCH_PROTECTION.md
```

## 🎯 Usage Examples

### Running Pytest Test Suite (recommended)

```bash
pytest -q
```

Run specific suites:

```bash
pytest tests/test_api_contracts.py -v
pytest tests/test_payloads_and_config.py -v
```

### Running legacy script-style API demos

```bash
python apiValidations.py
python postAPIexample.py
```

### Running BDD Tests

```bash
behave features/BookAPI.feature
```

### Database Operations

```bash
python dbDemo.py
```

### SSH File Operations

```bash
python sshConnectDemo.py
```

### Web Scraping

```bash
python webScrapping.py
```

## 🤖 Jenkins / CI Commands

Install and run tests in a pipeline shell step:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q --maxfail=1 --disable-warnings --junitxml=reports/pytest.xml
```

Optional (BDD):

```bash
behave --junit --junit-directory reports/behave
```

## 💡 Key Learning Points

This project demonstrates:

- API automation with Python `requests`
- Contract-style validation patterns with pytest
- CRUD workflow testing (GET/POST/DELETE/PUT)
- Parsing API responses and extracting reusable data
- Database interactions using Python SQL connector
- Building BDD tests with `behave`
- Integrating config-driven test execution
- CSV and JSON data parsing techniques
- SSH-based remote operations using Paramiko
- Web scraping with BeautifulSoup

## 🤝 Contributing

We welcome contributions. Please review:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md)

## 📝 License

This project is available for educational and portfolio purposes.

## 👤 Author

**apadlo**

Feel free to explore the code and use it as a reference for backend automation learning.
