---
title: "Common Errors: GXflow Client Sign In"
source_id: 7884
source_url: https://wiki.genexus.com/commwiki/wiki?7884
genexus_version: "18"
---

# Common Errors: GXflow Client Sign In

Here you can see the most common errors at the GXflow Client Sign In:

`[imagen omitida: wiki id 7885]`

**Cause**  
The username or password is wrong. The user's nomination is not being checked only for existence in the GXflow database.

`[imagen omitida: wiki id 7886]`

**Cause**  
The user has not been nominated.

**Solution**  
Open the License Manager and nominate the user. To do so, go to Start->Programs->  
Genexus ->GeneXus License Manager -> GXflow Client X and click the Authorized User button to  
add the user.

`[imagen omitida: wiki id 7889]`

**Cause**  
The user is blocked because a wrong password has been entered several times.

**Solution**  
If you have another administrator user, use it to enter and unblock the user from the "Participants" option in the process manager or from the "Users" option in the organizational model.  Otherwise, access the GXflow database and change the WFUserBloc attribute located in the WFUsers table by assigning it the 0 value.


|  |
| --- |
| **Backlinks** |
| [Category:GXflow Client](https://wiki.genexus.com/commwiki/wiki?17835) |

---
