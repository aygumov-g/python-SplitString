# python-SplitString

```py
print(_("Your String"))
```

A dictionary with the following keys is passed as output: `_`, `check`, `divisor`, `len`, `reversed`. <br/>
----`_` - A list is stored here, which contains almost equal parts of the passed string. <br/>
----`check` - If this key is equal to the value **True**, it means that the main function returned the value **0**. <br/>
----`divisor` - This key stores a dictionary that contains two keys `all`, `selected`. <br/>
--------`all` - This key stores the main divisors of the main list, into one of which the transmitted string will be divided. <br/>
--------`selected` - This key stores one divisor from their list, into which the transmitted string was divided. <br/>
----`len` - This key stores a dictionary with the following keys: `lenRussian`, `lenEnglish`, `lenNumber`, `len`. <br/>
--------`lenRussian` - This key stores the number of Russian letters in the transmitted string. <br/>
--------`lenEnglish`- This key stores the number of English letters in the transmitted string. <br/>
--------`lenNumber`- This key stores the number of digits in the transmitted string. <br/>
--------`lenWhitespace`- This key stores the value of spaces in the passed string. <br/>
--------`lenPunctuation` - This key stores a dictionary with punctuation marks. <br/>
------------ - The punctuation mark is a key with the corresponding value. <br/>
--------`lenOther` - Other characters are stored in this key. <br/>
--------`len` - This key stores the number of all characters in the transmitted string. <br/>
----`reversed` - If this key is equal to **True**, then this means that the program has walked through the line dividers backwards. <br/>
