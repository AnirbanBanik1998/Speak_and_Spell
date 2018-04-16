#!/bin/bash

gnome-terminal -e "pocketsphinx_continuous -inmic yes -lm 9731.lm -dict 9731.dic > decode.txt" 
python3 Game_voice.py
