# i3 config files and instructions to install in ubuntu
___

## Assumptions
___

This repo goes in **~/.config/i3/**

It also requires **~/.config/polybar**, which belongs to another github repo.

It expects a wallpapers folder like **~/Pictures/wallpapers/** (also create a **~/Pictures/wallpaper/** folder) where images don't have any spaces in their filenames.
You could remove the spaces in those filenames doing inside the folder:
```python
import os

for file in os.listdir():
  os.rename(file, file.replace(" ", ""))
```


## Installation
___

* Install i3-gaps:

https://github.com/Airblader/i3/wiki/Compiling-&-Installing

* Install other i3 related stuff and utils

  + `sudo apt-get install i3status i3lock`
  + `sudo apt-get install suckless-tools`
  + `sudo apt-get install compton feh`
  + `sudo apt-get install scrot xclip`


* Install pywal and dependencies

  + `sudo apt-get install libmagickwand-dev`
  + `sudo apt-get install libmagickcore5-extra`
  + `sudo pip3 install pywal`

  * Install polybar and dependencies

    + `sudo apt-get install polybar`
    + Install siji to get glyph icons, see https://github.com/stark/siji



## Customization
___

### Keep pywal style for new terminal windows

Append `(cat ~/.cache/wal/sequences &)` line to **~/.bashrc** file.


### set gtk theme from wal colorscheme
* Install Oomox https://github.com/themix-project/oomox

  A wal dependency to generate gtk themes from images.

* `sudo apt-get install lxappearance`

Install a gtk theme picker. Gnome-tweak-tools can achieve the same thing, but it is less as straightforward.

* Generate a gtk theme:

  + `wal -i </path/to/wallpaper/file.jpg> -g`

  + Open lxapperance and set wal as the gkt theme.

    gtk applications must be restarted to see the effects.


### gnome-terminal inner padding

Create following file: **~/.config/gtk-3.0/gtk.css**
And append to it: 
```css
VteTerminal,
TerminalScreen,
vte-terminal {
  padding: 10px 10px 10px 10px;
  -VteTerminal-inner-border: 10px 10px 10px 10px;
}
```


### vim/neovim wal colorscheme

Vim gets its colorscheme from pywal using the following plugin: https://github.com/dylanaraps/wal.vim

### Misc

* Show wallpaper image with neofetch: `neofetch --i3wm`

* Tune your keyboard repetition speed with *xset*, to which you can pass the speed at which the repetition mode is trigered, and the speed of those repetitions. (e.g. `xset r rate 300 50`)



## Usage
___

* `Control+Shift+Up` & `Control+Shift+Down`

  Keybindings to increase/decrease the volume using *pactl*.

* `$mod+space`

  Toogle keyboard language: between spanish and british.

* `$Shift+space`

  Remaping of toogle between windowed mode and tiling mode.

* `Control+Shift+b`
  
  Keybinding to run a python script: **~/.config/i3/short_scripts/new_wall.py** that gets a new randomly chosen wallpaper from **~/Pictures/wallpapers** folder, then reloads the i3 config file so the new colorscheme is generated and applied.

* `$mod+Shift+g`

  Enters gaps resizing mode. Exists with *Esc*.

* `$mod+r`

  Enters/Exist window resizing mode.

* `Print` & `Control+Print` & `Shift+Print` & `Control+Shift+Print`

  Gnome like shortcuts to do screenshots in various ways:
  + Get screenshot of whole desktop.
  + Get screenshot of selected window.
  + Select screenshot area and paste it in Picute folder.
  + Select screenshot area and copy to clipboard.

