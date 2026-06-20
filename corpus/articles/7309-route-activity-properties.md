---
title: "Route Activity Properties"
source_id: 7309
source_url: https://wiki.genexus.com/commwiki/wiki?7309
genexus_version: "18"
---

# Route Activity Properties

They help in defining the Route Activity's behavior.

Name: route activity name.

Visible in history: It indicates whether the task must be shown in the history.  
  
Roles: Associated roles to execute the task.  
  
Subject Rule: It allows defining the subject of the task at runtime. It admits  characters, attributes and relevant data (eg."Customer registration number"+CustomerId+&relevantData).

Advanced Properties

Calendar: It allows determining the calendar with which the time will be counted through a dialog that shows all the calendars defined on the Knowledge Base (more info). If we don´t specify a calendar the process will be continuous, 24 x 7. By default, the calendar will be the process calendar if applicable.  
  
Metadata: It allows adding metadata to the activity.

**History Security**

Security in history: It allows constraining the historical information on the task that can be accessed by the users when displaying the process history. The admitted values are:  
  
    - All roles: any user accessing the process history can see the task.  
    - None: no user can see the task in the process history.  
    - Task roles: only the users with the role to execute the task can see it in the history.  
    - Selected roles: it allows specifying a list of roles enabled to see the task in the history.

**Adaptability**

Selectable for ad-Hoc: allows setting up whether the task appears in the successor tasks selection dialog shown on completing an ad-hoc task.

**Event Handling**

On assignment change: Change in the assignment of a task instance.  
On deadline: Deadline of an instance (process or task instance).  
On warning: Warning of an instance (process or task instance).  
On new instance: A new instance was created (process or task instance).  
On priority change: Change in the priority of an instance (Process or task instance).  
On resource non available: There are no resources (users) available to process the task.  
On state change: Change in the status of an instance (process or task instance.
