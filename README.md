# Python Backend Testing Framework

[![Branch Protection](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml/badge.svg)](https://github.com/apadlo/PythonBackendTesting/actions/workflows/branch-protection.yml)

A Python learning project for backend test automation: API testing, data validation, config-driven workflows, and BDD scenarios.

## Highlights

- API automation with `requests`
- Config-driven setup (`env vars` + optional `utilities/properties.ini`)
- Database helper layer for MySQL examples
- BDD scenarios with `behave`
- Lightweight pytest suite for API contracts and config behavior

## Quick Start

### 1) Clone and install

```bash
git clone https://github.com/apadlo/PythonBackendTesting.git
cd PythonBackendTesting
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Configure runtime values

Use environment variables (recommended):

```bash
export API_ENDPOINT="https://your-api-host.example.com"
export DB_USER="your_user"
export DB_PASSWORD="your_password"
export DB_HOST="your_host"
export DB_NAME="your_database"
export GITHUB_USERNAME="your_github_user"
export GITHUB_TOKEN="your_github_token"
```

Or copy and fill local config:

```bash
cp utilities/properties.ini.example utilities/properties.ini
```

> `utilities/properties.ini` is gitignored by default.

## Running Tests

### Pytest (recommended)

```bash
pytest -q
```

Run specific tests:

```bash
pytest tests/test_api_contracts.py -v
pytest tests/test_payloads_and_config.py -v
```

### Behave

```bash
behave features/BookAPI.feature
```

## Project Layout

```text
PythonBackendTesting/
├── tests/                       # pytest tests
├── features/                    # behave features and steps
├── utilities/                   # config + helper modules
├── apiValidations.py            # script-style API checks
├── postAPIexample.py            # add/delete book demo
├── dbDemo.py                    # DB usage demo
├── README.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## Security Notes

- Do not commit credentials, tokens, or private keys.
- Use environment variables for secrets.
- Use `utilities/properties.ini.example` only as a template.
- See [SECURITY.md](SECURITY.md) for vulnerability reporting and policy.

## CI Example

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q --maxfail=1 --disable-warnings --junitxml=reports/pytest.xml
```

## Contributing

Please review:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SECURITY.md](SECURITY.md)
- [BRANCH_PROTECTION.md](BRANCH_PROTECTION.md)

## License

Educational / portfolio use.
