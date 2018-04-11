#!/bin/bash

echo "Welcome"
cd Wiki_scraper
if [ -e Wordlist.txt ]
then
	echo "Wordlists already present...we can start playing"
else
	echo "Collecting Wordlists..."
	python3 scraper.py &
fi
cd ..

