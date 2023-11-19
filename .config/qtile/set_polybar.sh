#!/bin/bash
SERVICE="polybar"
if pgrep -x "$SERVICE" >/dev/null
then
  killall -q polybar &
else
  polybar main -c ~/.config/polybar/config.ini &   
fi
