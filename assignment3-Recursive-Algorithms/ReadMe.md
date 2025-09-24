Assignment #3

Criteria:

It can be done in a group of three students (recommended)
You need to present it during the lab sessions and get it approved by the Student assistants.
The algorithms should work for any possible inputs and conditions
There will be online approval for those who are not available.
////////////////////////////////////////////////

 

**Q1: Recursion vs. Iteration**

A palindrome is a word that is spelled the same forward and backward. For example, "rotor" is a palindrome, but "motor" is not. A word of 0 or 1 letter is a palindrome.

Create two functions: a recursive function and an iterative function that checks whether a word is a palindrome

Check the first and last letter, then the second and the second last letter, and so on until the two references meet in the middle.
1. # iterative
def is_palindrome(word):
2.  # recursive
def is_palindrome(word):
For example:  print(is_palindrome("hello")) with the output False





**Q2: Recursion**

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

queens.jpg

 

Hints:

You have n*n board (matrix) with n rows and n columns. 

you need two functions: 

1. to see if we can place a queen on the board[i][j], by checking the current column and the two diagonals, then place Q on the board[i][j] if no conflict

2. a recursive function that backtracks and removes the queen and tries the next column if no place is found 

 

for n = 5 

nqueen.png

 

For example: for n = 4 the output can be printed as

 nqueen1.JPG
or
[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']] 