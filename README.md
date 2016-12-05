# Hangman

Duh!

Hangman is a word guessing game. The computer thinks of a word and the player tries to guess it by suggesting letters, within a certain number of guesses. The word to guess is represented by a row of dashes, representing each letter of the word. In most variants, proper nouns, such as names, places, and brands, are not allowed. If the player suggests a letter which occurs in the word, the other player writes it in all its correct positions. If the suggested letter does not occur in the word, the computer player draws one element of a hanged man stick figure as a tally mark. If the player guesses the word correctly within the number of chances given, he/she wins the game. On the other hand, if the player makes enough incorrect guesses to allow his opponent to complete the diagram, the game is also over

I have implemented this game in Python language using the Stack Data Structure. One Stack is used to store the word to be guessed and the other Stack is used to store the guesses. There are 2 basic conditions that have to be dealt with. One, to check if the letter that is guessed is a part of the word to be guessed and if the letter has not been previously used. The other condition is the exact opposite, ie. if the letter is not a part of the word. If the first condition is satisfied, I push the letter into one stack. If the second condition is satisfied, I just increment a variable that keeps count of the wrong guesses.  

If the wrong guesses counter reaches the limit, the game is over. But if you keep guessing the right letters, those get pushed to the stack. To check if the word that the computer has offered and the word that you hav guessed are the same, I check for the sizes of the two stacks. If both are equal, you have guessed the right word. Pretty simple isn't it?
