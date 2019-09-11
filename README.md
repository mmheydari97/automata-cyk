# CYK Algorithm

In computer science, the Cocke–Younger–Kasami algorithm (alternatively called CYK, or CKY)
is a parsing algorithm for context-free grammars, named after its inventors, John Cocke, Daniel Younger and Tadao 
Kasami.It employs bottom-up parsing and dynamic programming.

The standard version of CYK operates only on context-free grammars given in Chomsky normal form (CNF).
However any context-free grammar may be transformed to a CNF grammar expressing the same language.

The importance of the CYK algorithm stems from its high efficiency in certain situations.
Using Big O notation, the worst case running time of CYK is  O ( n^3 ⋅ | G | ), 
where n is the length of the parsed string and | G | is the size of the CNF grammar G. 
This makes it one of the most efficient parsing algorithms in terms of worst-case asymptotic complexity, 
although other algorithms exist with better average running time in many practical scenarios. 
[read more](https://en.wikipedia.org/wiki/CYK_algorithm)


## Pseudo code
First we store the variables producing each character of input as a terminal in any production rule of
grammar.
then for each substring of input with length 2, we consider produced combination of terminals in right side
of production rule and store the left side in the table.
then we iteratively fill other cells with the results of previous iterations.
finally if the last cell that holds variables which are able to produce the input, contains start symbol,
we can conclude that there exists a way to produce that input with the grammar given.

```
Begin
      for ( i = 1 to n do )
      Vi1 { A | A → a is a production where ith symbol of x is a }

      for ( j = 2 to n do )
           for ( i = 1 to n - j + 1 do )
           Begin
                 Vij = ϕ
                 For k = 1 to j - 1 do
                 Vij = Vij ∪ { A | A → BC is a production where B is in Vik and C is in V(i + k)(j - k) }
           End
End
```
[read more](https://www.gatevidyalay.com/cyk-cyk-algorithm/)


## example
You can find interactive example [here](https://www.xarg.org/tools/cyk-algorithm/).

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details
