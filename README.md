The repository gives examples of using vscode with different languages.

### Assumptions
This doument assumes you already have `vscode`, `python` and `node` installed and you are using OSX.

### Keyboard shortcuts
```
Format Document: option + shift + f
Optimize Imports: option + shift + o
```

### Setting up python
```
python3 -m venv python/.venv
source python/.venv/bin/activate
python -m pip install --upgrade pip
pip install -r python/requirements.txt
```

By default, the vscode Python extension looks for and uses the first Python 
interpreter it finds in the system path. To select a specific python 
environment, use the Python: Select Interpreter command from the 
Command Palette (⇧⌘P).

### Settings up node
```
cd node; npm install
```

### User and Workspace Settings

The workspace `settings.json` can be seen in the `.vscode` folder of this repo.

The user `settings.json` is as configured as:
```
{
    "editor.minimap.enabled": false,
    "explorer.confirmDelete": false,
    "terminal.integrated.defaultProfile.osx": "zsh",
    "editor.autoClosingQuotes": "never",
    "editor.autoClosingBrackets": "never",
    "editor.autoClosingDelete": "never",
    "html.autoClosingTags": false,
    "javascript.autoClosingTags": false,
    "typescript.autoClosingTags": false,
    "explorer.confirmDragAndDrop": false
}
```
