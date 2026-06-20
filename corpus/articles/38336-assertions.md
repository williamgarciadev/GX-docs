---
title: "Assertions"
source_id: 38336
source_url: https://wiki.genexus.com/commwiki/wiki?38336
genexus_version: "18"
---

# Assertions

Assertions are the only way to define if a unit test PASSES or FAILS, by comparing the result you get against the expected one.

An assertion is a function that compares the first two parameters and displays a message (3rd parameter) if they are different.

The value obtained is verified through assertions to check if it equals the expected one.

You can use assertions for everything, like a test if database table rows are expected ones or to check if an SDT has the correct (expected) data.

**IMPORTANT:** You can add as many assertions as you want, but if at least one of them fails, the Test will be marked as FAILED and the error message will be displayed on the Test Results panel. Otherwise, the test will PASS. Currently, there are 4 types of assertions to use inside [GXtest Module](https://wiki.genexus.com/commwiki/wiki?38402,,):

```
AssertNumericEquals (in:&ExpectedValue, in:&ObtainedValue, in:&ErrorMsgValue)
```

to verify that 2 numeric values are equal.

```
AssertStringEquals (in:&ExpectedValue, in:&ObtainedValue, in:&ErrorMsgValue)
```

to verify that 2 strings are equal.

```
AssertBoolEquals(in:&ExpectedValue, in:&ObtainedValue, in:&ErrorMsgValue)
```

to verify that 2 boolean values are equal, or

```
AssertTrue(in:&Value, in:&ErrorMsgValue)
```

to directly verify if a value is true.

*AssertStringEquals* is the most generic and useful function since almost any structure can be serialized as a *string*.

### [Sample](#Sample)

For example, if you want to test a procedure that uses an SDT as output, you can check its value by comparing the SDT as a JSON string like this:

```
AssertStringEquals(&SDTcountryExpected.ToJSON(), &SDTcountryObtained.ToJSON(), “The country data is different”)
```

You might also want to check a specific field of the SDT. You can do this by using something like:

```
AssertStringEquals(&SDTexpected.fieldX, &SDTobtained.fieldX, “Field X is wrong”)
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Get Text](https://wiki.genexus.com/commwiki/wiki?41680) |
| [GXtest UI Commands - Get Text from PDF](https://wiki.genexus.com/commwiki/wiki?49951) | [Introduction to UI Test for Web Automation](https://wiki.genexus.com/commwiki/wiki?40280) | [Unit Testing](https://wiki.genexus.com/commwiki/wiki?38334) |

---
