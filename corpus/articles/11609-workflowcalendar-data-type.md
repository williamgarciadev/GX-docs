---
title: "WorkflowCalendar data type"
source_id: 11609
source_url: https://wiki.genexus.com/commwiki/wiki?11609
genexus_version: "18"
---

# WorkflowCalendar data type

The WorkflowCalendar data type provides methods for working with calendars. It is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | Numeric | Read | Internal calendar’s identifier |
| Name | Character | Read | Calendar’s name |
| Description | Character | Read | Calendar’s description |

### [Methods](#Methods)

**IsHoliday**

Evaluates if a date corresponds to a holiday according to the calendar.

IsHoliday (date): Boolean

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| date | Date | Input | Date to be evaluated |

**IsWeekend**

Evaluates if a date corresponds to a weekend according to the calendar.

IsWeekend (date): Boolean

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| date | Date | Input | Date to be evaluated |

**IsWorkday**

Evaluates if a date corresponds to a working day according to the calendar.

IsWorkDay (date): Boolean

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| date | Date | Input | Date to be evaluated |

**FirstWorkdayInMonth**

Returns the date of the first working day for a specified month and year according to the calendar.

FirstWorkdayInMonth (month, year): Date

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| month | Numeric | Input | Month |
| year | Numeric | Input | Year |

**LastWorkdayInMonth**

Returns the date of the last working day for a specified month and year according to the calendar.

LastWorkdayInMonth (month, year): Date

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| month | Numeric | Input | Month |
| year | Numeric | Input | Year |

**NextWorkday**

Returns the date of the next working day from a given start date according to the calendar.

NextWorkday (startDate): Date

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| startDate | Date | Input | Initial date |

**Workday**

Returns the date resulting from adding a number of working days to a given initial date.

Workday (startDate, days): Date

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| startDate | Date | Input | Initial date |
| days | Numeric | Input | Amount of working days |

**Worktime**

It returns the date and time resulting from adding a number of working seconds to a given initial date and time.

Worktime (startTime, seconds): DateTime

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| startTime | DateTime | Input | Initial Date time |
| seconds | Numeric | Input | Amount of working seconds |

**WorkdayDuration**

Return the duration, in working seconds, of a given date according to the calendar.

WorkdayDuration (date): Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| date | Date | Input | Date of the journal day |

**WorkdaysBetweenDates**

Returns work days between two dates.

WorkdaysBetweenDates (startDate, endDate): Numeric

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| startDate | Date | Input | Initial date range |
| endDate | Date | Input | Final date range |

**Load**

Allows loading a calendar from the identifier.

Load (calendarId)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| Id | Numeric | Input | Calendar Id |

**LoadByName**

Allows loading a calendar from the name.

LoadByName (name)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Movement** | **Description** |
| name | Character | Input | Calendar name |

### [See Also](#See+Also)

[Workflow Error Codes](https://wiki.genexus.com/commwiki/wiki?11746)


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) | [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) | [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771) |

---
