---
title: "Validation Procedure property"
source_id: 42594
source_url: https://wiki.genexus.com/commwiki/wiki?42594
genexus_version: "18"
---

# Validation Procedure property

Procedure object used to validate the User Input.

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

The Validation Procedure is available for any [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) and is triggered as soon the user enters data for that user input.

It is useful to validate the user's entry and give him feedback about that entry.

Basically, every time that the validation procedure is executed, it returns a Boolean variable and a text message.

The Validation Procedure has two possible signatures(1):

```
1. parm(in:&UserInput,out:&Error,out:&CustomResponse);
2. parm(in:&UserInput,inout:&Context,out:&Error,out:&CustomResponse);
```

where

* &UserInput is the [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) (the parameter must be of the same data type of the User Input).
* &Error is Boolean
* &CustomResponse is a string parameter that contains the message to be displayed when the user fails to enter correct data.
* &Context is a variable based on the Context SDT generated for the chatbot's instance (you have to [generate the chatbot](https://wiki.genexus.com/commwiki/wiki?40241) to have the Context SDT). For example, if the instance is "Ctizen" the SDT context is under the module CitizenChatbot. The Context contains all the [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351).

The message (&CustomResponse) is displayed to the user, regardless of the value of the Boolean output (whether there is an error in the validation or not).

So, the validation procedure can be used for two purposes:

1. When there is an error in the validation, warn the user and give him a hint to enter a valid value.

That is, ask the user to retry if the entered value is not valid (for the model). For instance, you can ask the user to enter the country where a discount is going to be available. Although the user enters a valid country, it may not be the country where that discount applies. There, the chatbot can ask the user to enter the information again (giving a hint of the valid countries for the discount).

2. When the validation is right, to go on with another user input, you can change the message for the user (asking him for the next user input), depending on the logic of the procedure. For example, if the user is buying a car, and he enters the card make he is interested in, the validation procedure can change the message of the following user input and give the user a hint of the years of the models available.

One possible flow of the conversation:

Bot: I have the following models available: Onix, Corolla  
User: I want the Onix  
Bot: Ok, I have it available in the years 2018 and 2019.

Another possible conversation:

Bot: I have the following models available: Onix, Corolla  
User: I want the Corolla  
Bot: Ok, I have it available in 2018, 2019, and 2020 model years.

Therefore, what is configured in the [Ask Messages property](https://wiki.genexus.com/commwiki/wiki?40217) of the following user input is replaced by the message returned by the validation procedure.

**Note**

The user input may have other validations (such as [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295)), or even the data type - which is always checked for the user input (e.g. if it's a date, the AI Provider sends an error if the user enters data which isn't in a valid date format).  
Those validations are combined with the Validation Procedure:

* The data is requested.
* The AI Provider validates if it matches the entity ([Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) and/or the data type).
* If it doesn't match, it asks the user to enter it again (here the [Try Limit property](https://wiki.genexus.com/commwiki/wiki?40216) is used to determine the number of times the user is asked to retry).
* If it matches, the data is assigned to the parameter.
* The Validation Procedure is run.
* If it is not valid (the validation procedure returns &Error = TRUE), it goes back (implicitly clears the parameter in the context) and the user is asked to enter it again.
* The data is requested again.

#### [Temporary Limitation](#Temporary+Limitation)

The [Try Limit property](https://wiki.genexus.com/commwiki/wiki?40216) does not apply to the validation procedure yet. There isn't an automatic mechanism to count the failed attempts. You can have an internal counter for the maximum number of attempts, which can be implemented using the [Context API](https://wiki.genexus.com/commwiki/wiki?41364).

(1) The parameter names can be anything, except for data types, which have to be the expected ones. Otherwise, you'll get an error like the following:

error: Unexpected Data Type. The Data Type of the x parameter must be the same as the User Input Data Type NUMERIC.

### [Samples](#Samples)

Consider the [Citizen Service Chatbot sample](https://wiki.genexus.com/commwiki/wiki?40937) where several complaints can be sent to citizen services in relation to sanitation, traffic, etc.

In this sample, there is a [Flow](https://wiki.genexus.com/commwiki/wiki?38531) called "StatusClaim" where the user can enter his Identification and the Complaint ID (a number he was given when he made the complaint). Given that information, the chatbot answers the status of the complaint (it can be pending to be solved, or solved).

Then the following Flow is defined, where the ComplaintId user input has the Validation Procedure property set to "ValidateComplaint," which is a procedure of the KB.

`[imagen omitida: wiki id 42692]`

The "ValidateComplaint" procedure is as follows:

```
parm(in:&ComplaintId,out:&Error,out:&ResponseforFailure);
```

```
Chatbot.Context.GetUserContextValue(!"CitizenAdv",GetUserId(),!"UserIdentification",&ParameterValue)
for each Complaint
    where ComplaintId = &ComplaintId
    where UserIdentification.Trim().ToLower() = &ParameterValue.Trim().ToLower()
    
    &Error              = FALSE
    exit
when none
    &Error              = TRUE
    &ResponseforFailure = format(!"%1 isn't a valid complaint Id. Try again please.",&ComplaintId.ToString())
endfor
```

Note that the [Chatbots Context API](https://wiki.genexus.com/commwiki/wiki?41364) is used to get the UserIdentification (which is in the [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351)) as another parameter to find out if the complaint ID provided is valid (if it belongs to the user).

Another possibility for this example, would have been to receive the Context as parameter (&Context is based con CitizenAdvChatbot.Context SDT).

```
parm(in:&ComplaintId,inout:&Context,out:&Error,out:&ResponseforFailure);

&UserIdentification = &Context.Context.UserIdentification

for each Complaint
  where ComplaintId = &ComplaintId
  where UserIdentification.Trim().ToLower() = &UserIdentification 

  &Error = FALSE
  exit
when none
  &Error = TRUE
  &ResponseforFailure = format(!"%1 isn't a valid complaint Id. Try again please.",&ComplaintId.ToString())
endfor
```


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [HowTo: Get the User ID when using chatbots and WhatsApp channel](https://wiki.genexus.com/commwiki/wiki?45850) | [HowTo: Send and receive a message from the Provider](https://wiki.genexus.com/commwiki/wiki?42971) |

---
