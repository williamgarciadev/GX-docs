---
title: "HowTo: Get user's additional information from the GAM Identity Provider"
source_id: 37703
source_url: https://wiki.genexus.com/commwiki/wiki?37703
genexus_version: "18"
---

# HowTo: Get user's additional information from the GAM Identity Provider

When using [GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355), sometimes it may be necessary to retrieve additional information about the user from the Identity Provider. For example, after the user logs in, retrieve his place of work, or his salary. This information belongs to the Identity Provider and may have to be transferred to the client after login.

The so-called dynamic attributes of a user (or extended attributes) are managed through the "gam\_user\_additional\_data" scope as explained in this article:[Identity Provider Configuration for GAM Remote Authentication](https://wiki.genexus.com/commwiki/wiki?37038). Nevertheless, in some scenarios, it may be necessary to transfer to the client other information besides the extended attributes of the user.  
  
In such cases, the solution consists of using the [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698).  
Let's see it in more detail.

### [Implementation](#Implementation)

The information you want to pass from the Identity Provider to the Client is loaded using a procedure (named for example "servereventsubscription").  
That procedure is going to be subscribed to the *User\_GetCustomInfo* event in the GAM of the Identity Provider. It will trigger automatically after the login is executed.

`[imagen omitida: wiki id 37712]`

The procedure must have a specific interface:

**parm(in:&EventName,in:&JsonIn,out:&JsonOut);**

where

**EventName**: Belongs to the GAMEvents Domain.  
**JsonIn**: It's a json string whose structure is that of the *GAMsession* object.  
**JsonOut**: It's a json string with free format. There, you return the information you want, in any format.

### [Example](#Example)

Consider a scenario where the Client application of a GAM Identity Provider needs to get the salary and the salary incentive of the user who logs into the Identity Provider.

So, in the Client configuration, we need to add the necessary Additional Scopes to the Remote Authentication Type defined. In this case, we add the salary and salary\_incentive scopes, separated by '+'. Note that all the other scopes that need to be added are separated by '+' (such as the gam\_user\_additional\_data, if it's needed).

`[imagen omitida: wiki id 37711]`

First, we need to program a procedure which runs in the Identity Provider's and gets the information you're interested in, assuming that the GAMUser logged in can be obtained from the GAMSession received as a string parameter in JSON format.

The Scopes are also obtained from the GAMSession received. There you have a string where each scope is separated by '+'. You have to parse this string to search for the scope you are expecting to receive. In the following example, note that we search for the "salary" and "salary incentive" scopes. If those scopes aren't received, the procedure returns an empty string.

So the code is as follows:

```
parm(in:&EventName,in:&JsonIn,out:&JsonOut);

&GAMSession.FromJsonString(&jsonIN) //Get the GAMSession from the in parameter.

&UserGUID = &GAMSession.User.GUID //Get the GAMUser from the GAMSession obtained previously.
&Scopes    = &GAMSession.Scope.SplitRegEx(!"\+") //Read the scopes from the GAMSession.

&i = 1
Do while &i <= &Scopes.Count
    &ScopeReceived = &Scopes.Item(&i)
    If  &ScopeReceived = !"salary"
        do "GetSalary"
    else
        if &ScopeReceived = !"salary_incentive"
            do "GetSalaryIncentive"
        endif
    endif
    &i = &i + 1
EndDo

&jsonOUT = &SDT_UserCustomInfo.ToJson()
//Search for the salary of the user.
sub "GetSalary"
    for each Users
        where UserGUID = &UserGUID
        &SDT_UserCustomInfoItem = new()
        &SDT_UserCustomInfoItem.Id         = "salary"
        &SDT_UserCustomInfoItem.Value     =  userSalary.ToString()
        &SDT_UserCustomInfo.Add(&SDT_UserCustomInfoItem)
    endfor
endsub

sub "GetSalaryIncentive"
    for each Users
        where UserGUID = &UserGUID
        &SDT_UserCustomInfoItem = new()
        &SDT_UserCustomInfoItem.Id         = "salary_incentive"
        &SDT_UserCustomInfoItem.Value     =  userSalaryIncentive.ToString()
        &SDT_UserCustomInfo.Add(&SDT_UserCustomInfoItem)
    endfor
endsub
```

As stated above, the output is free format, so we've defined the following SDT (named UserCustomInfoItem) to store the information that we need to retrieve.

`[imagen omitida: wiki id 37706]`

In this example, the string returned for a given user, could be the following : [{"Value":"1000000","Id":"salary"},{"Value":"1000","Id":"salary\_incentive"}]

### [How to retrieve the information in the client?](#How+to+retrieve+the+information+in+the+client%3F)

In the Client, we subscribe to the User\_SaveCustomInfo event, which triggers automatically after the login. In this example, the procedure is called "clienteventsubscription".

`[imagen omitida: wiki id 37713]`

In the procedure subscribed to that event, we should program all the steps we need to execute using the information returned from the Identity Provider (in our example, the salary and the salary incentive).

The interface of the procedure is always as follows:

**Parm(in:&EventName, in:&jsonIN, out:&jsonout);**

where

**EventName**: Belongs to the GAMEvents Domain.  
**JsonIn**: It's a json string with free structure, where the information is passed from the Identity Provider to the client.  
**JsonOut**: It's a json string with a free format; it can be used for error handling.

The code of the example is the following:

```
&SDT_UserCustomInfo.FromJson(&JsonIn) // SDT_UserCustomInfo is based on the UserCustomInfoItem SDT.

for &SDT_UserCustomInfoItem in &SDT_UserCustomInfo
   //Save the data: &SDT_UserCustomInfoItem.id
  //Save the data:  &SDT_UserCustomInfoItem .value
endfor
```

### [Conclusion](#Conclusion)

The solution consists of using GAM Events subscription and specifying the correct Additional Scope in the Client configuration.


|  |
| --- |
| **Backlinks** |
| [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) | [HowTo: Use GAM as an OAuth 2.0 provider](https://wiki.genexus.com/commwiki/wiki?45493) |

---
