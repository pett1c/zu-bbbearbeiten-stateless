import os

def test_gitignore_exists():
    assert os.path.exists('.gitignore'), "The .gitignore file is missing!"

def test_gitignore_content():
    with open('.gitignore', 'r') as f:
        content = f.read()
        required_patterns = ['__pycache__', '.vscode/', '.webassets-cache']
        for pattern in required_patterns:
            assert pattern in content, f"Pattern {pattern} is missing from .gitignore!"