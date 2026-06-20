---
title: "HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property"
source_id: 16565
source_url: https://wiki.genexus.com/commwiki/wiki?16565
genexus_version: "18"
---

# HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property

**Warning**: The solution explained in this document can only be used when GAM Authentication Type is [Local](https://wiki.genexus.com/commwiki/wiki?20703). It is not useful when the [Authentication Types](https://wiki.genexus.com/commwiki/wiki?16508) are Facebook, Google, or external because in these cases the ExternalID field of GAM User table is reserved. It stores the ID given by the external authentication provider.

This is a possible solution to the problem presented at [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552).

Given that the user is identified in the application's tables using any attribute, for example: *UserIdentification*, this article shows you how to store this information in the ExternalID field of the GAM *User* table, to match the application's users to the GAM users.

In this case, there's no need to make any reorganization to the application tables (unlike the solution explained in [HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643)).

It consists of saving the *UserIdentification* information in the ExternalID field each time the user is registered, and retrieving the data when the user logs in, to have the *UserIdentification* in the application's *User* table.

### [How to update the ExternalID of a GAM User](#How+to+update+the+ExternalID+of+a+GAM+User)

Suppose you already have the application's *User* table and you want to duplicate the users in a GAM database, mapping them using the ExternalID of GAM.

**1.** You need to run a procedure that scans the application's *User*table and updates the information in a GAM database table (inserts the users in a GAM Repository).

For each user in the application's *User* table, there will be a GAM user, whose ExternalID will be the *UserIdentification* in the application's *User* table.

So, the idea is to store, in the *ExternalID* property of the GAMUser, the PK of the application's *User* table - *Usercod* in this sample.  
  
The code in the [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) would be similar to the following:

```
For Each UserCod
    &User.GUID = &UserId  //&User is GAMUser data type, &UserId is GAMGUID data type
    &User.Name      = UserName
    &User.FirstName = UserFirstName
    &User.LastName  = UserLastName
    &User.Password  = UserPassword
    &User.EMail     = UserEmail
    &User.ExternalId = UserCod.ToString().Trim()
    
    &User.Save()
    
    if &User.Success()
        msg('User added to GAM Repository: ' + &User.Name)
    else
        &GAMErrors = &User.GetErrors() //&GAMErrors is collection of GAMError data type
        do 'ProcessErrors'
    endif
Endfor

Commit

Sub 'ProcessErrors'
    For &GAMError in &GAMErrors
        Msg(Format("%1 (GAM%2)", &GAMError.Message, &GAMError.Code))       
    EndFor
EndSub
```

**2.** To keep the users duplicated in the application's database and in the GAM database, you need to update both when the user registers or updates data. This is very similar to what it is explained in [HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643).  
  
Note that *GAMExampleEntryUser webpanel* (which belongs to GAM Example library) shows a way to add users to GAM Repository using an ExternalID (which have to be filled in with the User Identification in the application's *User* table).  
  
`[imagen omitida: wiki id 16566]`

If the GAM backend is used to manage the user's information, the [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) should be changed to update the user's information in the application's database and in the GAM database, referencing the *ExternalID* property with its corresponding value as explained before.

### [How to retrieve the user's information: GetExternalId method of GAMUser object](#How+to+retrieve+the+user%27s+information%3A+GetExternalId+method+of+GAMUser+object)

The GetExternalId method of GAMUser object gets the value stored in the ExternalID field of the GAM *User* table.

Consider a scenario where users only see the information that corresponds to them; for instance, only their own *TourReservations*.

You can use a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) that obtains the *UserCode* from the GAMUser who is logged in:

```
&UserIdentification = GAMUser.GetExternalId()
&UserCod =  &UserIdentification.ToNumeric()

parm(out:&UserCod);
```

Then in the *WWTourReservation*, you can filter data using that Procedure:

`[imagen omitida: wiki id 16567]`

### [See Also](#See+Also)

[HowTo: Filtering Data by User Using the GAM API](https://wiki.genexus.com/commwiki/wiki?15387)  
[HowTo: Mapping Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552)  
[GAM API: How to reference GAM users](https://wiki.genexus.com/commwiki/wiki?16534)


|  |
| --- |
| **Backlinks** |
| [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) | [HowTo: Reference GAM users using the GAM API](https://wiki.genexus.com/commwiki/wiki?16534) |

---
