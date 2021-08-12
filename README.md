# python-SplitString

```py
print(_("Your String"))
```

A dictionary with the following keys is passed as output: `_`, `check`, `reversed`, `choice`, `len`. <br/>
`_` - A list is stored here, which contains almost equal parts of the passed string. <br/>
`check` - If this key is equal to the value **True**, it means that the main function returned the value **0**. <br/>
`reversed` - If this key is equal to **True**, then this means that the program has walked through the line dividers backwards. <br/>
`choice` - A list is passed to this key, with values that serve as divisors of the passed string. <br/>
`len` - This key stores a dictionary with the following keys: `lenRussian`, `lenEnglish`, `lenNumber`, `len`. <br/>
> `lenRussian` - This key stores the number of Russian letters in the transmitted string. <br/>
> `lenEnglish`- This key stores the number of English letters in the transmitted string. <br/>
> `lenNumber`- This key stores the number of digits in the transmitted string. <br/>
> `len` - This key stores the number of all characters in the transmitted string. <br/>
