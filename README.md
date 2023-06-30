## Engine resource browser
Browse the Unreal installation folder for default resources (icons, shapes, fonts) to use in your qt-tools.  
- Filter by file type
- Search by name
- Copy the path
- Pure Python, no compiling, code also works outside Unreal.

## Install

### Install using Plugget (recommended)
Plugget automatically installs this tool & it's dependencies in the correct location.
- Install the [plugget unreal](https://github.com/plugget/plugget-unreal) plugin
- Search texture browser and click install.
- restart Unreal

### Install manuallly
- pip install the Python dependencies to `...\MyProject\Content\Python\Lib\site-packages` (you can use `--target` with pip install)
  - PySide2
  - unreal-qt (optional)
- Just copy the folder in your Unreal project's plugin folder `...\MyProject\Plugins\texture-browser`
- Restart Unreal

## Dark mode
To not worry about QApp managegement, and automatically style in Unreal dark mode, you can use [unreal_qt](https://github.com/hannesdelbeke/unreal_qt) 

| dark style | default style |
| -- | -- |
| <img src="https://github.com/hannesdelbeke/texture-browser-unreal-plugin/assets/3758308/29b35d56-da78-4263-b8bb-08c24c072ae9" width="300"/> | <img src="https://user-images.githubusercontent.com/3758308/191581830-d0a527ec-cd5a-4724-9454-60f418bd93f0.png" width="400"/> |

### Similar projects
GitHub repos:
  - [SlateIconBrowser](https://github.com/sirjofri/SlateIconBrowser)  C++ icon browser, requires compiling  
  - [unreal-engine-editor-icons](https://github.com/EpicKiwi/unreal-engine-editor-icons) thumnails & names of all editor icons in your browser

Reference
- Unreal's [content browser docs](https://docs.unrealengine.com/4.26/en-US/Basics/ContentBrowser/UI/) are a good reference


## community
- Unreal forum [thread](https://forums.unrealengine.com/t/free-icon-font-browser-plugin/1215762)

If this tool is helpfull give it a ⭐ on the [GitHub](https://github.com/hannesdelbeke/texture-browser-unreal-plugin) page at the top right🙏 
