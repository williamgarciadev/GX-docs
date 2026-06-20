---
title: "Facebook Button control"
source_id: 31841
source_url: https://wiki.genexus.com/commwiki/wiki?31841
genexus_version: "18"
---

# Facebook Button control

The Facebook Button control gives you public information about the end-user in this social network and helps to log in to/out of Facebook in an easy way, interacting with its native app or requesting through the browser.

In order to use this feature, you must configure the [Facebook App Id property](https://wiki.genexus.com/commwiki/wiki?19399).

## [Adding the button](#Adding+the+button)

This control must consolidate the user state information. The steps to incorporate the button are described below:

1. Define an attribute or variable based on Character or VarChar data type to catch the JSON string with the user data retrieved from Facebook.
2. Drag this attribute or variable from the toolbox to a Panel or Work With object.
3. Set the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to "Facebook Button"

Once finished, two new properties will be available:

* **Read Permissions**  
  A set of permissions for retrieved user data separated by commas.  
  By default, GeneXus asks for public profile information (i.e. *public\_profile*, *email*, *user\_friends*).  
  For advanced developers, a complete list of values can be found in [Facebook login permissons](https://developers.facebook.com/docs/facebook-login/permissions/v2.2?locale=es_LA).
* **Publish Allowed**  
  A boolean value to indicate if the app requires publishing permissions.  
  By default, it's set to False.

## [Facilities](#Facilities)

Once you sets the button appropriately, new facilities are available to manipulate the user data retrieved from Facebook.

### [Structured Data Types](#Structured+Data+Types)

**SocialUserData**

It encapsulates the user data retrieved from Facebook. It is enabled once the SD Facebook Button control is detected.

```
SocialUserData
{
    Id: Character(20)
    Name: Character(20)
    FirstName: Character(20)
    MiddleName: Character(20)
    LastName: Character(20)
    ProfileName: Character(20)
    ProfileImage: Image 
    Gender: Character(100)
    Birthday: Character(20)
    Country: VarChar(40)
    City: VarChar(40)
    Email: Email
    LocationLatitude: Character(20)
    LocationLongitude: Character(20)
}
```

**Note**: If SocialUserData does not have this structure, please download and import [this patch](https://wiki.genexus.com/commwiki/wiki?36490,,) in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

### [Events](#Events)

A set of events is available to catch the relevant information for you.  
All of the events accept input parameters.

**OnUserInfoUpdated**

This is the first event called after the end-user starts a new Facebook session (async process). Once it's finished and the connection has been established, the user information is updated and available to you.  
The typical usage of this method is to load the user data in a variable based on SocialUserData SDT using [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809).

**OnUserLoggedIn**

This is an informative event that you can use to update some indication of the state of the current Facebook session.  
In this event, the user information is not updated yet. Try to avoid it to deserialize the user information because you can have outdated information.

**OnUserLoggetOut**

This is an informative event that indicates when the user logged out of the Facebook session.

**OnError**

This event retrieves the Facebook default error when something goes wrong during the authentication process.  
This event is appropriate if you want to show a custom error when something goes wrong.

## [Example](#Example)

First, define a variable called *JsonUserData*based on the Character data type and drag it into the abstract layout of a Panel object.

Then, set its Control Type property to "Facebook Button" value and note the new two properties displayed.  
Also, the variable in the layout changes its appearance (is not shown as a text field).

`[imagen omitida: wiki id 31856]`

After that, define a new variable based on UserSocialData SDT (in this case is called *SocialData*). Then proceed to write an event to load it and say hello to our user.

`[imagen omitida: wiki id 31857]`

```
Event &JsonUserData.OnUserInfoUpdated
    Composite
        &SocialData.FromJson(&JsonUserData)
        msg(Format("Hello %1!",&SocialData.name))
    EndComposite
Endevent
```

Finally, the result in runtime is shown below.

**Android device**  
`[imagen omitida: wiki id 31858]`

**iOS device**  
`[imagen omitida: wiki id 31861]`

## 

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Data type** | Character, VarChar |
| **Generators** | Apple, Android, .NET, .NET Core, Java |

##


|  |
| --- |
| **Backlinks** |
| [Client Token property](https://wiki.genexus.com/commwiki/wiki?51723) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) |
| [HowTo: Request data from Facebook using Graph API and Access Token](https://wiki.genexus.com/commwiki/wiki?38437) | [Publish Allowed property](https://wiki.genexus.com/commwiki/wiki?42190) |
| [Read Permissions property](https://wiki.genexus.com/commwiki/wiki?42189) |

---
