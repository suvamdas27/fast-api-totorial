#### 1. Create and Activate a Virtual Environment

- Step 1: Create a new directory and open it in VSCode:
```bash 
    mkdir fastAPI
```
- Step 1: Create the virtual environment 
```bash
    python -m venv .my-venv
```
- Step 2: Activate the virtual environment
```bash
    source .my-venv/Scripts/activate
```
- Step 3: Select python interpretor from the newly created virtual environment in VS Code

```Ctrl+Shift+P -> Python: Select Interpretor -> Select newly created python interpretor```
- Step 4: Check which python interpretor
```bash
    which python
```
- Step 5: Update pip
```bash
    python.exe -m pip install --upgrade pip
```
#### 2. Install Requirements
```bash
    pip install -r requirements.txt
```