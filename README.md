# pyman

pyman is an implementation of hangman in python which pulls a random secret word from a provided wordlist text file and then allows you to guess the letters contained within it

pyman ver 1 has notable limitations:
1. it doesn't work with words with duplicate letters ex. baLLet, CirCle
2. the player only gets three guesses before being hanged
3. wordlist.txt contains only a single word