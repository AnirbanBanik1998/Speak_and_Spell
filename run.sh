#!/bin/bash

echo "Welcome"
if [ -e Wordlist.csv ]
then
	echo "Wordlists already present...we can start playing"
else
	cd Wiki_scraper
	echo "Collecting Wordlists..."
	python3 scraper.py &
	cd ..
fi
echo "How do you want to play: 1->With, 2->Without keyboard?"
read input
b=2
if [[ "$input" -eq "$b" ]]
then
	cd Voice
	chmod +x voice.sh
	./voice.sh
	cd ..
else 
	python3 Game.py
fi

