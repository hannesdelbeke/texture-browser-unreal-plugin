search for icons in unreal (pure Python, no compiling)  

## Engine resource browser
Browse the unreal instal folder for default resources (icons, shapes, fonts) which can be used in your qt-tools  
- filter by file type
- search by name


## Install
- pip install the python dependencies to `...\MyProject\Content\Python\Lib\site-packages` (you can use `--target` with pip install)
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
- unreal's [content browser docs](https://docs.unrealengine.com/4.26/en-US/Basics/ContentBrowser/UI/) are a good reference


## community
- unreal forum [thread](https://forums.unrealengine.com/t/free-icon-font-browser-plugin/1215762)

If this tool is helpfull give it a ⭐ on the [GitHub](https://github.com/hannesdelbeke/texture-browser-unreal-plugin) page at the top right🙏 
