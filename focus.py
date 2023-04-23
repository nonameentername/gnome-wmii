#!/usr/bin/env python

import gi
import sys
gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gdk
from gi.repository import GdkX11
from gi.repository import Gtk
from gi.repository import Wnck


# Get screen - this must come before gtk loop
screen = Wnck.Screen.get_default()
gtk_screen = Gdk.Screen.get_default()

# Deal with pending events
while Gtk.events_pending():
    Gtk.main_iteration()

# Get windows list and filter for normal windows
windows = screen.get_windows_stacked()

now = GdkX11.x11_get_server_time(Gdk.get_default_root_window())
name = sys.argv[1]

for window in windows:
    if name in window.get_name():
        Wnck.Window.get(window.get_xid()).activate(now)
