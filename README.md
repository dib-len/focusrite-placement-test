# Ampify engineering placement test

This repository contains my answers for the technical tests for engineering placement students at Ampify.

Since the ZIP file only contained the calculator-main.cpp and README.md, I made this repository as a git fork was your preference and this was the closest I could to accommodate this. I will also be sure to email the zip contents too.

Throughout the development of both tasks, I employed feature branching to ensure a clean, organised workflow and to maintain the integrity of the main codebase. Since the tasks were relatively small I did not feel the need to create too many as I did not want to clutter the repository.

I would also like to note that I am unsure of the coding and Git standards you are familiar with, so I have used the standards we have been taught at school.

## C++ Calculator

I was provided with a simple C++ calculator that was only able to perform addition, subtraction and multiplication.

The tasks were as follows:

+ Add division to the calculator
+ Find and fix any problems
+ Add `pi` to the calculator as a constant (so instead of typing in 3.141 you can just use `pi` instead)

For adding division, I created a feature branch called `feature-addDivision`. In this branch I implemented the division operation, added zero division handling and also added a few tests.

For fixing problems, I did not notice a significant amount of bugs or problems. There were only 2 minor issues I found and fixed:

+ "assert" was undefined; fixed by adding `#include <cassert>`
+ One of the tests kept failing as it was expecting `-2.6` but was getting `2.6`

For adding `pi` to the calculator as a constant, I made the feature branch `feature-addPi`. In this branch, I added the constant `pi` and edited the functions `findAndExtractLHS` and `findAndExtractRHS` to remove any whitespaces, allowing us to see if the value inputted in either lhs or rhs was pi or not. I then made sure to add some tests to ensure it worked as intended.

The following examples were provided, and here is what the calculator gives upon inputting the example values:

```txt
10 * 4 outputs 40
25.3 + 18.6 outputs 43.9
3-5.6 outputs -2.6
pi * 5 (to five decimal places) outputs 15.708
```

Not only are these are all the correct outputs, but I also ensured these worked in the test function as well.

## Web API Parsing

For this I used Python as it is not only the language I am strongest at but I also believe Python is very ideal for this task.

The tasks were as follows:

+ Write a simple script that downloads the content of <https://api.ampifymusic.com/packs>
+ Parse the response and sort it into a set of genres
+ Print out a list of all the genres
+ Print out a list of all the packs in the genre ‘hip-hop’

I started by adding an initial python file named `web_api_parser.py`. I then created a feature branch `feature-genreProcessing` where I added a simple script that downloads the content of <https://api.ampifymusic.com/packs> using only one library, `requests`. I initially made it so that all the genres were then added into a set and then printed out as a list since the task asked for a "a set of genres" and also to print the list of genres, however, upon reaching the final task I switched the data structure to a dictionary as this not only allowed me to use a set for the key values (the genres), but also allowed me to then store the packs as well for each genre, including 'hip-hop'. I was also sure to add an `if` statement to check if 'hip-hop' exists just in case to prevent potential errors in the case it didn't.

My solutions to the task also satisfy the following:
You cannot cache theses results; the program must pull this information from the URL each time the script is run. No arguments should be required to run your script, and it should be easily callable using the default interpretter.



## Compiling and Running the C++ Calculator

To compile the C++ calculator, you will need a C++ compiler that supports C++17 standards. The following commands can be used if you have g++ installed:

`g++ -std=c++17 calculator-main.cpp -o calculator`

To then run the compiled calculator program, do:

`./calculator`

Simply follow the prompts to input calculations. For example, type `pi * 5` to calculate the value of pi times five, or `10 / 2` to perform 10 divided by 2.


## Running the Web API Parser

Ensure you have Python installed on your computer, along with the `requests` library. If `requests` is not installed, it can be installed using pip or homebrew (for Mac):

- `pip install requests`
- `brew install python-requests`

To then run the web parser script, you need to run:

`python web_api_parser.py`


Thank you!
