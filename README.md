# yaru-colors-folder-color

## Intro

Adapting the last version of [Yaru theme](https://github.com/ubuntu/yaru) with accent color to work with the [folder-color utility](https://costales.github.io/projects/folder-color/). This program allow you to choose a color or an emblem for a selected folder [(source code here)](https://github.com/costales/folder-color).

This will allow a perfect integration of Yaru with Folder Color in Ubuntu 22.04:

![Yaru & Folder Color in Ubuntu 22.04{caption=Yaru & Folder Color in Ubuntu 22.04}](https://raw.githubusercontent.com/pakaoraki/yaru-colors-folder-color/master/screenshots/main.png "Yaru & Folder Color in Ubuntu 22.04")

## Accent colors

This new version can handle the accent color theme introduced in Ubuntu 22.04:

![Light Theme - Purple accent color](https://raw.githubusercontent.com/pakaoraki/yaru-colors-folder-color/master/screenshots/light_theme-purple_accent.png "Light Theme - Purple accent color")

![Dark Theme - Blue accent color](https://raw.githubusercontent.com/pakaoraki/yaru-colors-folder-color/master/screenshots/dark_theme-blue_accent.png "Dark Theme - Blue accent color")

## How to install it

In Ubuntu 22.04 run these commands from a Terminal:

```
sudo add-apt-repository ppa:pakaoraki/yaru-colors-folder-color
sudo apt install folder-color yaru-colors-folder-color
```

Folder-color utility is available on the official Ubuntu depot but it can be also found [here](https://launchpad.net/~costales/+archive/ubuntu/folder-color) if needed (___sudo add-apt-repository ppa:costales/folder-color___).

## How to build 

I use a modified version of the code from the official Yaru theme to generate the needed colorized icons.

### Tweak and modification
The colors are defined in this file:
```
src/common/folder-colors.css
```
It's also possible to tweak the source SVG files to change the gradient for example:
```
src/icons/src/fullcolor/default/places/folders.svg
src/icons/src/fullcolor/accented/places/folders.svg
```

### Build icons

Go to src folder and clean previous build:
```
cd src
rm -R build
```

Then build new icons:
```
meson build
ninja -C build render-icons
```
The icons will be created in src/icons/.

## Credits

- ___Yaru official theme___: [Yaru](https://github.com/ubuntu/yaru).
- ___Yaru-color___: [Yaru-Colors](https://github.com/Jannomag/Yaru-Colors) icons created by [Jan Schröder](https://github.com/Jannomag).
- ___Previous Yaru folder color___: [yaru-color-folder-color](https://github.com/costales/yaru-colors-folder-color) by Marcos Costales.
- ___Folder-color utility___: [foler-color](https://github.com/costales/folder-color) by Marcos Costales.