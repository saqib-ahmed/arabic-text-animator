#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

def get_current_version() -> str:
    init_file = Path("arabic_animations/__init__.py")
    content = init_file.read_text()
    match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
    if not match:
        raise ValueError("Version not found in __init__.py")
    return match.group(1)

def bump_version(version: str, bump_type: str) -> str:
    major, minor, patch = map(int, version.split('.'))
    if bump_type == 'major':
        return f"{major + 1}.0.0"
    elif bump_type == 'minor':
        return f"{major}.{minor + 1}.0"
    elif bump_type == 'patch':
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"Invalid bump type: {bump_type}")

def update_version(new_version: str) -> None:
    init_file = Path("arabic_animations/__init__.py")
    content = init_file.read_text()
    new_content = re.sub(
        r'__version__\s*=\s*["\']([^"\']+)["\']',
        f'__version__ = "{new_version}"',
        content
    )
    init_file.write_text(new_content)

def main():
    # Get current version
    current = get_current_version()
    print(f"Current version: {current}")

    # Get bump type
    bump_type = input("Enter bump type (major/minor/patch): ").lower()
    if bump_type not in ('major', 'minor', 'patch'):
        print("Invalid bump type")
        return

    # Calculate new version
    new_version = bump_version(current, bump_type)
    print(f"New version will be: {new_version}")

    # Confirm
    if input("Continue? (y/n): ").lower() != 'y':
        return

    # Update version in files
    update_version(new_version)

    # Git commands
    subprocess.run(["git", "add", "arabic_animations/__init__.py"])
    subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"])
    subprocess.run(["git", "tag", f"v{new_version}"])

    print(f"\nVersion bumped to {new_version}")
    print("\nNext steps:")
    print("1. Push changes: git push origin main")
    print("2. Push tags: git push origin v{new_version}")
    print("3. Wait for GitHub Actions to create release")

if __name__ == "__main__":
    main()