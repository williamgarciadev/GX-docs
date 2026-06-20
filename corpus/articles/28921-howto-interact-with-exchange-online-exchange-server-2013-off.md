---
title: "HowTo: Interact with Exchange Online, Exchange Server 2013, Office 365"
source_id: 28921
source_url: https://wiki.genexus.com/commwiki/wiki?28921
genexus_version: "18"
---

# HowTo: Interact with Exchange Online, Exchange Server 2013, Office 365

**Deprecated** Microsoft has deprecated the EWS API and should not be used anymore. Please use SMTPSession and Pop3Session with Oauth to access a Exchange Mailbox.

To read and send messages using Microsoft Exchange Online, Microsoft Exchange Server 2013 or Office 365, you can use the following API.

### [**Properties**](#Properties)

* **ServerUrl**: Character  
  Exchange Server URL. If it is empty, the API tries to find a server based on the UserName.
* **UserName**: Character  
  Email of the user as defined in the Exchange Server
* **Password**: Character
* **AttachDir**: Character  
  Attached files will be saved here. If it is empty, the attachments will not be downloaded.
* **Count**: Numeric  
  Total number of messages or number of unread messages depending on the NewMessages property.
* **NewMessages**: bool  
  True: (Default) Only unread emails are read  
  False: All emails are read
* **SetProperty(Character key, Character value)**  
  Allows setting a property and its associated value. It may be used, for example, to set the Exchange Server version.
* **ErrCode**: Numeric
* **ErrDescription**: Character

### [**Methods**](#Methods)

* **Login**()  
  Starts the connection with the Exchange Server.
* **Logout**()  
  Ends the connection with the Exchange Server.
* **Receive**(MailMessage): Numeric  
  Downloads the message from the server. Returns 0 if it succeeded. By default, it downloads the message from the 'Inbox' folder.
* **Send**(MailMessage): Numeric
* **Delete**(MailMessage): Numeric
* **MarkAs**(MailMessage, IsRead): Numeric

IsRead = true. Mark the message as Read. IsRead = false, marks the message as unread.

* **GetMailMessage**(MsgId, Boolean FetchEntireMessage, MailMessage): Numeric

Gets the MailMessage with the MsgId specified. FetchEntireMessage indicates if MailMessage must be downloaded completely (subject, body, attachments) from server.

* **ChangeFolder**(Character): Numeric  
  Changes the folder for the next Receive() operations. Backlashes must be used to refer to Subfolders (e.g., 'Folder1\Subfolder11\Subfolder111')

### [**Error Codes**](#Error+Codes)

|  |  |
| --- | --- |
| **Code** | **Message** |
| 0 | Ok |
| 5 | Could not change folder |
| 10 | Could not send message |
| 11 | No messages to receive |
| 15 | Invalid Attachment |
| 16 | Could not save attachment |
| 22 | Error receiving message |
| 24 | Authentication Error |
| 27 | Mail Message with Id not found |

Sample to receive new Emails:

```
Event 'ReceiveMails'
    Do 'Login'
    
    if (&GXMailExchange.ErrCode = 0)
        &MailMessage = new()
        do while (&GXMailExchange.Receive(&MailMessage) = 0)
            
            &MailMessageSDT.Subject = &MailMessage.Subject
            &MailMessageSDT.From = Format(!"%1 (%2)", &MailMessage.From.Name, &MailMessage.From.Address)
            
            if (not &MailMessage.Text.IsEmpty())
                &MailMessageSDT.Body = &MailMessage.Text
            else
                &MailMessageSDT.Body = &MailMessage.HTMLText
            endif
            &MailMessageSDT.DateReceived = &MailMessage.DateReceived
            &MailMessageSDT.DateSent = &MailMessage.DateSent
            
            for &attach in &MailMessage.Attachments
                &MailMessageSDT.Attachments.Add(&attach.Trim())
            endfor
                    
            //Mark As Read
            &GXMailExchange.MarkAs(&MailMessage, true)        
            
            //Delete Message
            //&GXMailExchange.Delete(&MailMessage)        
                    
            &MailMessages.Add(&MailMessageSDT)
            &MailMessageSDT = new()
            &MailMessage = new()
        enddo
    
        
    else
        msg(!"Error: " + &GXMailExchange.ErrDescription)                
    endif
    
Endevent

Sub 'Login'
    
    &GXMailExchange.SetProperty(ExchangeVersion.Property, &ExchangeVersion)
    
    &GXMailExchange.ServerUrl = &ServerUrl.Trim()
    &GXMailExchange.UserName = &UserName.Trim()
    &GXMailExchange.Password = &Password.Trim()
    &GXMailExchange.AttachDir = &AttachDir.Trim()
    
    &GXMailExchange.NewMessages = &FetchNewMessagesOnly
    
    &GXMailExchange.Login()    
EndSub
```

where

* *&GXMailExchange* variable data type is GXMailExchange (External Object)

### [Requirements](#Requirements)

* [GXMicrosoftExchangeXPZ](https://wiki.genexus.com/commwiki/wiki?28922,,)

### [Availability](#Availability)

.NET Generator of [GeneXus X Evolution 3 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?28251,,)

For Java Generator use the [Java mail](https://www.genexus.com/developers/websac?en,,,33666) implementation.
