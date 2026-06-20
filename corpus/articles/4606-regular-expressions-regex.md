---
title: "Regular Expressions (RegEx)"
source_id: 4606
source_url: https://wiki.genexus.com/commwiki/wiki?4606
genexus_version: "18"
---

# Regular Expressions (RegEx)

A regular expression (regex) is a string used to describe or match a string collection, according to certain syntax rules. The use of Regular Expressions to search and manipulate strings is becoming very popular in text editors, utilities, and programming languages. Given its declarative nature, regular expressions are fully supported in GeneXus.

Java, .NET and Ruby generators support this feature not only on the server side, but on the client side as well (the generated jscripts).

GeneXus supports POSIX and POSIX ERE (Extended) regular expression syntax. More information about these standards [here](http://en.wikipedia.org/wiki/Regular_expression#POSIX).

Read about the RegExMatch data type [here](#RegExMatch)

### [Regex Methods](#Regex+Methods)

#### [IsMatch](#IsMatch)

**Scope:** Character, LongVarChar and VarChar data types.

**Purpose:** Check if the string matches the pattern.

**Syntax:**

```
B.IsMatch(C)
```

The type returned is Boolean. B and C can be a string attribute or variable. B represents the string where the pattern is tested and C is the string that contains the pattern (regular expression).

**Description:** The method tries to match the regular expression in C with the string contained in B. If it matches, "true" is returned. Otherwise "false" is returned. The syntax of the regular expression is specified in the "RegEx syntax" section.

**Example:**

```
&pattern = "\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*" // valid email address pattern
if(&str.IsMatch(&pattern))
    &result="MATCH"
else
    &result="DOESN'T MATCH"
endif

// The following table shows the value of &result given the value of &str after executing the above code.
// &str                           &result
// "john.doe12@mail.com.uk"       "MATCH"
// "john.doe@mail."               "DOESN'T MATCH"
```

NOTE: When the expression is used as "Regular Expression" attribute/domain property value, it must not include a start and end. Example: \w+([-+.']\w+)\*@\w+([-.]\w+)\*\.\w+([-.]\w+)\* instead of "\w+([-+.']\w+)\*@\w+([-.]\w+)\*\.\w+([-.]\w+)\*"

#### [ReplaceRegEx](#ReplaceRegEx)

**Scope:** Character, LongVarChar and VarChar data types.

**Purpose:** Replace all occurrences of the pattern.

**Syntax:**

```
B.ReplaceRegEx(C,D)
```

The type returned is String. B, C and D can be string attributes or variables. B represents the string where the pattern is replaced; C is the string that contains the pattern (regular expression) and D is the string that replaces the matches.

**Description:** This method replaces all occurrences of C pattern in B with D. The pattern uses the syntax described in the "RegEx syntax" section. The replacement string could be a simple string or could refer to parts of the replaced string using the $X expression. ("$X" refers to the group number X defined in the pattern, the groups could be defined in the pattern using the "()" expression, as described in the "RegEx syntax" section, and are numbered in order of appearance).

**Example:**

```
&pattern = "\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b" // date as dd/mm/yyyy
&str = "11/12/2003 extra 8/12/2003"
&rslt = &str. ReplaceRegEx(&pattern,&replacement)

// The following table shows the value of &rslt given the value of &str after executing the above code.
//     &replacement                          &rslt
//     "$2-$1-$3"                            "12-11-2003 extra 12-8-2003" //transform to mm-dd-yyyy
//     "<<DATE>>"                            "<<DATE>> extra <<DATE>>"    // date substitution
```

#### [Matches](#Matches)

**Scope:** Character, LongVarChar and VarChar data types

**Purpose:** Return a string collection that matches the pattern

**Syntax:**

```
B.Matches(C)
```

The type returned is Collection of RegExMatch. B and C can be string attributes or variables. B represents the string where the pattern is tested and C is the string that contains the pattern (regular expression).

**Description:** this method returns a collection of substrings, of the input string, which matches the pattern (C). The result is represented as a collection of RegExMatch (more information about it in the RegExMatch DataType section)

**Example:**

```
&pattern = "\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b" // date as dd/mm/yyyy
&str = "11/12/2003 extra 8/12/2003 extra 2/5 other text"
&rslt = &str.Matches(&pattern)

// After executing the above code &rslt contains (as RegExMatch): "11/12/2003" and "8/12/2003"
```

#### [**SplitRegEx**](#SplitRegEx)

**Scope**: Character, LongVarChar, VarChar data types

**Purpose**: Split the string using the pattern as splitter.

**Syntax**:

```
B.SplitRegEx(C)
```

The type returned is a Collection of strings. B and C can be string attributes or variables. B represents the string to be split and C is the string that contains the pattern (regular expression).

**Description**: This method returns a collection of substrings of the input string which doesn't match the pattern (C). The result is represented as a collection of strings.

**Example**:

```
&pattern = "\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b" // date as dd/mm/yyyy
&str = "11/12/2003 extra 8/12/2003 extra 2/5 other text"
&rslt = &str.SplitRegEx(&pattern)

// After executing the above code &rslt contains (as strings): "", " extra " and " extra 2/5 other text"
```

### [Regex Syntax](#Regex+Syntax)

#### [Characters](#Characters)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Description | Example | |
|  |  | match | Doesn't match |
| . | Any character | X | [everything matches] |
| [abcde] | A character of the set {abcde}\* | a | A or f or # |
| [^abcde] | A character which is not in the set {abcde}\* | A or g | c |
| [a-z0-9] | A character in the sets {a,b,c...z} {0,1,2...9}\* | b | B or # |
| \w | [\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}\p{Pc}\p{Lm}] - Matches any unicode character included in those categories. |  |  |
| \W | [^\p{Ll}\p{Lu}\p{Lt}\p{Lo}\p{Nd}\p{Pc}\p{Lm}] - Matches any unicode character not included in those categories. |  |  |
| \d | [0-9] (digit) | 8 | A or # |
| \D | [^0-9] (not a digit) | A or # | 8 |
| \s | Space | " " | A or 8 or # |
| \S | No space | A or 8 or # | " " |
| \xdd | dd is a hexadecimal number. Matches the character with ascii code dd. | \x41 matches A \x40 matches @ |  |
| \udddd | dddd is a hexadecimal character. Matches the character with unicode code dddd. | \u0013 matches # \u0030 matches @ |  |

\* Metacharacters Inside Character Classes:

Note that the only special characters or metacharacters inside a character class are the closing bracket (]), the backslash (\), the caret (^) and the hyphen (-). The usual metacharacters are normal characters inside a character class, and do not need to be escaped by a backslash. To search for a star or plus, use [+\*]. Your regex will work fine if you escape the regular metacharacters inside a character class, but doing so significantly reduces readability.

