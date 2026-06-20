---
title: "How to validate object execution time"
source_id: 53786
source_url: https://wiki.genexus.com/commwiki/wiki?53786
genexus_version: "18"
---

# How to validate object execution time

To validate the execution time of an object in GeneXus using tests you can do the following changes to an existing test.

Modify the test by adding two DateTime variables with a precision of milliseconds in case you need to check at that level. Otherwise, leave it with Seconds precision.

`[imagen omitida: wiki id 53787]`

In the Source tab of the test add the following lines (the ones with comments to the right):

```
For &TestCaseData in ProcATestData()
    
    &StartTime = now() // save the moment before the call to the object is performed
    
    /* Act...                       */
    ProcA(&TestCaseData.Param1, &TestCaseData.Param2)
    
    &EndTime = now() // save the moment after the object finished its execution
    
    
    /* Assert...                    */
    AssertTrue(&EndTime.Difference(&StartTime)*1000 < 1500, "Time") // Assert the elapsed time is less than 1500 ms (1.5 seconds)
endfor
```

The previous example is for a milliseconds precision, if it works for you checking in terms of seconds remove the \*1000 in the AssertTrue call.

Note that if you are interested in seeing the time elapsed you can add it to the assertion message like this:

```
AssertTrue(&EndTime.Difference(&StartTime)*1000 < 1500, format("Execution time was %1", &EndTime.Difference(&StartTime)))
```

Even better you could assign the difference value to a new variable so it is not calculated twice unnecessarily.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
