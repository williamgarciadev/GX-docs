---
title: "Protect.dll Error Codes and Descriptions"
source_id: 15246
source_url: https://wiki.genexus.com/commwiki/wiki?15246
genexus_version: "18"
---

# Protect.dll Error Codes and Descriptions

Error codes when "Suspended authorization data changed" error is given by Protect.dll

|  |  |  |  |
| --- | --- | --- | --- |
| **Code** | **Internal constant** | **Description** | **Posible Cause or Comment** |
| 0 | ADS\_UNINITIALIZED | Protect License Information not yet loaded |  |
| 1 | ADS\_OK | Correctly lodaded & consistent | Normal execution |
| 2 | ADS\_ERROR\_GETTING\_PROD\_LIC | Unknown data format (registry) | Saved with a newer version of Protect.dll than the one it is now installed |
| 3 | ADS\_ERROR\_CHECKING\_PROD\_LIC\_1 | MachineID in data doesn't match real one | Mismatch in registry information about MachineID  The user may not have permission on the registry to store the Site Code. Make sure to execute as an administrator |
| 4 | ADS\_ERROR\_CHECKING\_PROD\_LIC\_2 | ProductID or VersionID doesn't match | Mismatch in registry information about ProductID\VersionID |
| 5 | ADS\_ERROR\_OPENING\_GEN\_INFO | Error loading common data to all licenses | Generate a log file for more information |
| 6 | ADS\_WRONG\_MACHINE\_ID | MachineID in common data doesn't match real one | Generate a log file for more information |
| 7 | ADS\_GET\_PROTFILE\_FULL\_PATH | ProtFile can't be found |  |
| 8 | ADS\_ERROR\_ACCESS\_PROTFILE\_1 | Error opening ProtFile |  |
| 9 | ADS\_ERROR\_ACCESS\_PROTFILE\_2 | Error locating data in ProtFile |  |
| 10 | ADS\_ERROR\_ACCESS\_PROTFILE\_3 | Error reading data in ProtFile |  |
| 11 | ADS\_ERROR\_CHECK\_PROTFILE\_1 | MachineID reference doesn't match the real one | Mismatch in MachineID information |
| 12 | ADS\_ERROR\_CHECK\_PROTFILE\_2 | Value not used | (deprecated) |
| 13 | ADS\_ERROR\_UNKNOWN | When there is an error saving ProtFile, or MachineID  in common data doesn't match the one in license data | In this case, all licenses are suspended |
| 14 | ADS\_ERROR\_GETTING\_PROD\_USER\_LIC | Unknown data format (user registry) | Saved with a newer version of Protect.dll than the one it is now installed\* |
| 15 | ADS\_ERROR\_CHECKING\_PROD\_USER\_LIC | ProductID or VersionID doesn't match | Mismatch in user registry information about MachineID |
| 16 | ADS\_ERROR\_VERIFING\_RESTRICTIONS | Trial license with more than 60 days detected | (deprecated - License type not used) |
| 17 | ADS\_ERROR\_ABOVE\_MAX\_COPIES | Number of copies is higher than expected | Inconsistent number of copies |
| 18 | ADS\_ERROR\_GETTING\_LICENSES | Error loading licenses list | Generate a log file for further information; the first letter (in the log file) means the location of error:  a = can't find licenses  b = reading from registry  c = invalid format  d = decrypting  e = comparing restrictions  f = comparing product |
| 19 | ADS\_ERROR\_CHECK\_LIC\_INFO | Seed in common data doesn't match the expected one | There is an inconsistency in the license. |
| 20 | ADS\_ERROR\_GETLIC\_QUERY\_1 | License Keys not found |  |
| 21 | ADS\_ERROR\_GETLIC\_QUERY\_2 | Error reading license keys |  |
| 22 | ADS\_ERROR\_GETLIC\_QUERY\_3 | Invalid license key saved format |  |
| 23 | ADS\_ERROR\_GETLIC\_DECRYPT | Error checking license key |  |
| 24 | ADS\_ERROR\_GETLIC\_RESTRICTIONS | Incompatible license key restrictions |  |
| 25 | ADS\_ERROR\_FUTURE\_FORMAT | Unable to read new data format (registry) |  |
| 26 | ADS\_ERROR\_GETLIC\_INCORRECT\_PRODUCT | License key has the incorrect product |  |
| 27 | ADS\_ERROR\_GETTING\_PROD\_LIC\_SINGLE | Unknown data format (registry) |  |
| 28 | ADS\_ERROR\_FUTURE\_FORMAT\_SINGLE | Unable to read new data format (registry) |  |
| 29 | ADS\_ERROR\_CHECK\_LIC\_INFO\_SINGLE | Seed in common data doesn't match the expected one |  |
| 30 | ADS\_ERROR\_FUTURE\_FORMAT\_GENERAL | Unable to read new data format (registry) |  |
| 31 | ADS\_ERROR\_CHECK\_LIC\_CHANGED | Unauthorized change detected in license keys |  |
| 32 | ADS\_ERROR\_FUTURE\_FORMAT\_RECOVER | Unable to read new data format status was incorrectly saved (registry) |  |

ADS - Authorization Data Status
