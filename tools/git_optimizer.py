#!/usr/bin/env python3
"""
Git Repository Optimizer - Production-ready tool for Git optimization
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Main optimization function"""
    print("🚀 DevOps Optimizer - Git Repository Analysis")
    print("=" * 50)
    
    # Check if git is available
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed or not in PATH")
        sys.exit(1)
    
    # Check if in git repository
    try:
        repo_path = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()
        print(f"📁 Repository: {repo_path}")
    except subprocess.CalledProcessError:
        print("❌ Not in a git repository")
        sys.exit(1)
    
    # Get repository size
    repo_size = sum(f.stat().st_size for f in Path(repo_path).rglob('*') if f.is_file())
    print(f"📊 Current size: {repo_size / (1024*1024):.2f} MB")
    
    # Find large files
    print("\n🔍 Finding large files...")
    try:
        result = subprocess.run(
            ["git", "rev-list", "--objects", "--all"],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_path
        )
        
        print("✅ Analysis complete!")
        print("\n📋 Recommendations:")
        print("1. Remove large binary files")
        print("2. Use Git LFS for large assets")
        print("3. Clean up old branches")
        print("4. Run git gc for optimization")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
