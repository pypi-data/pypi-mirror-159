# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dndfog']

package_data = \
{'': ['*']}

install_requires = \
['pygame==2.1.2', 'pywin32==304']

entry_points = \
{'console_scripts': ['dndfog = dndfog.main:start']}

setup_kwargs = {
    'name': 'dndfog',
    'version': '0.1.0',
    'description': 'DND battle map with fog of war',
    'long_description': '# DnD Fog\n\n```shell\npip install dndfog\n```\n\nCreate battlemaps for tabletop RPGs, like [D&D](https://www.dndbeyond.com/).\n\n> Program is Windows only for now. This is due to the saving and loading widgets\n> being Windows only (using pywin32). You\'re free to modify the code to add file\n> loading and saving for other platforms.\n\n![Example Map](docs/img/example-map.png)\n\n## Features\n\n- Infinite grid\n- Add and remove a "[fog of war](https://en.wikipedia.org/wiki/Fog_of_war)" effect\n- Import maps from image files\n- Place, move and remove pieces on a grid (can be matched to image grid)\n- Save and load file to JSON files (background image saved in the JSON file!)\n\n## How to use\n\nWhen installing from [pypi](https://pypi.org/), the library should come with a script\nnamed `dndfog` that you can run. It should be available in your environment if\nthe `Python\\Scripts` folder is set in PATH. You can also download an EXE from\nthe [GitHub releases](https://github.com/MrThearMan/dndfog/releases).\n\nWhen the program opens, you need to select an image file to use as a background,\nor a JSON data file to load a map from. You can also lauch the program with extra\narguments `--file=<filepath>` or `--gridsize=<size>` to change the opening parameters.\n\n> The program does not autosave! You have to save (and override) the file yourself!\n\n### Keyboard shortcuts\n\n- Remove fog: `CTRL + Left mouse button`\n- Add fog: `CTRL + Shift + Left mouse button`\n- Add a piece: `Right mouse button`\n- Remove a piece: `Double click: Left mouse button`\n- Move a piece: `Click and drag: Left mouse button`\n- Move camera: `Click and drag: Middle mouse button`\n- Move background map: `ALT + Click and drag: Left mouse button`\n- Zoom in: `Scroll wheel: Up`\n- Zoom out: `Scroll wheel: Down`\n- Show/hide fog: `1`\n- Show/hide grid: `g`\n- Save file: `CTRL + s`\n- Open file: `CTRL + o`\n- Quit program: `Esc`\n\n## Known issues or lacking features\n\nWhen zooming, the program grid and background map might not stay aligned,\nif you have moved the background map. This is due to the background map offset\nnot being scaled correctly to the new zoom level. Usually this should be only\na few pixels, and you can fix it quickly by moving the background.\n\nGridsize can only be changed on initial lauch. Use the `--gridsize=<size>`\nextra argument on first lauch to change the grid size, and when you get it\ncorrect, save the file. There was some alignment issues with the background\nmap when I tried adding this, so I skipped it for now. Might add later.\n\nThere is no undo or redo. Might add later.\n\nThere is no way to mark/point on things on the map (apart from the mouse cursor).\nMight add later.\n\n',
    'author': 'Matti Lamppu',
    'author_email': 'lamppu.matti.akseli@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mrthearman.github.io/dndfog/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
