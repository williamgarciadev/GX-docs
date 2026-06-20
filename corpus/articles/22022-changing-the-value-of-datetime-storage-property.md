---
title: "Changing the value of DateTime Storage property"
source_id: 22022
source_url: https://wiki.genexus.com/commwiki/wiki?22022
genexus_version: "18"
---

# Changing the value of DateTime Storage property

Changing the value of [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) may or may not require regenerating the application (that is to say, [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691)).

* A Rebuild All \_is\_ required when the value changes from Enabled (UTC or Application server values) to Disabled (Undefined value) or vice versa.

Navigation of objects with conditions (Conditions, Where) or with order by formulas that use functions described in [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) may change.

If you are absolutely sure your application does not have any objects in this situation you may skip regenerating it.

If you have any doubts, you may use the [Navigation Comparer](https://wiki.genexus.com/commwiki/wiki?3217,,) to search for changes in navigation.

* A Rebuild All is not required when the value changes from UTC to Application Server or vice versa.

### Application deployment after changing DateTime Storage property

If a Rebuild All was \_not\_ necessary or if your application navigation did not change you may only deploy the [Application configuration file](https://wiki.genexus.com/commwiki/wiki?22044,,).

Otherwise, you must deploy the newly generated application and the [Application configuration file](https://wiki.genexus.com/commwiki/wiki?22044,,).

### See also

[Changing the value of DateTime Storage property at application installation/upgrade time](https://wiki.genexus.com/commwiki/wiki?22045)


|  |
| --- |
| **Backlinks** |
| [Changing the value of DateTime Storage property at application installation/upgrade time](https://wiki.genexus.com/commwiki/wiki?22045) | [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
