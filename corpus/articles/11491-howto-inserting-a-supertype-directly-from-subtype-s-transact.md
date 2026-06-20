---
title: "HowTo: Inserting a Supertype Directly from Subtype’s Transaction"
source_id: 11491
source_url: https://wiki.genexus.com/commwiki/wiki?11491
genexus_version: "18"
---

# HowTo: Inserting a Supertype Directly from Subtype’s Transaction

There are some situations where we need to insert a subtype and the corresponding supertype at the same time; but it would be very useful to hide from the user the manipulation of the supertype transaction.

For instance, let us suppose we have these two Transactions:

```
Transaction Party
PartyId*
PartyName
```

```
Transaction People
PeopleId*     subtype of PartyId
PeopleName    subtype of PartyName
PeopleGender
```

The ideal case would be to insert, update or delete a People without manipulating the Party Transaction. This behavior can be implemented by means of SDT’s and some rules.

In order to do that you need to change the following:

### [Supertype Transaction](#Supertype+Transaction)

Just define Party as Business Component

### [Procedure to Insert, Update and Delete de Supertype](#Procedure+to+Insert%2C+Update+and+Delete+de+Supertype)

Rules:

```
parm(in:&Party, in:&Mode, out:&PeopleId, out:&Result);
//&Party is defined based on TRN Party 
//&Result is defined based on SDT with two elements: Success (Boolean) and Messages (Messages)
```

Source:

```
&Result.Success = True
&PartyNew = New TParty()
If &Mode <> TrnMode.Insert
  &PartyNew.Load(&Party.PartyId)
Endif
If &Mode = TrnMode.Delete
  &PartyNew.Delete()
Else
  &PartyNew.PartyName = &Party.PartyName
  &PartyNew.Save()
Endif
If &PartyNew.Fail()
  &Result.Mensajes = &PartyNew.GetMessages()
  &Result.Success = False
Else
  &PeopleId = &PartyNew.PartyId
  &Result.Success = True
Endif
```

Properties:

```
Commit on Exit = No
```

### [Subtype Transaction](#Subtype+Transaction)

Variables:

Defined &Party based on Party BC.

Web Form:

In the Web Form, substitutes the inferred subtype by their corresponding variable. In this case:  
PeopleName by &Party.Name  
  
Start Event:

```
PeopleId.Visible = 0
If not &PeopleId.IsEmpty()
  &Party.Load(&PeopleId)
Endif
```

Rules:

```
RefCall(PABMParty, &Party, &Mode, PeopleId, &Result);
PABMParty.Call(&Party, &Mode, PeopleId, &Result) If Update dependencies PeopleId;

&ResultString = PResultGetString.Udp(&Result) if (update or insert);
Error(&ResultString.Trim()) If (update or insert) and &Result.Success = False dependencies PeopleId;

​​​​​​​PABMParty.Call(&Party, &Mode, PeopleId, &Result) If Delete on Beforecomplete;
&ResultString = PResultGetString.Udp(&Result) If Delete on Beforecomplete;
​​​​​​​Error(&ResultString) If Delete and &Result.Success = False on Beforecomplete;
```

Refcall is triggered when the referential integrity failed. In this case the procedure to insert a new Party is called on.

The same object is also called in the update and delete mode. In the delete mode it is called on BeforeComplete events because the Party needs to be deleted after the referenced People.

The rest of the rules enable you to show the possible error message when you insert/update/delete the supertype in the subtype transaction error viewer.
