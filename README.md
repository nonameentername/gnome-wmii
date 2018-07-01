gnome-wmii
==========

Simple script to allow focusing and moving gnome windows in a similar way to wmii.

Install
-------

Install system dependencies:

    sudo apt-get install python-gi

Clone the github project and run the setup script:

    git clone https://github.com/nonameentername/gnome-wmii.git
    cd gnome-wmii
    ./setup.sh

Key bindings:

| Description                  | Command               |
| ---------------------------- | --------------------- |
| move window to left monitor  | '\<Shift\>\<Super\>h' |
| move window to right monitor | '\<Shift\>\<Super\>l' |
| maximize window              | '\<Shift\>\<Super\>k' |
| unmaximize window            | '\<Shift\>\<Super\>j' |
| move focus left              | '\<Super\>h'          |
| move focus right             | '\<Super\>l'          |
| move focus up                | '\<Super\>k'          |
| move focus down              | '\<Super\>j'          |
| open terminal                | '\<Super\>return'     |
| close terminal               | '\<Shift\>\<Super\>c' |
| open rofi menu               | '\<Super\>space'      |
