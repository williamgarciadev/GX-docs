---
title: "Logout options for Single Sign On using GAM"
source_id: 32336
source_url: https://wiki.genexus.com/commwiki/wiki?32336
genexus_version: "18"
---

# Logout options for Single Sign On using GAM

Regarding [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385), there are three different ways to implement a Logout.

First, the following has to be taken into account:

1. The Single Sign On feature behaves as explained in [GAM SSO flow of execution](https://wiki.genexus.com/commwiki/wiki?28106,,). Note that in this architecture there are n client applications (\*) and an Identity Provider. All of them have their own [GAM](https://wiki.genexus.com/commwiki/wiki?24746).
2. Internally, when the user logs in using the Identity Provider, a user session is created locally (on the local GAM), and two sessions are created on the Identity Provider's GAM. The sessions created on the server IP (from now on, Identity Provider) are the following:

* The session associated with the pair User - Client. Killing this session removes the user's Identity Provider connection.
* The user session on the server IP. Killing this session removes the possibility of establishing a new connection to the Identity Provider without performing a new login.

        3. Performing *GAMsession.logout* on the client without considering any of the options below, does not perform the server logout.

 (\*) "client application" means an applications running in a browser/device.

  Examples:

* one browser with three tabs opened with App1, App1, App2 means two "client applications" (i.e. App1 and App2).
* one browser with three tabs opened with App1, App1, App2 and another browser in the same device (or not) with App1 and App3 opened means four "client applications" (i.e. App1 and App2 for one side and App1 and App3 for the other side)

Basically, the Logout can be **Client-Side exclusively** (so the server's user session is kept alive), **Identity Provider & Client** (the user session on the server IP is killed), and **Identity Provider & All Clients**(all the client application's sessions are killed for the user, as well as the user session on the server IP).

## [Client-Side Only](#Client-Side+Only)

In this scenario, the session associated with the pair User - Client application is killed. Killing this session removes the user's Identity Provider connection. The next time he wants to log in from this client application, the server's Identity Provider session will be used if it remains alive (if it hasn't timed out).

The flow is as follows:

1. Logout is performed on the client and the user session on the client's GAM database is killed.
2. The session associated with the pair User - Client application is killed. However, the user's session is kept alive on the server.

Finally, a redirect is done to the [GAM Application logout object](https://wiki.genexus.com/commwiki/wiki?32354) of the client application where the log out was executed.

`[imagen omitida: wiki id 32374]`

## [Identity Provider & Client](#Identity+Provider+%26+Client)

1. Logout is done on the client and the user session on the client's GAM database is killed.
2. The session associated with the pair User - Client application is killed.
3. The user session on the server Identity Provider is killed. Then, if the user tries to log in, since the server session doesn't exist, he will be asked to enter his credentials again to log in to the Identity Provider. The user remains logged into the other applications while the local session in those applications is alive.

Finally, a redirect is done to the [GAM Application logout object](https://wiki.genexus.com/commwiki/wiki?32354) of the client application where the log out was executed.

`[imagen omitida: wiki id 32373]`

## [Identity Provider & All Clients](#Identity+Provider+%26+All+Clients)

1. Logout is performed on the client and the user session on the client's GAM database is killed.
2. For all the client applications, the session associated with the pair User - Client application is killed.
3. The user session is killed on the server.
4. For each application, the user session on the client application's GAM database is killed.

Finally, a redirect is done to the [GAM Application logout object](https://wiki.genexus.com/commwiki/wiki?32354) of the client application where the log out was executed.

`[imagen omitida: wiki id 32372]`

Using the Identity Provider & All clients options, since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) if the final users logsout from the Identity Provider, the client sessions (who run in the same browser instance) are also finished.

### [Logout example code](#Logout+example+code)

```
Event 'Logout'
    GAMRepository.Logout(&GAMErrorCollection) // &GAMErrorConnection variable is defined as GAMError,GeneXusSecurity data type and Collection = True.
    Refresh
Endevent
```

**Note**: It is important that a Redirect is not executed after the Logout.

## [How to configure the Logout options for SSO](#How+to+configure+the+Logout+options+for+SSO)

The option is configured using the [Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) under the Identity Provider's Repository Configuration (or programmatically, using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)).

`[imagen omitida: wiki id 32371]`


|  |
| --- |
| **Backlinks** |
| [GAM - GAMRemote Authentication Type](https://wiki.genexus.com/commwiki/wiki?25355) | [GAM Application logout object](https://wiki.genexus.com/commwiki/wiki?32354) |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [Single Sign On in applications using GAM](https://wiki.genexus.com/commwiki/wiki?25385) |

---
