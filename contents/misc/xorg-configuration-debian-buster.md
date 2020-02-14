title: Debian Buster Touchpad configuration
date: 2020-02-13
comments: true
code: true

The default display server in Buster is now Wayland. Unfortunately, it is currently not possible to configure Wayland as extensively as Xorg. Example: Impossible to make two-finger tap cause a middle click. Both Xorg and Wayland use libinput for handling input devices and only via the Xorg configuration one can tap into the configuration of libinput. For the Xorg configuration, one has to keep in mind that the configuration is applied in both the xorg config files and also via some Gnome tools, which sometimes leads to config entries from the config overriden by the Gnome tools. Places where to set configuration values:

- Gnome Touchpad settings
- Gnome Tweaks -> Touchpad
- xorg configuration files

For the latter, it is best to create a directory xorg.conf.d in /etc/X11 and copy the file /usr/share/X11/xorg.conf.d/40-libinput.conf into that folder. For my setup, almost everything can be configured via the Gnome tools except for disabling the middle click button:

```
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        MatchDriver "libinput"
        Option "MiddleEmulation" "on"
EndSection
```

Also, the Xorg log file is now located somewhere in the home folder.
