---
title: "GXflow Process Analysis"
source_id: 18410
source_url: https://wiki.genexus.com/commwiki/wiki?18410
genexus_version: "18"
---

# GXflow Process Analysis

The GXflow process analysis module provides a comprehensive view of operational process behavior through various visual indicators. This section describes the purpose, usefulness, and context of each of the presented charts.

#### [Process Activity](#Process+Activity)

**`[imagen omitida: wiki id 59974]`**  
Purpose:  
Visualize the number of process instances created, completed, and aborted during the selected period.  
Usefulness:  
Provides a quick snapshot of the overall process execution status, making it easier to identify bottlenecks or frequent failures (e.g., a high number of aborted processes).  
Interpretation:  
In the example, 13 processes were opened, 1 was closed, and 11 were aborted, which may suggest a recurring issue in process execution.

#### [Process Activity Trend](#Process+Activity+Trend)

`[imagen omitida: wiki id 59975]`  
Purpose:  
Show the daily evolution of process instances in their different states (opened, closed, aborted, active) over time.  
Usefulness:  
Helps detect temporal patterns and analyze operational behavior, identifying peak workload days or anomalous events.  
Interpretation:  
A growing trend of aborted processes is observed over time, which may require a detailed investigation into the causes.

#### [Process Status](#Process+Status)

`[imagen omitida: wiki id 59976]`  
Purpose:  
Indicate the percentage of closed processes that were completed on time according to the estimated schedule.  
Usefulness:  
Measures efficiency in meeting deadlines and helps assess process timeliness.  
Interpretation:  
100% of closed processes were completed on time, reflecting good time performance in finalized processes.

#### [Process Duration](#Process+Duration)

`[imagen omitida: wiki id 59977]`  
Purpose:  
Compare the actual duration (minimum, maximum, average) of completed instances against the estimated duration.  
Usefulness:  
Helps evaluate the accuracy of estimates and the consistency of execution time, supporting decisions on planning improvements and resource allocation.  
Interpretation:  
In the “Ticket Reservation” process, the estimated duration is 0 (undefined), while the actual average duration is 0.82 units. This indicates a need to define clear duration expectations.

#### [Process Ranking](#Process+Ranking)

`[imagen omitida: wiki id 59978]`  
Purpose:  
Compare the number of instances created per process during the analyzed period.  
Usefulness:  
Provides an overview of the operational workload by process type, helping to prioritize resources or identify the most critical processes in terms of volume.  
Interpretation:  
The “Ticket Reservation” process dominates with 14 instances compared to only 2 for the “Purchases” process, suggesting greater operational focus on the former.


|  |
| --- |
| **Backlinks** |
| [Estimated process duration property](https://wiki.genexus.com/commwiki/wiki?20897) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [GXflow Statistics](https://wiki.genexus.com/commwiki/wiki?17850) | [HowTo: Use GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?10721) | [Statistics and business process optimization](https://wiki.genexus.com/commwiki/wiki?25239) |

---
