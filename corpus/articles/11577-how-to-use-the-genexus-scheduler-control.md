---
title: "How to use the GeneXus Scheduler Control"
source_id: 11577
source_url: https://wiki.genexus.com/commwiki/wiki?11577
genexus_version: "18"
---

# How to use the GeneXus Scheduler Control

## [When to use it?](#When+to+use+it%3F)

If you want to show a serie of chronological events by day, week or month probably this is the control that will fit your needs.

## [What does it look like?](#What+does+it+look+like%3F)

`[imagen omitida: wiki id 11579]`

`[imagen omitida: wiki id 11580]`

## [How to use it?](#How+to+use+it%3F)

The scheduler control is available in the GeneXus toolbox as many other controls. If you want to use it:

1. First of all, drag it on to your webpanel form.
2. In order to load the events set the control's LoadObjectEvents property with a Procedure or DataProvider which must return an SDT with the corresponding events. Take a look on **How must be the LoadObjectEvents DataProvider look like** for details.
3. Handle the EventAdded, EventDeleted or EventUpdated if needed. Take a look on **How to handle Scheduler user events** for details.

## [**How must the LoadObjectEvents Data Provider look like?**](#How+must+the+LoadObjectEvents+Data+Provider+look+like%3F)

This DataProvider is in charge of loading the events of a given period. Must have the following parameter:

```
parm(&dateFrom, &dateTo,&events);
   // &dateFrom and &dateTo must be Date
```

And the Data Provider's SDT (&events) must be of type SchedulerEvents.

#### [Example 1: Loading a set of fixed data](#Example+1%3A+Loading+a+set+of+fixed+data)

This is the Data Provider used to show the previous screenshots:

```
CalendarEvents
{
	Items
	{
		event
		{
			Id = "1"	
			Notes = "<img  src='http://i.conmebol.com/banderas/VEN_flag_ssm.gif' /> <img src='http://i.conmebol.com/banderas/URU_flag_ssm.gif' />Venezuela vs Uruguay"
			StartTime = ctot("06/11/2009 01:00 AM")
			EndTime = ctot("06/11/2009 03:00 AM")
			
		}
		event
		{
			Id = "2"	
			Notes = "<img src='http://i.conmebol.com/banderas/COL_flag_ssm.gif' /> <img src='http://i.conmebol.com/banderas/PER_flag_ssm.gif' />Colombia vs Peru"
			StartTime = ctot("06/10/2009 11:00 PM")
			EndTime = ctot("06/10/2009 11:45 PM")
			
		}
		event
		{
			Id = "3"	
			Notes = "<img src='http://i.conmebol.com/banderas/ECU_flag_ssm.gif' /> <img src='http://i.conmebol.com/banderas/ARG_flag_ssm.gif' />Ecuador vs Argentina"
			StartTime = ctot("06/10/2009 09:00 PM")
			EndTime = ctot("06/10/2009 11:00 PM")
			
		}
		event
		{
			Id = "4"	
			Notes = "<img src='http://i.conmebol.com/banderas/BRA_flag_ssm.gif' /> <img src='http://i.conmebol.com/banderas/PAR_flag_ssm.gif' />Brasil vs Paraguay"
			StartTime = ctot("06/11/2009 00:50 AM")
			EndTime = ctot("06/11/2009 01:50 AM")
		}
		event
		{
			Id = "5"	
			Notes = "<img src='http://i.conmebol.com/banderas/CHI_flag_ssm.gif' /> <img src='http://i.conmebol.com/banderas/BOL_flag_ssm.gif' />Chile vs Bolivia"
			StartTime = ctot("06/11/2009 01:00 AM")
			EndTime = ctot("06/11/2009 03:00 AM")
		}
	}
}
```

#### [Example II: loading event from the database](#Example+II%3A+loading+event+from+the+database)

If you have the events stored in the database you can write something like this:

```
CalendarEvents
{
   items
   {
      event
         where EventStart >= &dateFrom
         where EventEnd   <= &dateTo
      {
          Id                    = EventId
          StartTime             = EventStart
	  EndTime               = EventEnd
	  Notes                 = EventDescription
	  AdditionalInformation = EventDetails
      }
   }
}
```

## [How to handle Scheduler user events?](#How+to+handle+Scheduler+user+events%3F)

The Scheduler control expose four events: EventAdded, EventDeleted, EventUpdated, EventSelected

These events are essential when you want to allow the user to create, update or delete events directly using the Scheduler control. When the Scheduler control raise one of these events it load the property CurrentEvent that is bound to a variable (by default the variable is called &currentEvent).

So, suppose you want to add the event to your data store when the control raise the EventAdded

```
Event gxCalendar1.EventAdded
	&eventTrnBC.EventId = &currentEvent.Id
	&eventTrnBC.EventStart = &currentEvent.StartTime
	&eventTrnBC.EventEnd = &currentEvent.EndTime
        &eventTrnBC.EventDescription = &currentEvent.Notes
	&eventTrnBC.EventDetails = &currentEvent.AdditionalInformation
	&eventTrnBC.Save()
	commit	
EndEvent
```

## [Sample KB](#Sample+KB)

See [Patient Appointment KB](https://wiki.genexus.com/commwiki/wiki?11725,,).
