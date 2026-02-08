# Contributing to PythonBackendTesting

Thank you for your interest in contributing to the Python Backend Testing Framework! This document provides guidelines and best practices for contributing to this project.

## 🛡️ Branch Protection Policy

The `master` branch is protected to ensure code quality and stability. All contributions must follow these guidelines:

### Protected Branch Rules

1. **Direct pushes to master are not allowed**
   - All changes must go through Pull Requests
   - PRs must pass all automated checks before merging

2. **Required Status Checks**
   - Code quality checks (Pylint, Flake8)
   - Security scanning (Bandit, Safety)
   - Test suite execution
   - Python syntax validation

3. **Code Review Requirements**
   - At least one approval from CODEOWNERS
   - All review comments must be resolved
   - All CI checks must pass

## 🚀 How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/apadlo/PythonBackendTesting.git
cd PythonBackendTesting
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bug-fix
```

### 3. Make Your Changes

- Write clean, readable code
- Follow Python PEP 8 style guidelines
- Add comments for complex logic
- Update documentation if needed

### 4. Test Your Changes

```bash
# Install dependencies
pip install -r requirements.txt

# Run syntax validation
python -m py_compile *.py

# Run BDD tests (if applicable)
behave features/

# Run individual test scripts
python apiValidations.py
python postAPIexample.py
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature" # or "fix: resolve bug"
```

#### Commit Message Guidelines

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Reference to related issues
- Screenshots (if applicable)
- Testing details

## 📋 Code Quality Standards

### Python Style Guide

- Follow PEP 8 conventions
- Maximum line length: 127 characters
- Use meaningful variable and function names
- Add docstrings to functions and classes

### Security Requirements

- No hardcoded credentials or secrets
- Use environment variables for sensitive data
- Run security checks before submitting PR
- Address all critical security findings

### Testing Requirements

- Add tests for new features
- Ensure existing tests still pass
- Provide test data in appropriate formats
- Document test setup requirements

## 🔍 Code Review Process

1. **Automated Checks**
   - CI workflow runs automatically on PR
   - All checks must pass (green status)

2. **Human Review**
   - CODEOWNERS will review your PR
   - Address all feedback and comments
   - Make necessary changes and push updates

3. **Approval and Merge**
   - Once approved and all checks pass
   - Maintainer will merge your PR
   - Your contribution will be part of master!

## 🐛 Reporting Issues

If you find a bug or have a feature request:

1. Check existing issues first
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)

## 📚 Areas for Contribution

- **API Testing**: Enhance API validation capabilities
- **Database Operations**: Add new database testing features
- **BDD Scenarios**: Create more comprehensive test scenarios
- **Security**: Improve security scanning and validation
- **Documentation**: Improve or translate documentation
- **Bug Fixes**: Resolve open issues

## 💡 Need Help?

- Check the [README.md](README.md) for project overview
- Review existing code for patterns and examples
- Open an issue for questions or clarifications
- Contact @apadlo for major architectural changes

## 📜 Code of Conduct

- Be respectful and professional
- Provide constructive feedback
- Help others learn and grow
- Follow GitHub's Community Guidelines

Thank you for contributing to making this project better! 🎉
