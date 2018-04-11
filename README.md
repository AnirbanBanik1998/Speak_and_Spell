# Speak_and_Spell

### A repository to recreate the previous games in Speak and Spell

### Prerequisites
* Python3
* Espeak

### Run
To run the entire program including collecting the wordlists if not present:
```
sudo bash run.sh
```

### In order to update the speech processing dictionary
* Update the corpus.txt file with the necessary words, and delete the previous models.
* Go to the [CMU-Sphinx](https://cmusphinx.github.io) website
* Click on **Building a language model**
* Click on the **LMtools page** link
* Upload the text file there.
* Download the contents provided to the **Voice** directory.


### Future Improvements
* Making "Encrypter" game.
* Making "Crossword" game.
* Building a suitable UI for the whole project.
* Fixing bugs related to the speech processing part.

## Documentation

### scraper.py
This scrapes out the basic English wordlists from Wikitionary to be used in this project.

### Game.py
This is a basic terminal version of the games, where input is to be typed from the keyboard.

### Game_voice.py
This provides an added functionality where words spoken out over the microphone are treated as inputs.


