#
# ~/.bashrc
#

# If not running interactively, don't do anything
neofetch
~/Scripts/pacman_pinguco
[[ $- != *i* ]] && return
alias rm='rm -I'
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias v='nvim'
export PS1="\[$(tput bold)\]\[\033[38;5;117m\]\W\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;83m\]>\[$(tput sgr0)\] \[$(tput sgr0)\]"
alias post="curl   -X POST  -H 'Content-Type: application/json'" 
export PATH=$PATH:~/Scripts
