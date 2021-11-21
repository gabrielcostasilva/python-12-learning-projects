# python-12-learning-projects
A set of 12 python projects for helping me get practice.

# 12 Python Learning Projects
The projects in this repo are based on [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg).

## Overview of Projects

The projects in this repo varies from complexity, starting very easy and becoming hard as we evolve. The main goal is just to practice python syntax.

- _madlibs_ fills a sentence with user informed words. It shows an easy way to concatenate strings. It also practices basic user input. I added a check to ensure a valid weekday.

- _user guess random number_ is a game in which you try to guess a random number. It puts together conditionals (`if/elif`) and loops (`while`), along with the `random` library. I improved the code by importing only the function we used, `randint()`.

- _computer guess random number_ is a game similar to the previous one. The difference is that, in this one, the computer should guess the number. You think on a number and give the computer a limit. It tries random numbers till the limit you gave. Every time the computer guesses, you give it a hint whether it is too low or high. Eventually, the computer will get it right.

- _rock, paper, scissors_ is a traditional game in which each player choose ... well... rock, paper or scissors! Rock wins over scissors, scissors wins over paper, and paper wins over rock. Again, this games uses the `random` library. I struggled to refactor the `is_win()` function, but I could not make it. In a Java world, I probably would use the [Strategy pattern](https://github.com/gabrielcostasilva/dp-strategy.git) ;)

- _handman_ is a another guessing game. The computer chooses a word from a (huge) list and you have to guess what word it is. As in previous games, the `random` library is used to randomly pick a word from a list. This game also introduces the `string` library, which we use to access the alphabet letters. In this game, the things start to get complex. The game is the longest so far in the number of lines of code. It also relies on several conditionals. This is the point in which the code design becomes important.