To include a backslash as a character without any special meaning inside a character class, you have to escape it with another backslash. [\\x] matches a backslash or an x. The closing bracket (]), the caret (^) and the hyphen (-) can be included by escaping them with a backslash, or by placing them in a position where they do not take on their special meaning. I recommend the latter method, since it improves readability. To include a caret, place it anywhere except right after the opening bracket. [x^] matches an x or a caret. The hyphen can be included right after the opening bracket, or right before the closing bracket, or right after the negating caret. Both [-x] and [x-] match an x or a hyphen.

You can put the closing bracket right after the opening bracket, or the negating caret. []x] matches a closing bracket or an x. [^]x] matches any character that is not a closing bracket or an x. However, we do not recommend this particular practice because it may reduce readability and with the ruby generator it prints a warning in its standard error output.

#### [Matching Limits](#Matching+Limits)

|  |  |
| --- | --- |
|  | Description |
| ^ | Start of line i.e.: pattern= ^ab string that matches=ab doesn't match=aab |
| $ | End of line i.e.: pattern= ab$ string that matches=ab<<enter>> doesn't match=abc |
| \b | Limit between words i.e.: pattern= ab.\bcde string that matches=ab cde doesn't match=abocde |
| \B | No match limit between words |
| \A | Start of input string |
| \G | At the end of previous match |
| \Z | At the end of the string or before the \n at the end of the string |
| \z | At the end of the string |

