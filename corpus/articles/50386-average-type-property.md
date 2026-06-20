---
title: "Average type property"
source_id: 50386
source_url: https://wiki.genexus.com/commwiki/wiki?50386
genexus_version: "18"
---

# Average type property

Specifies the type of rolling average calculation to be computed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Central** | Computes the unweighted average of N data-points taking half of the data-point to the right and half to the left |
| **Cumulative** | Computes the unweighted average of all previous data-points |
| **Exponential** | Computes the weighted average of previous N data-points with weights decreasing exponentially |
| **Simple** | Computes the unweighted average of previous N data-points (this is the default value) |
| **Weighted** | Computes the weighted average of previous N data-points with weights decreasing linearly |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Query element](https://wiki.genexus.com/commwiki/wiki?19788)

### [Description](#Description)

In data analysis, a rolling average is a calculation to analyze data points by creating a series of averages of different subsets from the full data set. Variations include simple, cumulative, or weighted forms (described below).

Given a series of numbers and a fixed subset size, the first element of the moving average is obtained by taking the average of the initial fixed subset of the number series. The subset is then modified by "shifting forward"; that is, by excluding the first number of the series, while including the following value in the subset.

A moving average is commonly used with time series data to smooth out short-term fluctuations and to highlight longer-term trends or cycles.

#### [Simple rolling average](#Simple+rolling+average)

Computes the unweighted mean of the previous N data-points. For the first terms of the series, until the size of the sampling window reaches N, the average calculation is computed as a cumulative moving average.

#### [Central rolling average](#Central+rolling+average)

For a number of applications, it is advantageous to avoid the shifting induced by using only "past" data. Hence, a central rolling average can be computed using equally spaced data on either side of the point in the series where the mean is calculated. This requires using an odd number of points in the sample window.

#### [Cumulative rolling average](#Cumulative+rolling+average)

Computes the average of all of the terms up to current one. For the last term in the series, the cumulative average will equal the final average.

#### [Weighted rolling average](#Weighted+rolling+average)

A weighted average is an average that has multiplying factors to give data different weights at different positions in the sample window. A weighted moving average has the specific meaning of weights decreasing in arithmetical progression.

This enables you to overcome inconveniences in the simple rolling average technique, because, depending on the characteristics of the data analyzed, we may decide to give greater importance to more recent data over older data or not.

#### [Exponential rolling average](#Exponential+rolling+average)

An exponential rolling average applies weighting factors which decrease exponentially. The weighting for each older datum decreases exponentially, though never reaching zero.

This technique will be more efficient than simple or weighted rolling average in quickly adapting the forecast value to fluctuations in recent data (eg: giving newer values a higher weight).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Run the main object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).

### [See Also](#See+Also)

[Number of terms property](https://wiki.genexus.com/commwiki/wiki?50339)  
[Show values as property](https://wiki.genexus.com/commwiki/wiki?50338)


|  |
| --- |
| **Backlinks** |
| [How to analyze data trends and evolution with a query object](https://wiki.genexus.com/commwiki/wiki?50410) | [Number of terms property](https://wiki.genexus.com/commwiki/wiki?50339) | [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338) |

---
