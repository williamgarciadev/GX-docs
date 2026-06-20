---
title: "Implementing Authentication and Logout Using the GAM API"
source_id: 15938
source_url: https://wiki.genexus.com/commwiki/wiki?15938
genexus_version: "18"
---

# Implementing Authentication and Logout Using the GAM API

The GAM\_Examples folder contains a large number of GeneXus objects. They are part of the GAM that is automatically installed in the KB when the property Enable Integrated Security is set to True.

Some of them, such as GAMExampleLogin and GAMExampleHome, are used in the first sequence of screens for the session. They are both regular Web Panels with the right programming for the security system to perform its function.

Even so, the developer will be allowed to make as many changes as needed; therefore, backing up the objects to be changed is recommended. A good practice could be to create a new folder, for instance “New Security System”, and copy the GeneXus objects from the GAM\_Examples folder to this new folder and make the changes there. Actually, the objects saved in the GAM\_Examples folder are precisely examples that show how to program the GAM and how to handle its API.

### [Examples](#Examples)

The examples below show how to use the GAM API based on the feature programmed in a couple of sample Web Panels.

##### [Implementing Authentication](#Implementing+Authentication)

The authentication mechanism consists of using a Web Panel and some of the objects published as external objects in the GAM\_Library folder. The Web Panel where the login mechanism is implemented through the GAM is GAMExampleLogin.

`[imagen omitida: wiki id 15872]`

Basically, it has three variables which, in turn, are based on their corresponding domains included in GeneXus by default: &UserName, &UserPassword and &UserRememberMe. The label “Forgot your password” is just a text block with the SmallLink class that has been assigned the 'ForgotPassword' user event.

Lastly, the Login button is assigned to the Enter event.  
Let’s see an example of the mechanism used by the GAM to implement these features through its API. Below is the event code:

```
Event Enter
        &AdditionalParameter.RememberUserType = &UserRememberMe
        &LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors)
        If not &LoginOK
           If &Errors.Count > 0 and
            (&Errors.Item(1).Code =
                    GAMErrorMessages.UserPasswordExpired or
             &Errors.Item(1).Code = 
                    GAMErrorMessages.UserPasswordMustBeChanged)
               GAMExampleChangePassword(&UserAutType, &UserName, &UserRememberMe )
           Else
               Do 'DisplayMessages'
           EndIf
        Endif
EndEvent
```

Now look at the first equation, which uses the RememberUserType property of the &AdditionalParameter variable that is based on the external object GAMLoginAdditionalParameters. Look at the following images:

`[imagen omitida: wiki id 15873]`

The Folder View shows the external object and its contents are displayed to the right. There, the property RememberUserType based on Numeric(2) is defined. The image at the front shows the AdditionalParameter variable of the Web Panel and its type, which in turn is assigned to the external object itself (actually, to any of its properties and methods).

Now, in the image below we can see the relationship existing between the &UserRememberMe variable and the &AdditionalParameter variable:

`[imagen omitida: wiki id 15939]`

Thus, the declaration:

```
&AdditionalParameter.RememberUserType = &UserRememberMe
```

...assigns the value of the &UserRememberMe variable to the &AdditionalParameter variable through its RememberUserType property (this can be done since &AdditionalParameter is based on the external object. Therefore, it inherits all its properties and methods).

Likewise, in the following declaration:

```
&LoginOK = GAMRepository.Login(&UserName, &UserPassword, &AdditionalParameter, &Errors)
```

...the &LoginOK variable will receive the resulting value from the call to the Login method of the GAMRepository external object; in the DB\_GAM, it will check whether the username and password are correct, which will return True or False.

`[imagen omitida: wiki id 15875]`

In the previous image, we can see part of the structure of the GAMRepository external object. Note that the Login method lists the four parameters sent in the declaration using variables.  
Next, the following code of the event checks the variable status and solves it accordingly. Note that other methods and properties of the GAM API continue to be used.

#### [Solving the Logout](#Solving+the+Logout)

The Logout can be easily implemented. In the image below, a button labeled Logout has been added to the front-end menu of an application.

`[imagen omitida: wiki id 15876]`

In its event, the following has been programmed:

```
Event 'Logout'
    GAMRepository.Logout(&Errors)  
EndEvent
```

This instruction loads the user data in the GAM\_DB repository. If errors occur, they are received in the SDT &Errors.

Examine the contents of all the events in the Web Panel’s Events tab, always using the same criteria described in the above examples.

**Note**: Do not delete the WebSession (&WebSession.Destroy()) if you use the GAMRepository.Logout() method, GAM does it inside the Logout method, in case of destroying the session before calling the Logout method, it will not work correctly..
