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
filtered_windows = [
    window for window in windows
    if window.get_window_type() == Wnck.WindowType.__enum_values__[0]]
filtered_windows.reverse()

active_window = Wnck.Screen.get_default().get_active_window()

if not active_window:
    exit()

gdk_display = GdkX11.X11Display.get_default()
gdk_window = GdkX11.X11Window.foreign_new_for_display(
    gdk_display, active_window.get_xid())
gdk_monitor = gdk_display.get_monitor_at_window(gdk_window)

monitor_windows = {}

number_monitors = gdk_display.get_n_monitors()

for number in range(number_monitors):
    if gdk_monitor == gdk_display.get_monitor(number):
        monitor = number

for number in range(number_monitors):
    monitor_windows[number] = []

gdk_windows = gtk_screen.get_toplevel_windows()
for window in filtered_windows:
    if not isinstance(window, Gdk.Window):
        gdk_window = GdkX11.X11Window.foreign_new_for_display(
            gdk_display, window.get_xid())

    current_monitor = gtk_screen.get_monitor_at_window(gdk_window)
    monitor_windows[current_monitor].append(window)


direction = sys.argv[1]

now = GdkX11.x11_get_server_time(Gdk.get_default_root_window())

if direction == 'left':
    new_monitor = monitor - 1

    if new_monitor >= 0:
        windows = monitor_windows[new_monitor]

        if len(windows) > 0:
            Wnck.Window.get(windows[0].get_xid()).activate(now)

if direction == 'right':
    new_monitor = monitor + 1

    if new_monitor < number_monitors:
        windows = monitor_windows[new_monitor]

        if len(windows) > 0:
            Wnck.Window.get(windows[0].get_xid()).activate(now)

if direction == 'up':
    windows = sorted(monitor_windows[monitor])

    for number, window in enumerate(windows):
        if active_window.get_xid() == window.get_xid():
            window_index = number

    window_index = window_index - 1

    if window_index < 0:
        window_index = len(windows) - 1

    Wnck.Window.get(windows[window_index].get_xid()).activate(now)

if direction == 'down':
    windows = sorted(monitor_windows[monitor])

    for number, window in enumerate(windows):
        if active_window.get_xid() == window.get_xid():
            window_index = number

    window_index = window_index + 1

    if window_index >= len(windows):
        window_index = 0

    Wnck.Window.get(windows[window_index].get_xid()).activate(now)
