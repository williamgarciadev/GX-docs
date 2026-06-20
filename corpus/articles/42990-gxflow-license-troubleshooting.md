---
title: "GXflow license troubleshooting"
source_id: 42990
source_url: https://wiki.genexus.com/commwiki/wiki?42990
genexus_version: "18"
---

# GXflow license troubleshooting

### [Exception message: An internal error occurred 0x8001FFFF](#Exception+message%3A+An+internal+error+occurred+0x8001FFFF)

Trying to connect GXflow to a Protection server the following error occurs:

```
GX Protection (DATE TIME): Error: Unexpected error
GX Protection (DATE TIME): Exception message: An internal error occurred. [0x8001FFFF]
com.gxflow.protection.F: An internal error occurred. [0x8001FFFF]
 at com.gxflow.protection.A.B.E.C(Unknown Source)
 at com.gxflow.protection.Protection.isNominatedUser(Unknown Source)
 at com.gxflow.SdtWFProtection.isnominateduser(SdtWFProtection.java:109)
 at com.gxflow.pwfin.privateExecute(pwfin.java:127)
 at com.gxflow.pwfin.executeUdp(pwfin.java:80)
 at com.gxflow.pwfgsh.privateExecute(pwfgsh.java:108)
 at com.gxflow.pwfgsh.execute_int(pwfgsh.java:101)
 at com.gxflow.pwfgsh.execute(pwfgsh.java:88)
 at com.gxflow.pwfintconnect.S111(pwfintconnect.java:451)
 at com.gxflow.pwfintconnect.privateExecute(pwfintconnect.java:364)
 at com.gxflow.pwfintconnect.execute_int(pwfintconnect.java:116)
 at com.gxflow.pwfintconnect.execute(pwfintconnect.java:97)
 at com.gxflow.pwfdtserconnect.privateExecute(pwfdtserconnect.java:127)
 at com.gxflow.pwfdtserconnect.execute_int(pwfdtserconnect.java:108)
 at com.gxflow.pwfdtserconnect.execute(pwfdtserconnect.java:92)
 at com.gxflow.api.GXInterop.ServerConnect(Unknown Source)
 at com.gxflow.api.Server.Connect(Unknown Source)
 at com.oasystem.SdtWorkflowServer.connect(SdtWorkflowServer.java:58)
 ...
Caused by: org.jinterop.dcom.common.JIException: An internal error occurred. [0x8001FFFF]
 at org.jinterop.dcom.core.JIComServer.getInterface(JIComServer.java:701)
 at org.jinterop.dcom.core.JIComObjectImpl.queryInterface(JIComObjectImpl.java:89)
```

Disable the DCOM NTLMv2 version.

* Edit the registry with *regedit* utility.
* Go to the key *HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Control\Lsa*
* Change the DWORD [LMCompatibilityLevel](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level) from 1 to 2 (NTLM)
* Restart the server and check again.

### [Error 0x00000005 when checking GXflow licenses](#Error+0x00000005+when+checking+GXflow+licenses)

The following error occurs when checking GXflow licenses

```
GX Protection (DATE TIME): Error: Unexpected error
could not connect to remote protection server, tried to establish connection with the following data: 
    Server host: localhost
    Server port: 15531
    User domain: MACHINENAME
    User id: test
com.gxflow.protection.F: could not connect to remote protection server, tried to establish connection with the following data: 
    Server host: localhost
    Server port: 15531
    User domain: MACHINENAME
    User id: test
    at com.gxflow.protection.A.B.E.<init>(Unknown Source)
    at com.gxflow.protection.Protection.A(Unknown Source)
    at com.gxflow.protection.Protection.getLicenses(Unknown Source)
    at com.gxflow.SdtWFProtection.getlicenses(SdtWFProtection.java:86)
    at com.gxflow.pwfislicenseproductauthorized.privateExecute(pwfislicenseproductauthorized.java:102)
    at com.gxflow.pwfislicenseproductauthorized.executeUdp(pwfislicenseproductauthorized.java:78)
    at com.gxflow.pwfgetmenu.privateExecute(pwfgetmenu.java:340)
    at com.gxflow.pwfgetmenu.execute_int(pwfgetmenu.java:92)
    at com.gxflow.pwfgetmenu.execute(pwfgetmenu.java:83)
    ...
Caused by: org.jinterop.dcom.common.JIException: Access is denied, please check whether the [domain-username-password] are correct. Also, if not already done please check the GETTING STARTED and FAQ sections in readme.htm. They provide information on how to correctly configure the Windows machine for DCOM access, so as to avoid such exceptions.  [0x00000005]
    at org.jinterop.dcom.core.JIComServer.init(JIComServer.java:572)
    at org.jinterop.dcom.core.JIComServer.initialise(JIComServer.java:481)
    at org.jinterop.dcom.core.JIComServer.<init>(JIComServer.java:445)
    ... 52 more
Caused by: rpc.FaultException: Received fault. (unknown)
    at rpc.ConnectionOrientedEndpoint.call(ConnectionOrientedEndpoint.java:141)
    at rpc.Stub.call(Stub.java:113)
    at org.jinterop.dcom.core.JIComServer.init(JIComServer.java:568)
    ... 54 more
```

