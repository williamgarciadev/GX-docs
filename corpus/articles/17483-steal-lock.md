---
title: "Steal Lock"
source_id: 17483
source_url: https://wiki.genexus.com/commwiki/wiki?17483
genexus_version: "18"
---

# Steal Lock

If one of your co-workers acquires a lock and then goes on holiday without releasing it, what do you do? GXserver provides a means to force locks. Releasing a lock held by someone else is referred to as Breaking the lock, and forcibly acquiring a lock which someone else already holds is referred to as Stealing the lock. Naturally these are not things you should do lightly, try first the contact with your co-workers.

Locks are recorded in the repository, and a lock token is created in your local working copy. If there is a discrepancy, for example if someone else has broken the lock, the local lock token becomes invalid. The repository is always the definitive reference. You can check locks on the [GXserver console locks](https://wiki.genexus.com/commwiki/wiki?26410,,) menu.


|  |
| --- |
| **Backlinks** |
| [Force Edit](https://wiki.genexus.com/commwiki/wiki?17486) |
| [Team Development Contextual Menu](https://wiki.genexus.com/commwiki/wiki?31972) |

---
