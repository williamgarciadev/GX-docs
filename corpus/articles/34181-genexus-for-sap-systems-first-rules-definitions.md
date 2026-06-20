---
title: "GeneXus for SAP Systems - First Rules definitions"
source_id: 34181
source_url: https://wiki.genexus.com/commwiki/wiki?34181
genexus_version: "18"
---

# GeneXus for SAP Systems - First Rules definitions

In addition to all the automatic controls included by GeneXus in the applications it generates, sometimes users request some specific controls.

In a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), the rules that must be complied with, or the controls that need to be validated, are defined in the Rules section.

For instance, if one of the requirements is not to allow storing clients without a name, there's a rule called [Error](https://wiki.genexus.com/commwiki/wiki?6852) that will prevent that from happening.

Type “Error”, open brackets and between single quotation marks, enter the text you want to have displayed if the user tries to leave a client's name blank. Close brackets, and now indicate the condition that must be met for that text to be displayed.

The condition is that the CustomerName attribute is empty. Write “if CustomerName”, period:

`[imagen omitida: wiki id 34242]`

and select: [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645).

**Note**: All the stated rules must end with a semicolon.

`[imagen omitida: wiki id 34243]`

Save and press F5 to see this rule at runtime.

Run the Customer Transaction object, and if the client's name is left blank, the text that had been defined will be displayed.

The [Error rule](https://wiki.genexus.com/commwiki/wiki?6852) doesn’t let you continue if the condition continues to be met, so, the user either enters a client's name or cancels.

Note that when clicking on the client’s surname, the message stays on screen, because the condition continues to be met.

`[imagen omitida: wiki id 54706]`

Enter a name and note that now you can continue entering the rest of the client's details.

If there's another requirement that prevents the client’s surname from being left blank, a similar rule needs to be stated. So, copy and paste this rule definition, replace “name” with lastname and change the attribute involved.

Press F5 and run Customer. Leave the client's name empty so that the error associated with a blank name is displayed. Then, enter "Paul" and leave the surname empty; the error message associated with a blank surname is displayed.

There is another rule whose syntax is very similar to that of the Error. It is called [Msg rule](https://wiki.genexus.com/commwiki/wiki?6854) and the only difference with Error is that if the condition is met, the message is displayed as a notice or warning, but the user can continue working. That is to say, it doesn’t prevent users from moving on, as the Error rule does.

Suppose you want to inform that the client's phone number has been left blank without forcing the user to enter it. To do so, create a Message rule: open brackets, enter the text between single (or double) quotation marks 'The phone is empty', close brackets, and then define the condition for the rule to be executed: “if CustomerPhone”, period, IsEmpty. Don't forget to add a semicolon to complete the rule's definition.

`[imagen omitida: wiki id 34247]`

Press F5 to try this functionality.

Note that if the phone number is left blank, and you try to move on, the message that you created is displayed. In this case, it is orange and it lets you continue.

`[imagen omitida: wiki id 54707]`

This set of rules could be written in any other order, and the result at runtime would be exactly the same because GeneXus decides when each one of the defined rules should be triggered (when the user leaves each involved field, etc.).

Of course, GeneXus offers more rules to define different kinds of validations and actions. See [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) to know more about this.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) | [GeneXus for SAP Systems First Rules definitions (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54700) |

---
