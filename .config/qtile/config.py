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

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

colors = {
    'k': '1e1e1e',
    'r': 'ff5555',
    'g': '5ac2a8',
    'y': 'eb9967',
    'b': '566ef0',
    'm': 'd098ff',
    'c': '8cceff',
    'w': '92aab7',
    'K': '6b746b',
    'R': 'ff8c8c',
    'G': '98eb98',
    'Y': 'ccc784',
    'B': '8fa0ff',
    'M': 'f298c3',
    'C': 'a6d9ff',
    'W': 'dddddd',
}

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus up in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    # Window manipulation
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod], "plus", lazy.layout.grow()),
    Key([mod], "minus", lazy.layout.shrink()),
    Key([mod, "shift"], "0", lazy.layout.normalize()), # Mod+Equal
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "b", lazy.hide_show_bar("top"), desc="Toggle bar visibility"),

    # Floating layout
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating mode"),
    Key([mod], "e", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod], "f", lazy.window.bring_to_front(), desc="Bring to front"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Application spawning
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "f", lazy.spawn("firefox -P haris"), desc="Launch Firefox"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),
    Key([mod, "shift"], "v", lazy.spawn("alacritty -e vifm"), desc="Spawn a command using a prompt widget"),
    Key([mod],          "v", lazy.spawn("/opt/vim-anywhere/bin/run"), desc="Edit anything in vim"),
    Key([mod, "shift"], "e", lazy.spawn("emacsclient --create-frame"), desc="Launch Emacs"),
    Key([mod, "shift"], "w", lazy.spawn("fish -c wiki"), desc="Launch Wiki in Emacs"),
    Key([mod, "shift"], "o", lazy.spawn("fish -c todo"), desc="Launch TODO in Emacs"),
    Key([mod, "shift"], "t", lazy.spawn("alacritty -e trans -shell"), desc="Open translate-shell"),

    Key([mod], "period", lazy.spawn("emacsclient --create-frame /home/haris/projects/schim/TODO.org"), desc="Open schim TODO.org"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group("wrk"), Group("study"), Group("sys"), Group("org"),
        Group("media"), Group("extra"), Group("min")]

for i in range(len(groups) - 1):
    # mod + number of group = switch to group
    keys.append(Key([mod], str(i+1), lazy.group[groups[i].name].toscreen()))
    # mod + shift + number of group = move focused window to group
    keys.append(Key([mod, "shift"], str(i+1), lazy.window.togroup(groups[i].name)))

# Cycle through groups
keys.append(Key([mod], "n", lazy.screen.next_group()))
keys.append(Key([mod], "p", lazy.screen.prev_group()))

# 'Minimize' group
keys.append(Key([mod], "m", lazy.group["min"].toscreen()))
keys.append(Key([mod, "shift"], "m", lazy.window.togroup("min")))

layout_theme = {"border_width": 3,
                "margin": 4,
                "border_focus": "8c9eff",
                "border_normal": "666666"
                }

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=4,
    background="202023"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
