# 12 Python Learning Projects
The projects in this repo are based on [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg).

## Overview of Projects

The projects in this repo varies from complexity, starting very easy and becoming hard as we evolve. The main goal is just to practice programming with Python.

- _madlibs_ fills a sentence with user informed words. It shows an easy way to concatenate strings. It also practices basic user input. I added a check to ensure a valid weekday.

- _user guess random number_ is a game in which you try to guess a random number. It puts together conditionals (`if/elif`) and loops (`while`), along with the `random` library. I improved the code by importing only the function we used, `randint()`.

- _computer guess random number_ is a game similar to the previous one. The difference is that, in this one, the computer should guess the number. You think on a number and give the computer a limit. It tries random numbers till the limit you gave. Every time the computer guesses, you give it a hint whether it is too low or high. Eventually, the computer will get it right.

- _rock, paper, scissors_ is a traditional game in which each player choose ... well... rock, paper or scissors! Rock wins over scissors, scissors wins over paper, and paper wins over rock. Again, this games uses the `random` library. I struggled to refactor the `is_win()` function, but I could not make it. In a Java world, I probably would use the [Strategy pattern](https://github.com/gabrielcostasilva/dp-strategy.git) ;)

- _hangman_ is a another guessing game. The computer chooses a word from a (huge) list and you have to guess what word it is. As in previous games, the `random` library is used to randomly pick a word from a list. This game also introduces the `string` library, which we use to access the alphabet letters. In this game, the things start to get complex. The game is the longest so far in number of lines of code. It also relies on several conditionals. This is the point in which the code design becomes important.

- _tic-tac-toe_ is a multiplayer strategy game. Two players compete in a 3 x 3 board. The one that _leaves their mark_ in 3 spaces in a row, wins. It is fun playing this game with the machine - specially because I always win! :D This game introduces OO programming. There are classes, inheritance, constructors, message passing and objects interacting. However, I have serious concerns on the game design. It mixes UI and code functionality. In addition, there are many conditionals in the code. Of course, this is just a practicing exercise for beginners and decoupling the code may introduce unnecessary complexity for beginners. On the other hand, if you learn using good practices, it is more likely that you are gonna apply good practices when you become a pro.

- _binary search_ is an implementation of the binary search algorithm. The also code features a `naive_search` function that searches using a `for` loop for comparison purposes. It also uses the `time` module for checking the time each algorithm takes. 

Ok, ok, I know what you are thinking, "What a heck! Where are the 12 projects???" I learning by doing. So, I needed to practice Python and these projects helped me to put basic Python skills in practice. I turns out that after a few projects, the rest was just repetition. Therefore, there is no point in keep going.

What I did was starting my own projects and practicing new features with little snippets. You can check them out in my repo list.
