---
title: "GAM - Auto-register anonymous users"
source_id: 19395
source_url: https://wiki.genexus.com/commwiki/wiki?19395
genexus_version: "18"
---

# GAM - Auto-register anonymous users

Users are generally not too keen on registering to try an application. They prefer to do it anonymously and then register after the application has proven useful to them. Therefore, providing the same or similar functionalities to registered and non-registered users is a key to success in several markets. It implies a significant challenge from the programming viewpoint, even more so if you want to maintain the information provided by a user who worked anonymously after that user becomes registered.  
  
The activation of the [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) provides all the functionality required, with no need for significant considerations in the logic of the application.

Read more in:

• [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909)  
• [GAM - Auto-register anonymous users - How to identify them](https://wiki.genexus.com/commwiki/wiki?19910)  
• [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911)

### [Frequently Asked Questions (FAQs)](#Frequently+Asked+Questions+%28FAQs%29)

Q: **What permissions does the auto-registered user apply for executing?**  
A: Read the document [What permissions does the registered user apply for executing](https://wiki.genexus.com/commwiki/wiki?19917)

Q: **If the GAM user logs out and accesses again as an anonymous user, is it possible to recover that user’s information?**  
A: No, it isn’t. This must be solved programmatically, using [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) to store the user’s information when not logged in order to recover it after login.

Q: **What happens when an action or event in an object accepting the auto-registered user prompts the user to enter credentials.**  
A: [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835)


|  |
| --- |
| **Backlinks** |
| [Auto-register Anonymous User property](https://wiki.genexus.com/commwiki/wiki?19912) | [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835) | [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911) |
| [GAM - Auto-register anonymous users - How to identify them](https://wiki.genexus.com/commwiki/wiki?19910) | [GAM - Impersonation](https://wiki.genexus.com/commwiki/wiki?24241) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [What permissions does the registered user apply for executing](https://wiki.genexus.com/commwiki/wiki?19917) |

---
