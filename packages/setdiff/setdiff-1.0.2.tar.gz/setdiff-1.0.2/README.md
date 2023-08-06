# setdiff
Given two files, show the size of set difference, union, intersection, and more of their lines.

## Example:

File a:
```
123
a
a
ab
cd
```

File b:
```
a
a
ab
456
```
### Usage:

`sett a b` or alias `setdiff a b`

Output:
```
     {A}  4
       A  5
     {B}  3
       B  4
 |A|-|B|  1
   A ∖ B  2
   B ∖ A  1
   A ∪ B  5
   A ∩ B  2
```



