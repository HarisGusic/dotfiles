export MAKEFLAGS='-j4'
export GPG_TTY=$(tty)
export QT_QPA_PLATFORMTHEME=gtk2

export PATH=\
~/.local/bin:\
$(echo ~/.local/share/gem/ruby/*/bin):\
$PATH:\
$(echo ~/scripts/*/):\
~/.pyenv/versions/3.8.3/bin:\
/opt/anaconda/bin

[ -f ~/.alias ]         && . ~/.alias
[ -f ~/.alias-tmp ]     && . ~/.alias-tmp
[ -f ~/.alias-gui ]     && . ~/.alias-gui
[ -f ~/.alias-gui-tmp ] && . ~/.alias-gui-tmp

