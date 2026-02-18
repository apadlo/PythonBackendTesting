# Python Backend Testing Framework

[![Branch Protection](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml/badge.svg)](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml)

A comprehensive Python automation framework demonstrating backend testing capabilities including API testing, database operations, web scraping, SSH connectivity, and BDD test implementation. This project showcases various Python testing modules and techniques for end-to-end backend/server-side automation.

> **Note**: This repository implements branch protection via CI workflows and governance files. See [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md) for details.

## 🚀 Features

- **API Automation**: RESTful API testing with requests library
  - GET, POST, PUT, DELETE operations
  - Authentication handling
  - Response validation and parsing
  
- **Database Testing**: MySQL database connectivity and operations
  - CRUD operations on database tables
  - Multiple result set handling
  - Database-driven test data management

- **BDD Framework**: Behavior-driven development implementation
  - Behave framework integration
  - Feature files with Gherkin syntax
  - Step definitions and scenarios

- **File Processing**: Data handling capabilities
  - JSON parsing and manipulation
  - CSV file reading and writing
  - Dynamic payload generation

- **SSH Automation**: Remote server interactions
  - SSH connection via Paramiko
  - Remote command execution
  - File upload/download operations
  - Batch job management

- **Web Scraping**: Data extraction from web pages
  - BeautifulSoup integration
  - HTML parsing
  - Content extraction techniques

## 🛠️ Technologies Used

- **Python 3.x**
- **requests** - HTTP library for API testing
- **mysql-connector-python** - MySQL database connectivity
- **paramiko** - SSH protocol implementation
- **beautifulsoup4** - Web scraping and HTML parsing
- **behave** - BDD framework for Python
- **configparser** - Configuration file management

## 📋 Prerequisites

- Python 3.7 or higher
- MySQL Server (for database testing)
- SSH server access (for SSH demos)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/apadlo/PythonBackendTesting.git
cd PythonBackendTesting
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
   - Copy `utilities/properties.ini.example` to `utilities/properties.ini` and update values as needed
   - Or set environment variables (CI-friendly): `API_ENDPOINT`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`
   - For GitHub API BDD scenario, set: `GITHUB_USERNAME`, `GITHUB_TOKEN`

## 📁 Project Structure

```
PythonBackendTesting/
├── apiValidations.py         # API GET request validation examples
├── postAPIexample.py          # API POST/DELETE examples with authentication
├── dbDemo.py                  # Database connection and operations
├── csvDemo.py                 # CSV file reading and parsing
├── jsonParser.py              # JSON parsing examples
├── webScrapping.py            # Web scraping implementation
├── sshConnectDemo.py          # SSH connectivity and file operations
├── payLoad.py                 # Dynamic payload generation
├── features/                  # BDD test scenarios
│   ├── BookAPI.feature        # API testing scenarios
│   ├── environment.py         # Test setup and teardown
│   └── steps/                 # Step definitions
├── utilities/                 # Helper modules
│   ├── configurations.py      # Configuration management
│   └── resources.py           # Resource paths and endpoints
└── requirements.txt           # Project dependencies
```

## 🎯 Usage Examples

### Running Pytest Test Suite (recommended)
```bash
pytest
```

Run only API contract tests:
```bash
pytest tests/test_api_contracts.py -v
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
- JSON parsing and manipulation with Python modules
- API automation using the requests library
- CRUD operations (GET, POST, DELETE, PUT) automation
- API response parsing with Python utilities
- Database interactions with Python SQL Connector
- BDD automation framework development from scratch
- Reading multiple result sets from database tables
- Integrating database readers with API calls to build payloads
- CSV parsing with Python modules
- Reading and writing to CSV files
- Interacting with Linux servers
- Establishing SSH connections using Python Paramiko
- Executing commands and jobs on remote servers through Python
- Uploading and downloading batch job files from servers with Paramiko
- Web scraping techniques for data extraction
- Content extraction from web pages using BeautifulSoup

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- Branch protection policies
- Code quality standards
- Pull request process
- Security best practices

Before contributing, please review:
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [SECURITY.md](SECURITY.md) - Security policy
- [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md) - Branch protection details

## 📝 License

This project is available for educational and portfolio purposes.

## 👤 Author

**apadlo**

Feel free to explore the code and use it as a reference for your backend automation projects!
