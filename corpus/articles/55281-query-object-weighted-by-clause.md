---
title: "Query Object: Weighted By clause"
source_id: 55281
source_url: https://wiki.genexus.com/commwiki/wiki?55281
genexus_version: "18"
---

# Query Object: Weighted By clause

The Weighted By clause in a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) allows you to obtain a weighted mean that is a measure of central tendency, applicable when in a certain set of data each data item has a relative importance (or weight) in relation to the other data. It is obtained from the quotient between the sums of all the products corresponding to each data item depending on its weight and the sum of all weights.

Within the Query object, it operates similarly to the average() function, taking into account that for a weighted average an attribute to weight by has to be defined.

### [Syntax](#Syntax)

```
Average(NumericAttribute) Weighted By NumericAttribute
```

### [Sample](#Sample)

During the school year, each student applies to tests about different subjects.

Each subject has a different weight in the final average.

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Subject
{
  SubjectId*
  SubjectName
  SubjectWeight
}
```

```
Student
{
  StudentId*
  StudentName
  Test
  {
    SubjectId*
    SubjectName
    SubjectWeight
    TestNote
  }
}
```

Suppose student Peter got a 7 (TestNote) in math and a 9 in chemistry, where the math subject has a weight of 1 and the chemistry subject has a weight of 3 in the final average.

The implementation below shows an arithmetic mean and a weighted mean.

`[imagen omitida: wiki id 55293]`

The result of the query at runtime is as follows:

`[imagen omitida: wiki id 55294]`
