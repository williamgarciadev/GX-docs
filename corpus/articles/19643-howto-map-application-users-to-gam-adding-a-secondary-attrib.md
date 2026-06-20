---
title: "HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser"
source_id: 19643
source_url: https://wiki.genexus.com/commwiki/wiki?19643
genexus_version: "18"
---

# HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser

In this scenario, a secondary attribute, named *UserIdentification* and of GAMGUID data type will be added to the application's *Users* table, linking the users to the [GAM](https://wiki.genexus.com/commwiki/wiki?24746) database (Figure 2). Note that there are other [ways to identify the GAM user](https://wiki.genexus.com/commwiki/wiki?16534) other than using GAMGUID.

##### [Figure 1.](#Figure+1.)

`[imagen omitida: wiki id 16556]`

##### [Figure 2.](#Figure+2.)

`[imagen omitida: wiki id 16557]`

The *UserIdentification* attribute can be set as [Candidate Key](https://wiki.genexus.com/commwiki/wiki?2199,,) depending on the needs of the application.

In this solution, the users are redundant in the GAM database table and in the application's database *AppUsers* table, so there must be a mechanism to keep both tables updated. Here you have a way to do it.

### [Keep GAM *User* table and the application's *AppUsers* table updated](#Keep+GAM+User+table+and+the+application%27s+AppUsers+table+updated)

**1.** In order to insert the users of the *AppUsers* table in GAM database, you need to run a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) that scans the *AppUsers*table and updates the information in the GAM database table (inserts the users in the GAM Repository).

The [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) code would be similar to the following:

```
For each UserCod

    &User.GUID = &UserId  //&User is GAMUser data type, &UserId is GAMGUID data type
    &User.Name            = UserName
    &User.FirstName        = UserFirstName
    &User.LastName        = UserLastName
    &User.Password        = UserPassword
    &User.EMail = UserEmail
    &User.Save()

    if &User.Success()
        msg('User added to GAM Repository: ' + &User.Name)
    else
        &GAMErrors = &User.GetErrors() //&GAMErrors is collection of GAMError data type
        do 'ProcessErrors'
    endif

Endfor
commit
Sub 'ProcessErrors'
    For &GAMError in &GAMErrors
        Msg(Format("%1 (GAM%2)", &GAMError.Message, &GAMError.Code))    
    EndFor
EndSub
```

**2.** Then, in the *Registration form* of the application, you need to update both, the user in the application's database and the same user in the GAM database. So, for each user who is registered, updated, or deleted in the application, you need to update GAM repository.

The following are the rules of the Transaction *AppUsers*, used to manage the users in this sample:

```
[web]
{
parm(in:&Mode, in:&UserCod);

UserCod = &UserCod if not &UserCod.IsEmpty();
noaccept(UserCod);
noprompt(UserCod);
}

UpdateGAMUser(UserIdentification,UserName,UserFirstName,UserLastName,UserAddress,UserPhone,UserEmail,&Error)
    if update
    on aftervalidate;

DeleteGAMUser(UserIdentification,&Error) if delete  on aftervalidate;

error('Please enter your Email') if UserEmail.IsEmpty();

[web]
{
    accept(&Password);
    accept(&PasswordConfirm);
   
    error('Passwords don´t match')
        if insert and &Password <> &PasswordConfirm;
       
    RegisterGAMUser(UserName,UserFirstName,UserLastName,UserAddress,UserPhone,UserEmail,&Password,UserIdentification,&Error)
            if insert  on aftervalidate;

}
    error('Data could not be updated, try again please') if &Error on aftervalidate;
```

#### [**Notes:**](#Notes%3A)

* The Procedures *RegisterGAMUser*, *UpdateGAMUser*, and *DeleteGAMUser* have Commit on Exit = No. The idea is to simulate only one [LUW](https://wiki.genexus.com/commwiki/wiki?2424), so that the user is updated in both databases (app DB, and GAM DB) or in none of them. That is why the *&Error* flag is also used, which is returned by those Procedures if there is a failure in GAM database user update.

Download the [sample](https://wiki.genexus.com/commwiki/wiki?16558,,) for more details.

* Take into account that if the GAM backend is also used to manage the users, the [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)s of the GAM backend have to be modified as well, so that the data is updated in the *Users* table of the application's database.

### [Samples](#Samples)

**Sample 1**

The following code is an example taken from the *RegisterGAMUser* Procedure:

```
&User.Name = &UserName   //&User is GAMUser data type
&User.FirstName = &UserFirstName
&User.LastName = &UserLastName
&User.Address = &UserAddress
&User.Phone = &UserPhone
&User.EMail = &UserEmail
&User.Password = &UserPassword
&User.Save()

if &User.Success()
        &UserIdentification = &User.GUID //&UserIdentification is GAMGUID data type
        &Error = False
else
    &GAMErrors = &User.GetErrors()  //&GAMErrors is collection of GAMError data type
    do 'ProcessErrors'
    &Error = True
endif

Sub 'ProcessErrors'
    For &GAMError in &GAMErrors
        Msg(Format("%1 (GAM%2)", &GAMError.Message, &GAMError.Code))
       
    EndFor
EndSub

parm(in:&UserName,in:&UserFirstName,in:&UserLastName,in:&UserAddress,in:&UserPhone,in:&UserEmail,in:&UserPassword,out:&UserIdentification,out:&Error);
```

**Note**: Since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,), [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) allows triggering a Procedure automatically when the GAM user is updated using GAM.

**Sample 2 - Filtering a user's data**

Suppose that a user has to see only their own *TourReservations*.

In order to filter only the data related to the user who has logged in, you need to add the following condition to the *WWTourReservation* Web Panel:

```
UserCod = GetUser();
```

##### [Figure 3.](#Figure+3.)

`[imagen omitida: wiki id 16555]`

Where *GetUser* is a Procedure that gets the GAM user who is logged in and returns the corresponding *UserCod* of the application's database:

```
&User = GAMUser.Get()
&GAMErrors = &User.GetErrors()
if &GAMErrors.Count > 0
    do 'ProcessErrors'
else
    &UserIdentification = &User.GetId()
     for each UserCod
         where UserIdentification = &UserIdentification
         &UserCod = UserCod
    endfor
endif

Sub 'ProcessErrors'
For &GAMError in &GAMErrors
    Msg(Format("%1 (GAM%2)", &GAMError.Message, &GAMError.Code))
EndFor
endsub

parm(out:&UserCod);
```

The same happens when calling the Transaction for registering new *TourReservations*, you have the following rule, so as the *UserCod* is instantiated with the user who has logged in:

```
equal(UserCod, GetUser());
```

The code of getting the user can also read the user from a Web Session.

Download the sample xpz from [here](https://wiki.genexus.com/commwiki/wiki?16558,,).

### [See Also](#See+Also)

[HowTo: Mapping Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552)


|  |
| --- |
| **Backlinks** |
| [HowTo: Map Application Users to GAM Users](https://wiki.genexus.com/commwiki/wiki?16552) | [HowTo: Map Application Users to GAM Users - Using ExternalID GAMUser property](https://wiki.genexus.com/commwiki/wiki?16565) |

---
