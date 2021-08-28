This repository gives examples of using VS Code with different languages.

### Assumptions
This doument assumes you are running on OSX and have the following installed:
- `vscode`
- `python3`
- `node`
- `npm`

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

By default, the VS Code Python extension looks for and uses the first Python 
interpreter it finds in the system path. To select a specific python 
environment, use the `Python: Select Interpreter` command from the 
Command Palette (⇧⌘P).

### Setting up node
```
cd node; npm install
```

### User and Workspace settings

Workspace settings override user settings. Workspace settings are specific to a project and can be shared across developers on a project.  You can also have more than one root folder in a VS Code workspace through a feature called [Multi-root workspaces](https://code.visualstudio.com/docs/editor/multi-root-workspaces).

- `Workspace` - Settings stored inside your workspace and only apply when the workspace is opened.
- `User` - Settings that apply globally to any instance of VS Code you open.
- `Default` - Contains all default settings which are applied globally.


The Workspace `settings.json` file can be seen in the `.vscode` folder of this repo.

The User `settings.json` is configured as (the personal preference of one developer):
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
