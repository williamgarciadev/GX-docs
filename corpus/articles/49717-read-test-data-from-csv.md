---
title: "Read test data from CSV"
source_id: 49717
source_url: https://wiki.genexus.com/commwiki/wiki?49717
genexus_version: "18"
---

# Read test data from CSV

GXtest provides a procedure and SDTs to allow read test data from a CSV file. The procedure is called ReadCSV and it will be explained next.

## [ReadCSV](#ReadCSV)

Goal: allow to read test data in runtime and from outside the KB, enabling to change testing data without having to modify any object in the KB.

Parameters:

* filePath: path to the CSV file. Full and relative paths are supported
* separator: character used to split the values from each row
* useHeaders: if the CSV file has a first file of header names. Required to access values by name instead of index only
* dataPool: output SDT containing data read from the file.

Example of use:

`[imagen omitida: wiki id 49907]`

```
&DataPool = ReadCSV("inputFile.csv", ',', true)

For &Row in &DataPool.Rows

    // use &Row data to call the object under test and perform assertions

   &id = GetIntegerValueFromRow(&DataPool, &Row, "id")

   &expectedName = GetValueFromRow(&DataPool, &Row, "ExpectedName")

   &name = getName(&id)

  AssertStringEquals(&expectedName, &name, "Assert name is retrieved correctly")

endfor
```

## [Auxiliar procedures and SDTs](#Auxiliar+procedures+and+SDTs)

As you might have noted in the previous example, there are some functions and SDTs we used to convert string values to some specific types of values, like integer (numeric), and to store the data read from the CSV file. Those functions are also included inside the GXtest module and are listed below:

* GetValueFromRow
* GetIntegerValueFromRow
* GetDecimalValueFromRow
* GetDateValueFromRow
* GetDateTimeValueFromRow
* GetBooleanValueFromRow

The input parameters of these methods are the same:

* DataPool: the structure read from the CSV file
* DataPoolRow: the row to read the value from
* Column: name of the column/header to read from the DataPoolRow

The last parameter is an output parameter and its type is different for each function.

Regarding the SDTs there are two of them: DataPool and DataPoolRow

DataPool object is comprised of a collection of headers in the order they were defined in the CSV file and a list of DataPoolRows, containing the information of each line of the CSV file.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