#### [Quantifiers](#Quantifiers)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Description | Example | | |
|  |  | RE | match | Doesn't match |
| \* | Zero or more | a\* | aaaaa or "" | b |
| ? | Zero or one | a? | a or "" | b |
| + | One or more | a+ | aaaa or a | a or b |
| {n} | Exactly n times | a{3} | aaa | aa or aaaa |
| {n, } | At least n times | a{2, } | aa or aaaaa | a or bb |
| {n,m} | At least n and not more than m | a{2,4} | aa or aaa or aaaa | a or aaaaa |
| \*? | Zero or more with the minimum use of repetitions (lazy) | a\*? | aaaa or "" | b |
| ?? | Zero or one repetition, preferably zero (lazy) | a?? | a or "" | b or aa |
| +? | One or more with the minimum use of repetitions (lazy) | a+? | aaa or a | "" b |
| {n,}? | At least n times with the minimum use of repetitions (lazy) | a{2,}? | aa or aaaa | a |
| {n,m}? | At least n and not more than m with the minimum use of repetitions (lazy) | a{2,3}? | aa or aaa | a or aaaa |

#### [Groups](#Groups)

|  |  |
| --- | --- |
| () | Capture Group. Everything that matches the regular expression defined between "(" and ")" can be accessed using the $n expression in a replace string. [see ReplaceRegEx for more information]  i.e.: pattern= a(b\*)c string=abbbc replacement=$1 result=bbb |
| (?:X) | no capture X. Defines a group that is not accessible with the $n expression |
| (?flgs) | Turn on flags for the group. i.e.: pattern=(?i)ac string that matches=ac also matches=AC [flag i=ignoreCase] |
| (?flgs:X) | Turn on or off flags for X. i.e.: pattern=(?i:ac) string that matches=ac also matches=AC [flag i=ignoreCase] |
| (?=X) | Continue to match only if X matches right side. It doesn't consume the right side, i.e. if (?=X) matches then (?=X)X also matches  i.e.: pattern=aaa(?=bbb) string=aaabbb matches. i.e.: pattern=(aaa(?=bbb)) string=aaabbb replacement=$1 result=aaa |
| (?!X) | Continue to match only if X does not match right side |

#### [Other](#Other)

|  |  |
| --- | --- |
| $n | Replaces with group Nr. n |
| X|Y | X or Y |

#### [Flags](#Flags)

|  |  |
| --- | --- |
| s | dot matches all (including newline) |
| m | multiline |
| i | ignore case |

### [RegExMatch Data Type](#RegExMatch+Data+Type)

**Type**: Data type used to handle matches in regular expression methods.

**Properties:**

Value: String found by the pattern Groups: Collection of strings that matches each of the groups defined in the pattern.

**Example:**

```
&Input             ="11/12/2003 extra 8/12/2003 extra 2/5 other text" 
&RegularExpression ="\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b"   // regular expression for Date of type xx/xx/xxxx
 
&matchCollection = &Input.Matches(&RegularExpression) //&matchCollection is RegExpMatch collection
&rslt =""
for &match in &matchCollection     
   &rslt += "[" + &match.Value + " " 
   for &item in &match.Groups 
       &rslt += "(" + &item + ")"  
   endFor
   &rslt += t + "]"
endfor
 
// &rslt is  "[11/12/2003 (11)(12)(2003)] [8/12/2003 (8)(12)(2003)]"
```

**In the example...**

The value of &rslt will be "[11/12/2003 (11)(12)(2003)] [8/12/2003 (8)(12)(2003)]" where 11/12/2003 and 8/12/2003 represent the strings found by the pattern; the values between "(" and ")" are the values found by the groups defined in the pattern for each string found.

### [Error Checking](#Error+Checking)

Errors occurred when using Regular Expressions methods can be checked using the following static methods:

#### [GetLastErrCode()](#GetLastErrCode%28%29)

