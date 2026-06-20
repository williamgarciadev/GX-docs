---
title: "On session timeout property"
source_id: 17458
source_url: https://wiki.genexus.com/commwiki/wiki?17458
genexus_version: "18"
---

# On session timeout property

Specifies if the user has to receive an alert when an action that is solved using AJAX is triggered, and the web session has expired.

### [Values](#Values)

|  |  |
| --- | --- |
| **Ignore** | If integrated security is not enabled, actions that are solved using AJAX are executed even if the web session has expired. If integrated security is enabled and an action that is solved using AJAX is executed, the user will be redirected to the login page. This is the default value |
| **Warn** | When the web session expires or if it is invalid, a warning message will be displayed suggesting the user to refresh the page to get a new WebSession |

### [Scope](#Scope)

**Objects:** Transaction, Web Panel

### [Description](#Description)

This helps to alert users that a redirect will be done so they can avoid losing the changes they have made on the page (by pressing the cancel button).

`[imagen omitida: wiki id 32619]`

The security level of both values is the same.

#### [Notes:](#Notes%3A)

1. In a load balancing environment, it's necessary to have Server Affinity or any way to persist the web session among the servers; otherwise, the results will be unpredictable.

2. When [GAM](https://wiki.genexus.com/commwiki/wiki?14960) is activated in the [KB](https://wiki.genexus.com/commwiki/wiki?2428), if the "On session timeout" property is set to WARN and GAM session timeout expires, the session expiration warning message will also be displayed, even though that session timeout does not expire on the server.

This helps to alert the user that a redirect will be done (to the GAM login object); in this case, he will lose his work unless he cancels in the session timeout alert box and saves his work before the redirect takes place.

#### [**Note**](#Note)

The behavior described in this document is valid for [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Smooth, since GeneXus X Evolution 3 upgrade 9.

For [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Previous versions compatible or GeneXus X Evolution 3 upgrade 8 or previous, the behavior is as described in [On Session Timeout property](https://wiki.genexus.com/commwiki/wiki?32616,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Compatibility](#Compatibility)

For Smooth models (since GeneXus X Evolution 3 upgrade 9), the On Session Timeout property is independent of the parameter encryption mechanism of the AJAX calls.


|  |
| --- |
| **Backlinks** |
| [A07:2021 - Identification and authentication failures](https://wiki.genexus.com/commwiki/wiki?50187) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |

---
