# What is this?
This code generates a picture called a "phase coloring" (see [domain coloring](https://en.wikipedia.org/wiki/Domain_coloring) for the essential idea) from a "[generalized hypergeometric function](https://en.wikipedia.org/wiki/Generalized_hypergeometric_function)" whose parameters are chosen from a given amateur radio callsign. 

# How does it work?
The code contains an assignment of letters to numbers. In the file ```frontsidegenerator.py``` you see lines like 
```
    if(c=="C"):
        return 5.5
```
That is code saying "assign the number 5.5 to the letter C". The entire alphabet has an assignment in the code. Numbers in callsigns just remain numbers. For instance, my callsign KE8QZC would have this translation into numbers:
```
K -> 1.5
E -> 4.5
8 -> 8
Q -> 2
Z -> 6.5
C -> 5.5
```
and so my callsign will translate into a list of numbers ```num_csg=[1.5,4.5,8,2,6.5,5.5]```. The current version of the code is written to turn callsigns that are 6 symbols long into a "2F3" [hypergeometric function](https://en.wikipedia.org/wiki/Generalized_hypergeometric_function). The first two letters of ```num_csg``` become the "top 2 parameters" of the function, the next three become the "bottom 3 parameters", and the final number becomes the exponent on the independent variable of the 2F1 function. So, my callsign KE8QZC generates the phase coloring of the function 2F1(1.5,4.5;8,2,6.5;z^(5.5)).

# What does "commit" refer to in the QSL card I received?
A "commit" is a term used in the "git" software version control software. The commit that generated your QSL card was given so you could find the exact code that was used to generate your card. You can find the list of previous commits from this main page by clicking "# commits" under the green box that says "Code". I include this because the precise scheme I use to assign callsigns to generalized hypergeometric functions will change as I run into callsigns whose phase coloring behaves in a way I don't like.

# Can I use your code?
Sure; have fun and tell me what you do with it!!
