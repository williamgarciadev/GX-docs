---
title: "Error_Handler rule"
source_id: 6853
source_url: https://wiki.genexus.com/commwiki/wiki?6853
genexus_version: "18"
---

# Error_Handler rule

# Error\_Handler rule

Provides a dynamic way to perform user-specific actions when a database-related error occurs during program runtime.

### [Syntax](#Syntax)

**Error\_Handler(‘***subname*'**);**  
  
**Where:**  
  
*subname*  
   Is the name of a subroutine contained in the program which makes use of this rule.

### Scope

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### Description

By using this rule, any transactional and connection errors are detected and a user-defined routine is executed.  
  
It's a declarative rule which applies to the whole program, anywhere that an active error\_handler command does not exist.  
  
The scope of the rule or command will only be taken into consideration by the program that makes use of it. This means that it will not affect any programs called by the program that uses it, and if a program that uses this rule/command happens to call another program that also makes use of it, the second program will ignore the specification of the rule/command belonging to the calling program (the original program) and will not affect the calling program at all. Again, it should be pointed out that the use of this rule/command is limited to the program that uses it.  
  
The error\_handler program is called whenever a database related error is detected at run time. It receives no parameters and it allows usage of the &err [standard variable](https://wiki.genexus.com/commwiki/wiki?7386) to identify GeneXus Error as specified below:  

|  |  |  |
| --- | --- | --- |
| **Name** | **Data Type** | **Description** |
| &Err | Numeric(3) | It contains the GeneXus standard error codes or 999 if an undefined database error code is detected. It is strongly recommended to use this variable whenever possible to identify errors. This technique will make your programs portable from one GeneXus platform to another. The following list shows &Err values and their meaning (which can be assigned to the &Errmsg variable):  1                       Duplicate record  101                   End of file  103                   Object locked (record or file)  105                   Object not found  106                   Database already exists  500                   Parent primary key not found  600                   Referential Integrity error raised (only Java Generator)  999                   Unexpected DBMS error. |

Also, it is possible to receive more detailed information about database native error codes and descriptions, defining these variables:

|  |  |  |
| --- | --- | --- |
| **Name** | **Data Type** | **Description** |
| &gxDBErr | Numeric(5) | It contains the native DBMS error code. Its value is set only when &Err is greater than 500, otherwise, its value is undefined. |
| &GxDbSqlState | Character(5) | It contains the native [SQLSate](https://en.wikipedia.org/wiki/SQLSTATE) error code. |
| &gxDBTxt | Character(255) | It contains the native DBMS error message. Its value is set only when &Err is greater than 500, otherwise, its value is undefined. |
| &gxOper | Character(30) | It contains a descriptive identification of the operation that had been taking place when the error was encountered. Possible values for this variable are: Declare, Fetch, Insert, Update, Delete |
| &gxErrTbl | Character(30) | It contains the name of the table (if any) that was being accessed when the error occurred. This variable may contain the special value 'N/A' if no table is related to the database operation (i.e. database creation, remote procedure calls, etc.). |
| &gxErrOpt | Numeric(1) | Used as a return code by the error\_handler. Depending on the value set by the error\_handler, the program will:  0 = Continue processing: The error is ignored.  1 = Retry the operation: retries the specified amount using the Lock retry count property. If the error continues after the retries it continues with the processing.  2 = Cancel application execution:  it will cancel the application at any SQL error.  3 = Perform default GeneXus processing: It's the Default value. It will behave in the same way as a program without an error handler, that is: some errors will be ignored as locked, duplicate, etc., and the rest will cancel the application's execution.  **Considerations:**   * If the &gxErrOpt is set to 0 or 1, the error will not be shown in the standard output because it's being captured by the GeneXus generated code. * If a [Return command](https://wiki.genexus.com/commwiki/wiki?31353) is executed within the subroutine called by the Error\_Handler rule, the running object will end and it will return to the caller. In this case, the code that processes the error according to the &gxErrOpt value will not be executed. So, regardless of the value assigned to &gxErrOpt, the application will not cancel. In other words, if you assign &gxErrOpt=2 or &gxErrOpt=3 but a Return command is executed within the subroutine called by the Error\_Handler rule, the application will not cancel. |

#### **Notes:**

* These Variables can be used on each object that has an Error\_handler rule or command.
* Any DBMS exception is caught by the error\_handler rule or command. Then, the standard variables are loaded in the following cases:
  + &gxDBErr and &gxDBTxt are loaded in any case
  + &gxDBSqlState is loaded in:
    - Java
      * All DBMSes
    - .Net Framework:
      * PostgreSQL
      * Informix
    - .Net:
      * MySQL
      * PostgreSQL

### [Samples](#Samples)

Consider a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with the following defined:

Rules:

```
error_handler('DBErrors');
```

  
Events:

```
Sub 'DBErrors'
    If &Err = 1
        Msg('Duplicate record')
    Endif 
EndSub
```

### [See Also](#See+Also)

[Error\_Handler Command](https://wiki.genexus.com/commwiki/wiki?8238)


|  |
| --- |
| **Backlinks** |
| [Declare referential integrity property](https://wiki.genexus.com/commwiki/wiki?9093) | [Err variable](https://wiki.genexus.com/commwiki/wiki?51028) | [ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) |
| [Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238) | [Exception\_Handler rule](https://wiki.genexus.com/commwiki/wiki?44808) | [Paging clauses in Data Provider Group Statement](https://wiki.genexus.com/commwiki/wiki?25410) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |
| [Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288) |

---
