---
title: "Business Components - Differences between the Save method and the Insert and Update methods"
source_id: 31703
source_url: https://wiki.genexus.com/commwiki/wiki?31703
genexus_version: "18"
---

# Business Components - Differences between the Save method and the Insert and Update methods

While the [Save method](https://wiki.genexus.com/commwiki/wiki?23229) takes into account the current mode of the variable based on the [business component](https://wiki.genexus.com/commwiki/wiki?5846) to which it is applied, the [Insert](https://wiki.genexus.com/commwiki/wiki?31695) and [Update](https://wiki.genexus.com/commwiki/wiki?31696) methods don't take it into account to determine if an addition or an update has to be performed in the database. The [Insert](https://wiki.genexus.com/commwiki/wiki?31695) and [Update](https://wiki.genexus.com/commwiki/wiki?31696) methods directly perform the operations indicated by their names.

In addition, the Update method does not require the use of the [Load method](https://wiki.genexus.com/commwiki/wiki?23211), as opposed to the Save method when it is used to update the database. This is advantageous because the Load method produces an access to the database and it can be avoided.

So, the first code is more performant than the second, even though the result of both of them is the same:

**1)**

```
&Customer=new()   //in this case the new operator can be omitted, but if several customers are updated, it must be used
&Customer.CustomerId = 8    
&Customer.CustomerEmail = !'marybrown@gmail.com'
If &Customer.Update()
   commit
else
   rollback
endif 
```

**2)**

```
&Customer.Load(8)
&Customer.CustomerEmail = !'marybrown@gmail.com'
&Customer.Save()
if &Customer.Success()
  commit
else
  rollback
endif
```

**Note:** If the above codes are inside a loop, by using the Load() method, you don't need to use the New operator (because the variable is reloaded every time regardless if you are using the Save or the Update method). On the other hand, if you decide to assign the primary key attribute(s) value(s), you have to precede that assignment with the New operator.


|  |
| --- |
| **Backlinks** |
| [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Business Component Update method](https://wiki.genexus.com/commwiki/wiki?31696) |

---
