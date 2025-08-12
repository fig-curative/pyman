# pyman

pyman is an implementation of hangman in python which pulls a random secret word from a provided wordlist text file and then allows you to guess the letters contained within it

pyman ver 1 has limitations:
1. it accounts for words with duplicate letters by revealing all of the like letters - players don't have to guess C twice for CIRCLE, for example
2. the player only gets three guesses before being hanged
3. wordlist.txt contains a limited number of words

pyman ver 1 has features:
1. add any word you want for a chance to play it in hangman
2. naive hangman illustrations included
3. you can both win and lose
4. pyman makes sure you actually guessed a letter and doesn't care if its uppercase or lowercase

ideas for improvement and expansion:
1. add GUI
2. expand wordlist
3. player-selected difficulty levels
4. "no spoilers" system argument to hide word reveal upon a loss