Review the credentials (user, password and domain name) connecting to the GeneXus Protection Server, the 0x00000005 is "Access Denied".

Check the following links.

[Setting user permissions using remote licenses](https://wiki.genexus.com/commwiki/wiki?19985)  
[Enabling centralized licenses scheme](https://wiki.genexus.com/commwiki/wiki?26132,,)

You can use the following Microsoft Tool [DCom client server test app](https://support.microsoft.com/en-us/help/259011/sample-a-simple-dcom-client-server-test-application) for checking that the DCOM infrastructure is working.

### [Native SSPI library not loaded](#Native+SSPI+library+not+loaded)

The following error occurs when GXflow licenses credentials are not correctly set:

```
GX Protection (DATE TIME): Error: Unexpected error
could not connect to remote protection server, tried to establish connection with the following data: 
    Server host: localhost
    Server port: 15531
    User domain: 
    User id: 
com.gxflow.protection.F: could not connect to remote protection server, tried to establish connection with the following data: 
    Server host: localhost
    Server port: 15531
    User domain: 
    User id:
    at com.gxflow.protection.A.B.E.<init>(Unknown Source)
    at com.gxflow.protection.Protection.A(Unknown Source)
    at com.gxflow.protection.Protection.getLicenses(Unknown Source)
    at com.gxflow.SdtWFProtection.getlicenses(SdtWFProtection.java:86)
    at com.gxflow.pwfislicenseproductauthorized.privateExecute(pwfislicenseproductauthorized.java:102)
    at com.gxflow.pwfislicenseproductauthorized.executeUdp(pwfislicenseproductauthorized.java:78)
    at com.gxflow.pwfislicenseauthorized.privateExecute(pwfislicenseauthorized.java:97)
    at com.gxflow.pwfislicenseauthorized.executeUdp(pwfislicenseauthorized.java:77)
    ...
Caused by: java.lang.IllegalStateException: Native SSPI library not loaded. Check the java.library.path system property.This functionality is available only under "Microsoft Windows" line of Operating systems.
    at net.sourceforge.jtds.util.SSPIJNIClient.<init>(SSPIJNIClient.java:84)
    at net.sourceforge.jtds.util.SSPIJNIClient.getInstance(SSPIJNIClient.java:104)
    at rpc.security.ntlm.NtlmAuthentication.<init>(NtlmAuthentication.java:119)
    at rpc.security.ntlm.NtlmConnection.<init>(NtlmConnection.java:44)
    at rpc.security.ntlm.NtlmConnectionContext.init2(NtlmConnectionContext.java:76)
    at rpc.security.ntlm.NtlmConnectionContext.init(NtlmConnectionContext.java:84)
    at rpc.ConnectionOrientedEndpoint.connect(ConnectionOrientedEndpoint.java:244)
    at rpc.ConnectionOrientedEndpoint.bind(ConnectionOrientedEndpoint.java:216)
    at rpc.ConnectionOrientedEndpoint.rebind(ConnectionOrientedEndpoint.java:152)
    at org.jinterop.dcom.transport.JIComEndpoint.rebindEndPoint(JIComEndpoint.java:40)
    at org.jinterop.dcom.core.JIComServer.init(JIComServer.java:559)
    at org.jinterop.dcom.core.JIComServer.initialise(JIComServer.java:481)
    at org.jinterop.dcom.core.JIComServer.<init>(JIComServer.java:445)
    ... 47 more
```

Review the credentials to connect to the GeneXus Protection Server, it seems User and Password are empty.

### [License will expire in X days. Please contact the system administrator](#License+will+expire+in+X+days.+Please+contact+the+system+administrator)

The message could also be "There was a problem with the License. Please contact the system administrator."

As of [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,), this warning appears when logging in to GXflow when there is a problem in the license.

It is just a warning, the access to the GXflow inbox won't be blocked.  
However, the problem must be solved in less than 15 days or before the application server restarts. For this, you (\*) must access to license manager (\*\*)and request new licenses, change restrictions or use your contingency license.   
(\*) [Who can handle licenses](https://wiki.genexus.com/commwiki/wiki?37204)  
(\*\*) [HowTo: Work with GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207)

### [See Also](#See+Also)

* [GXflow license scheme](https://wiki.genexus.com/commwiki/wiki?37204)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
