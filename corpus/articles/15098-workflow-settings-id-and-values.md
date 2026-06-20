---
title: "Workflow Settings Id and Values"
source_id: 15098
source_url: https://wiki.genexus.com/commwiki/wiki?15098
genexus_version: "18"
---

# Workflow Settings Id and Values

This article lists the Id and values ​​of the preferences of [Workflow Settings](https://wiki.genexus.com/commwiki/wiki?15097) in the database. This information is necessary to work with preferences from the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350). Read more in [HowTo: Create a settings menu using the Workflow API](https://wiki.genexus.com/commwiki/wiki?54056).

#### [Application Preferences](#Application+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Show applications in a new window | 1399 | 0, 1 | No, Yes |
| Autoresize application windows | 1400 | 0, 1 | No, Yes |
| Window height | 1401 |  |  |
| Window width | 1402 |  |  |
| Encrypt URL Parameters | 1410 | 0, 1, 2 | No, Session key, Site Key |
| Enable Dynamic Forms | 1500 | 0, 1 | No, Yes |
| Dynamic Forms Provider | 1502 | EXTERNAL, GXFLOW | External, GXflow |

#### [Language Preference](#Language+Preference)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Default Language | 1220 | ara, chs, cht, eng, ger, ita, jap, por, spa | Arabic, Simplified Chinese, Traditional Chinese, English, German, Italian, Japanese, Portuguese, Spanish |

#### [Notification Preferences](#Notification+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Server | 1010 |  |  |
| Port | 1011 |  |  |
| Email | 1020 |  |  |
| Name | 1030 |  |  |
| Authentication Required | 1040 | 0, 1 | No, Yes |
| User | 1050 |  |  |
| Password | 1060 |  |  |
| Secure | 1062 | 0, 1 | No, Yes |

#### [Authentication Preferences](#Authentication+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Authentication Schema | 1070 | EXTERNAL, GAM, GXFLOW, WINDOWS | External, GAM, GXflow, Windows |
| External login page | 1082 |  |  |
| Authentication Program | 1083 |  |  |
| Disable Email Uniqueness control | 1085 | 0, 1 | No, Yes |
| GAM Authentification Type | 1086 |  |  |

#### [Session Management Preferences](#Session+Management+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Session Timeout | 1180 | 3600, 7200, 28800, 86400 | 1 hour, 2 hours, 8 hours, 24 hours |
| Reconnect automatically when expiring | 1181 | 0, 1 | No, Yes |

#### [Password Policy Preferences](#Password+Policy+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **V****alue Description** |
| Enable Expiration | 1421 | 0, 1 | No, Yes |
| Maximum password retries before block user account | 1419 | 3, 5, 10 | 3, 5, 10 |
| Duration (Days) | 1420 |  |  |
| Rules | 1426 | CUSTOM, GXFLOW | Custom, GXflow |
| Custom Rules Program | 1427 |  |  |
| Number of months that must pass in order to repeat passwords | 1428 | 3, 6, 12, 18, 24 | 3, 6, 12, 18, 24 |
| Minimum Length | 1425 | 0, 5, 6, 7, 8, 9, 10 | 0, 5, 6, 7, 8, 9, 10 |
| Use upper and lower case letters | 1422 | 0, 1 | No, Yes |
| Include numerical digits | 1423 | 0, 1 | No, Yes |
| Include special characters | 1424 | 0, 1 | No, Yes |

#### [Event Handling Preferences](#Event+Handling+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Enable | 1300 | 0, 1 | No, Yes |
| New Instance | 1301 | 0, 1 | No, Yes |
| State Change | 1302 | 0, 1 | No, Yes |
| Priority Change | 1303 | 0, 1 | No, Yes |
| Assignment Change | 1304 | 0, 1 | No, Yes |
| Data Change | 1305 | 0, 1 | No, Yes |
| Warning | 1306 | 0, 1 | No, Yes |
| Deadline | 1307 | 0, 1 | No, Yes |
| Error | 1308 | 0, 1 | No, Yes |
| Condition Nonsatisfied | 1309 | 0, 1 | No, Yes |
| Resource Nonavailable | 1310 | 0, 1 | No, Yes |
| External | 1311 | 0, 1 | No, Yes |
| Action Performed | 1312 | 0, 1 | No, Yes |

#### [Document Management Preferences](#Document+Management+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Enable | 1340 | 0, 1 | No, Yes |
| Upload Path | 1350 |  |  |
| Enable Full Text Search | 1351 | 0, 1 | No, Yes |
| Index Directory | 1352 |  |  |
| Enable Digital Signature | 1353 | 0, 1 | No, Yes |
| Certificates Directory | 1354 |  |  |
| Automatic User Certificate Insertion | 1355 | 0, 1 | No, Yes |
| Enable Cloud Storage | 1341 | 0, 1 | No, Yes |
| Storage Provider | 1342 | (none), AMAZONS3, AZURESTORAGE | None, Amazon, Azure |
| Storage Access Key | 1343 |  |  |
| Secret Access Key | 1344 |  |  |
| Public Bucket Name | 1345 |  |  |
| Storage Region | 1346 |  |  |
| Private Bucket Name | 1347 |  |  |
| Account Name | 1348 |  |  |

#### [Performance Preferences](#Performance+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Rebuild Worklist When Org. Struct. Changes | 1360 | 0, 1 | No, Yes |
| Enable Deferred Task Completion | 1370 | 0, 1 | No, Yes |
| Pre-calculate Process Participants | 1380 | 0, 1 | No, Yes |
| Fetch | 1130 | 10, 20, 50, 100, 200, 500 | 10, 20, 50, 100, 200, 500 |
| Max Fetch | 1140 | 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000 | 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000 |
| Maximum number of elements in a SQL list | 1141 | 1000, 10000, 100000 | 1000, 10000, 100000 |
| Enable Organizational Model Cache | 1201 | 0, 1 | No, Yes |
| Organizational Model Cache Timeout | 1202 |  |  |

#### [Compatibility Preferences](#Compatibility+Preferences)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Null Organizational Unit Assignment Behavior | 1390 | 9, 10 | Version 9 and prior, Current Version |
| Disable process selection in Start New Process dialog | 1391 | 0, 1 | No, Yes |

#### [Business Process Deployment](#Business+Process+Deployment)

|  |  |  |  |
| --- | --- | --- | --- |
| **Preference Description** | **Id** | **Preference Values** | **Value Description** |
| Override Task-Role Assignments | 1450 | 0, 1 | No, Yes |


|  |
| --- |
| **Backlinks** |
| [HowTo: Create a settings menu using the Workflow API](https://wiki.genexus.com/commwiki/wiki?54056) |

---
