---
title: "NoOutput clause"
source_id: 25408
source_url: https://wiki.genexus.com/commwiki/wiki?25408
genexus_version: "18"
---

# NoOutput clause

The NoOutput clause in a [Data Provider Group](https://wiki.genexus.com/commwiki/wiki?25082) means that the Group itself will not be present in the Output, only its subordinate elements.

### [Syntax](#Syntax)

```
'['NoOutput']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

### [Samples](#Samples)

Suppose that you want to Output the list of Employees, but showing salary information only to authorized users:

```
Employees parm(&UserId)
{
   Employee
   {
      Id   = EmployeeId
      Name = EmployeeName
      EarningInfo
         Where IsAutorized(&UserId)
      {
         Salary = EmployeeSalary
         Bonus  = EmployeeBonus
      }
   }
}
```

The Output (in XML) will be:

```
<Employees>
   <Employee>
      <Id>123</Id>
      <Name>John Doe</Name>
      <EarningInfo>
         <Salary>30000</Salary>
         <Bonus>5000</Bonus>
      </EarningInfo>
   </Employee>
   ...
</Employees>
```

But if the Output needs to be 'flat' like this:

```
<Employees>
   <Employee>
      <Id>123</Id>
      <Name>John Doe</Name>
      <Salary>30000</Salary>
      <Bonus>5000</Bonus>
   </Employee>
   ...
</Employees>
```

...the NoOutput is sufficient:

```
Employees parm(&UserId)
{
   Employee
   {
      Id   = EmployeeId
      Name = EmployeeName
      EarningInfo [NoOutput]
         Where IsAutorized(&UserId)
      {
         Salary = EmployeeSalary
         Bonus  = EmployeeBonus
      }
   }
}
```


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
