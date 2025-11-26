# UV: Python's Fast Package Manager

## What is UV?

UV is a modern, extremely fast package and project manager for Python. 

## What Does UV Actually Do?

UV solves common Python problems:

**Problem 1: Installing packages** - When you want to use external code (like `requests` for web scraping or `pandas` for data analysis), you need to download and install it. UV handles this.

**Problem 2: Avoiding conflicts** - Different projects might need different versions of the same package. UV creates isolated "virtual environments" - separate spaces for each project so they don't interfere with each other.

**Problem 3: Sharing projects** - When you want someone else to run your code, they need the exact same packages. UV creates a "lockfile" that lists everything needed, making it easy to reproduce your setup.

Summary: UV manages all the external code your Python projects depend on, keeps projects separate from each other, and makes sure everything runs smoothly.

## How to Install UV


**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

## How to Use UV

**Check UV Version**
```bash
uv --version
```

**Create a new project:**
```bash
uv init my-project #if new project
uv init # if already in folder
cd my-project
```

**Install packages:**
```bash
uv add requests
```

**Update the lockfile (without installing):**
```bash
uv lock
```
This updates `uv.lock` to reflect changes in your dependencies without installing them.

**Install all dependencies from lockfile:**
```bash
uv sync
```
This installs exactly what's specified in `uv.lock`, ensuring everyone on your team has identical packages.

**Run Python scripts:**
```bash
uv run main.py

```

**Create a virtual environment:**
```bash
uv venv
```

**Install from requirements.txt:**
```bash
uv pip install -r requirements.txt
```

UV handles virtual environments automatically when you use `uv run` or `uv add`, making Python project management much simpler.