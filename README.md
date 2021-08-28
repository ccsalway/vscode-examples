The repository gives exampls of using vscode with different languages.


Format Document: option + shift + f
Optimize Imports: option + shift + o

---------
python3 -m venv python/.venv
source python/.venv/bin/activate
python -m pip install --upgrade pip
pip install -r python/requirements.txt

By default, the Python extension looks for and uses the first Python 
interpreter it finds in the system path. To select a specific python 
environment, use the Python: Select Interpreter command from the 
Command Palette (⇧⌘P).

---------
cd node; npm install


---------
The user `settings.json` is as follows
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