**Scope**: RegEx

**Purpose**: Check the error code after the last Regular Expressions method call

**Syntax**:

```
RegEx.GetLastErrCode()
```

**Description**: The method returns a numeric value. 0 indicates no error and 1 indicates that an error has occurred.

#### [GetLastErrDescription()](#GetLastErrDescription%28%29)

**Scope**: RegEx

**Purpose**: Get last error description after the last Regular Expressions method call

**Syntax**:

```
RegEx.GetLastErrDescription()
```

**Description**: The method returns a string indicating last error description. The description depends on the generator being use.

#### [Example:](#Example%3A)

```
&pattern = "[z-a]" //this is an invalid regular expression
&str = "abc"
&rslt = &str.Matches(&pattern)
&errCode = RegEx.GetLastErrCode()
&errDsc = RegEx.GetLastErrDescription()
// In this case &errCode will be 1 and &errDsc will be:
// .net:
// parsing "[z-a]" - [x-y] range in reverse order
// 
// java:
// Illegal character range near index 3
// [z-a]
//    ^
```

### [Regex Examples](#Regex+Examples)

##### [Use of lazy expressions ("?")](#Use+of+lazy+expressions+%28%22%3F%22%29)

```
&string = "alaalaalaala"
&replaceSentence = "($1) "
&rslt = &string.ReplaceRegEx(&RegularExpression,&replaceSentence)
```

In the example if &RegularExpression = "((ala)+?)" then &rslt= "(ala) (ala) (ala) (ala) ", but if &RegularExpression = "((ala)+)" then &rslt= "(alaalaalaala) "  
  
But why? When a lazy expression is used with a quantifier (i.e. the "+?"), the quantifier matches the shortest occurrence of the pattern quantified that makes the regular expression match. But when a quantifier is used without "?", it will match the longest occurrence of the pattern that produces a match for the expression.  
That's why the first regular expression obtains 4 results with the minimum match "ala", but the second one obtains 1 result with all the input string "alaalaalaala"

### [Regular Expression Examples:](#Regular+Expression+Examples%3A)

Valid email address:

```
\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*
```

Valid email address (allows empty email):

```
^(\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)??\s*$
```

URL (protocol, domain, port, file, parameters):

```
\b(?i:https?|ftp)(://([\w.]+(:\d{1,4})?)(/[\w+&@#/%=_!:,.;]*))?(\?[\w+&@#/%=_|!:,.;]*)?
```

Valid IP: from 0.0.0.0 to 255.255.255.255 (no capture)

```
\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})\b
```

Path (drive, folder, filename):

```
\b(?i:[a-z]):\\([^/:*?"<>]*\\)?([^\\/:*?"<>]*)
```

Valid characters are numbers, letters and underscore:

```
^[\w]*$
```

### [Resources](#Resources)

Online tools to test regular expressions:

[Regexpal](http://regexpal.com). It's a JS regular expression tester, powerful and easy to use.

[HiFi Regex Tools](http://www.gethifi.com/tools/regex). Another JS regular expression tester, with some nice eyecandy. Great for testintg ReplaceRegEx and Matches methods.

<http://www.fileformat.info/tool/regex.htm>

<http://www.radsoftware.com.au/regexdesigner/> usefull tool to test regex, ReplaceRegEx and Matches methods.

More Information:

[Regular expressionsTutorial](http://www.regular-expressions.info/tutorial.html)

[Java RegEx implementation](http://java.sun.com/docs/books/tutorial/essential/regex/) used by GeneXus generated applications.

[C# RegEx implementation](http://msdn2.microsoft.com/en-us/library/az24scfc(VS.71).aspx) used by GeneXus generated applications.


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Find option](https://wiki.genexus.com/commwiki/wiki?9723) |
| [Regular Expression property](https://wiki.genexus.com/commwiki/wiki?10484) | [Replace option](https://wiki.genexus.com/commwiki/wiki?33337) | [Translation exceptions property](https://wiki.genexus.com/commwiki/wiki?13245) |

---
