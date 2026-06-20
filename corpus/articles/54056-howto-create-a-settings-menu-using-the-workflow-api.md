---
title: "HowTo: Create a settings menu using the Workflow API"
source_id: 54056
source_url: https://wiki.genexus.com/commwiki/wiki?54056
genexus_version: "18"
---

# HowTo: Create a settings menu using the Workflow API

This article describes how to create a settings menu using the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

You can access the preferences with a [Workflow Server](https://wiki.genexus.com/commwiki/wiki?11671) object and its GetSettingById() method. In addition, you can find the Id of each preference in the following [documentation](https://wiki.genexus.com/commwiki/wiki?15098). Once you have gotten the preference, you can modify it with its value property or assign it to a [Workfow Setting](https://wiki.genexus.com/commwiki/wiki?15084) object.

Below is an example of how to create a password policy menu in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916):

```
Event Start
    &WorkflowServer.Connect('WFADMINISTRATOR','WFADMINISTRATOR')
    Do 'Load'
Endevent

Sub 'Load'
    &MaximumPasswordRetries = &WorkflowServer.GetSettingById(1419).Value
    &PasswordDuration = &WorkflowServer.GetSettingById(1420).Value
    &EnablePwdExpiration = &WorkflowServer.GetSettingById(1421).Value
    &UseOfBothUpperAndLowercaseLetters = &WorkflowServer.GetSettingById(1422).Value
    &IncludeOneOrNoreNumericalDigits = &WorkflowServer.GetSettingById(1423).Value
    &IncludeSpecialCharacters =    &WorkflowServer.GetSettingById(1424).Value
    &MinimumPasswordLength = &WorkflowServer.GetSettingById(1425).Value
    &PasswordPolicyRules =    &WorkflowServer.GetSettingById(1426).Value
    &PasswordPolicyCustomProgram = &WorkflowServer.GetSettingById(1427).Value
    &CannotRepeatPasswords = &WorkflowServer.GetSettingById(1428).Value
Endsub

Event 'Save'
    if &MaximumPasswordRetries <> &WorkflowServer.GetSettingById(1419).Value
        &WorkflowServer.GetSettingById(1419).Value=&MaximumPasswordRetries
    endif
    if &PasswordDuration <> &WorkflowServer.GetSettingById(1420).Value
        &WorkflowServer.GetSettingById(1420).Value=&PasswordDuration
    endif
    if &EnablePwdExpiration <> &WorkflowServer.GetSettingById(1421).Value
        &WorkflowServer.GetSettingById(1421).Value=&EnablePwdExpiration
    endif
    if &UseOfBothUpperAndLowercaseLetters <> &WorkflowServer.GetSettingById(1422).Value
        &WorkflowServer.GetSettingById(1422).Value=&UseOfBothUpperAndLowercaseLetters
    endif
    if &IncludeOneOrNoreNumericalDigits <> &WorkflowServer.GetSettingById(1423).Value
        &WorkflowServer.GetSettingById(1423).Value=&IncludeOneOrNoreNumericalDigits
    endif
    if &IncludeSpecialCharacters <>    &WorkflowServer.GetSettingById(1424).Value
        &WorkflowServer.GetSettingById(1424).Value=&IncludeSpecialCharacters
    endif
    if &MinimumPasswordLength <> &WorkflowServer.GetSettingById(1425).Value
        &WorkflowServer.GetSettingById(1425).Value=&MinimumPasswordLength
    endif
    if &PasswordPolicyRules <> &WorkflowServer.GetSettingById(1426).Value
        &WorkflowServer.GetSettingById(1426).Value=&PasswordPolicyRules
    endif
    if &PasswordPolicyCustomProgram <> &WorkflowServer.GetSettingById(1427).Value
        &WorkflowServer.GetSettingById(1427).Value=&PasswordPolicyCustomProgram
    endif
    if &CannotRepeatPasswords <> &WorkflowServer.GetSettingById(1428).Value
        &WorkflowServer.GetSettingById(1428).Value=&CannotRepeatPasswords
    endif
    commit
    Do 'Load'
Endevent
```

Where the data types variables are as follows:

```
&WorkflowServer – WorkflowServer
&MaximumPasswordRetries – Characacter (20)
&PasswordDuration – Characacter (20)
&EnablePwdExpiration – Characacter (20)
&UseOfBothUpperAndLowercaseLetters – Characacter (20)
&IncludeOneOrNoreNumericalDigits – Characacter (20)
&IncludeSpecialCharacters – Characacter (20)
&MinimumPasswordLength – Characacter (20)
&PasswordPolicyRules – Characacter (20)
&PasswordPolicyCustomProgram – Characacter (20)
&CannotRepeatPasswords – Characacter (20)
```

Note that most preferences have a predefined set of possible values which can be assigned. Check these values in the following [documentation](https://wiki.genexus.com/commwiki/wiki?15098).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Workflow Settings Id and Values](https://wiki.genexus.com/commwiki/wiki?15098) |

---
