#!/usr/bin/env python

import gtk
import sys
import wnck

# Get screen - this must come before gtk loop
screen = wnck.screen_get_default()
gtk_screen = gtk.gdk.screen_get_default()

# Deal with pending events
while gtk.events_pending():
    gtk.main_iteration()

# Get windows list and filter for normal windows
windows = screen.get_windows_stacked()
filtered_windows = [
    window for window in windows
    if window.get_window_type() == wnck.WindowType.__enum_values__[0]]
filtered_windows.reverse()

active_window = wnck.screen_get_default().get_active_window()
gdk_window = gtk.gdk.window_foreign_new(active_window.get_xid())
monitor = gtk_screen.get_monitor_at_window(gdk_window)

monitor_windows = {}

number_monitors = gtk.gdk.screen_get_default().get_n_monitors()

for number in range(number_monitors):
    monitor_windows[number] = []

gdk_windows = gtk_screen.get_toplevel_windows()
for window in filtered_windows:
    if not isinstance(window, gtk.gdk.Window):
        gdk_window = gtk.gdk.window_foreign_new(window.get_xid())

    current_monitor = gtk_screen.get_monitor_at_window(gdk_window)
    monitor_windows[current_monitor].append(window)


direction = sys.argv[1]

now = gtk.gdk.x11_get_server_time(gtk.gdk.get_default_root_window())

if direction == 'left':
    new_monitor = monitor - 1

    if new_monitor >= 0:
        windows = monitor_windows[new_monitor]

        if len(windows) > 0:
            wnck.window_get(windows[0].get_xid()).activate(now)

if direction == 'right':
    new_monitor = monitor + 1

    if new_monitor < number_monitors:
        windows = monitor_windows[new_monitor]

        if len(windows) > 0:
            wnck.window_get(windows[0].get_xid()).activate(now)

if direction == 'up':
    windows = sorted(monitor_windows[monitor])

    for number, window in enumerate(windows):
        if active_window.get_xid() == window.get_xid():
            window_index = number

    window_index = window_index - 1

    if window_index < 0:
        window_index = len(windows) - 1

    wnck.window_get(windows[window_index].get_xid()).activate(now)

if direction == 'down':
    windows = sorted(monitor_windows[monitor])

    for number, window in enumerate(windows):
        if active_window.get_xid() == window.get_xid():
            window_index = number

    window_index = window_index + 1

    if window_index >= len(windows):
        window_index = 0

    wnck.window_get(windows[window_index].get_xid()).activate(now)
