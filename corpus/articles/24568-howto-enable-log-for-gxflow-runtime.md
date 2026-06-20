---
title: "HowTo: Enable Log for GXflow runtime"
source_id: 24568
source_url: https://wiki.genexus.com/commwiki/wiki?24568
genexus_version: "18"
---

# HowTo: Enable Log for GXflow runtime

This document explains how to enable the logging for Workflow Tables impact, reorganizations, and access to GXflow database information when using the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272).

Sometimes, when you need to reorganize Workflow Tablesor make an impact analysis or when a Workflow process isn't working correctly, an error showing no specific details occurs. This may happen when a new Upgrade of GeneXus is installed. In this case, it is useful to enable the logging and look for errors in the *.log* file created, as shown below:

### [Enabling logging in the GeneXus IDE (for GXflow impact)](#Enabling+logging+in+the+GeneXus+IDE+%28for+GXflow+impact%29)

It only implies enabling the Generator's logging. The logging properties can be found under Preferences, by clicking on the corresponding Generator node.

To generate the log with the required information, the Log Level and User Log Level properties must be set as follows:

`[imagen omitida: wiki id 54000]`

The properties to be set for all the Generators are as follows:

* [**Log level**](https://wiki.genexus.com/commwiki/wiki?36304) property defines how much detail has to be added to the log at runtime.
* [**User log level**](https://wiki.genexus.com/commwiki/wiki?42434) property details the writing level of the Log when using the Log API programmatically.
* [**Log output**](https://wiki.genexus.com/commwiki/wiki?39568)property indicates the output for the Log level property.
* [**Log file**](https://wiki.genexus.com/commwiki/wiki?39601)property defines the name of the Log Output file when the Log Output Property is set to File.

[Java](https://wiki.genexus.com/commwiki/wiki?12258) has some unique properties:

* [**Log JDBC Activity**](https://wiki.genexus.com/commwiki/wiki?9135) allows knowing what happens in the JDBC connections to the databases. If you set this property to Yes, the following properties will appear.
* [**Use unique names**](https://wiki.genexus.com/commwiki/wiki?13945) property defines whether you want to automatically generate a log file or use a fixed name.
* [**JDBC Log File**](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13946,,) property completes the path to a log file.
* [**Detail**](https://wiki.genexus.com/commwiki/wiki?13948) property indicates the JDBC log’s detail level.
* [**Enable buffering**](https://wiki.genexus.com/commwiki/wiki?13947) property allows indicating whether the buffer is activated when generating the activity log.

To apply changes made by these properties, Build any object.

After setting the properties, execute the reorganization or impact analysis, and the log will be created. The actions that you do in GXflow Client will be registered in this log.

### [Enabling logging in Production](#Enabling+logging+in+Production)

By default, the log.config (NET) or log4j2.xml (java) file is configured with minimal logging to reduce overhead in production environments. To enable detailed logging for GXflow, you must update this archive described below.

```
    <root>
        <level value="ALL"/>
        <appender-ref ref="RollingFile"/>
    </root>
    
    <!-- GeneXus User Log Logger 'GX_LOG_LEVEL_USER' !-->
    <logger name="GeneXusUserLog" additivity="false">
        <level value="ALL" />
        <appender-ref ref="RollingFile"/>
    </logger>
    <!-- GeneXus Standard Classes Logging !-->
        <logger name="GeneXus" additivity="false">
            <level value="DEBUG" />
            <appender-ref ref="RollingFile"/>
        </logger>
```

Increasing log verbosity may generate large log files; use these settings temporarily during troubleshooting or controlled production monitoring.

If the path is not defined, the log will be created by default in the following files according to your generator:

* [**.NET Framework:**](https://wiki.genexus.com/commwiki/wiki?2892) *<kb\_path>\CSharpModel\web*
* [**.NET:**](https://wiki.genexus.com/commwiki/wiki?38604)  *<kb\_path>\NetModel\web\bin*
* [**Java:**](https://wiki.genexus.com/commwiki/wiki?12258)*<webapp\_path>\logs\*

If the log is working correctly, it should have a line similar to this one when you are signing in GXflow:

```
2022-06-15 10:41:49,002 [34] DEBUG GeneXus.Data.ADO.GxCommand - ExecuteReader: Parameters @AV40WFUsrCod='WFADMINISTRATOR'
```

**Note**: If you are generating with [.NET](https://wiki.genexus.com/commwiki/wiki?38604) or [Java](https://wiki.genexus.com/commwiki/wiki?12258), another *client.log* will be created in *<kb\_path>\Model\web\bin* and *<kb\_path>\Model\web\logs*, respectively. It will only have information about the creation or reorganization of the database when you do a Build/Rebuild.

### [See Also](#See+Also)

[HowTo: Enable Log for GXflow BPDeployer](https://wiki.genexus.com/commwiki/wiki?51046)  
[HowTo: Generate log for GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Enable Log for GXflow BPDeployer](https://wiki.genexus.com/commwiki/wiki?51046) |

---
