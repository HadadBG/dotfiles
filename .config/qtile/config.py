# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click ,Match
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
import os
from typing import List  # noqa: F401
import locale

#locale.setlocale(locale.LC_TIME,"es_ES")
show_more_info = False
mod = "mod4"
terminal="alacritty"
keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "h", lazy.layout.left()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86Display", lazy.spawn("./.config/qtile/set_polybar.sh")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "c", lazy.spawn("gpick -s")),


]

groups = [        
        Group('🎵'),
        Group('🍃'),
		Group('🌎'),
		Group('☕'),
		Group('🙀'),
		  ]
#1-musica
#2-servidores
#3-web
#4-trabajo
#5-visualizacion


j=0
for i in groups:
    j+=1
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(j), lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],str(j), lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"],str(j), lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Max(),
    #layout.Stack(num_stacks=2, margin = 15, borderwidth = 5,
    #    autosplit = True),
    # Try more layouts by unleashing below layouts.
   #  layout.Bsp(),
    # layout.Columns(),
     #layout.Matrix(),
     layout.MonadTall(
            border_focus = 'ffffff',
            margin = 15
         ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
##     layout.TreeTab(),
  #  layout.VerticalTile(),
   #  layout.Zoomy(),
]

widget_defaults = dict(
    font='SF Pro Text 16',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#screens = [ Screen()]
screens = [
	Screen(
		bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale = 0.8),
                widget.GroupBox(fontsize=15, highlight_method = 'line', highlight_color = ['2E3440', 'ffffff'], borderwidth = 0),
                 widget.Spacer(length=400),
                 widget.Mpris2(
                    name='spotify',
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text='',
                    fmt='▶   {}',
                    **widget_defaults
                ),
            	widget.Spacer(),
                widget.Clock(format='%d-%m-%Y   %I:%M %p'),
               
            ],
            30,
        background="#2E3440",
        opacity=0.93,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
#floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
 #   {'wmclass': 'confirm'},
  #  {'wmclass': 'dialog'},
   # {'wmclass': 'download'},
    #{'wmclass': 'error'},
   # {'wmclass': 'file_progress'},
   # {'wmclass': 'notification'},
   # {'wmclass': 'splash'},
   # {'wmclass': 'toolbar'},
   # {'wmclass': 'confirmreset'},  # gitk
   # {'wmclass': 'makebranch'},  # gitk
   # {'wmclass': 'maketag'},  # gitk
   # {'wname': 'branchdialog'},  # gitk
   # {'wname': 'pinentry'},  # GPG key password entry
   # {'wmclass': 'ssh-askpass'},  # ssh-askpass
#])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser('~')
	subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
