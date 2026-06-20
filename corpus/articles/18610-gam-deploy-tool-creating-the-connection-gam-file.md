---
title: "GAM Deploy Tool: Creating the connection.gam file"
source_id: 18610
source_url: https://wiki.genexus.com/commwiki/wiki?18610
genexus_version: "18"
---

# GAM Deploy Tool: Creating the connection.gam file

One purpose of the [GAM Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) is to create the connection.gam file (needed to connect to the GAM Repositories).

Each [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) may have n [GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150), which are defined for each Repository in the GAM database.

The [connection.gam](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,E,0,,30451) file includes the key associated with each Repository you want to connect to. The connection information associated with the key has to exist in the GAM database (it should have been previously created using the GAM API).

So, by using GAMDeployTool, the entries in the SysConnectionConfig table (in the GAM database) are added depending on the selection of the user (who can select among the existing [GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) of each Repository).

The tool is for use of administrators of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) (for example: gamadmin user).

### [How to execute GAMDeployTool in standalone mode:](#How+to+execute+GAMDeployTool+in+standalone+mode%3A)

1. Execute GamDeployTool.exe.  
  
2. Select the operation you want to perform; in this case, "Generate Connection File".

`[imagen omitida: wiki id 18612]`

###### [Figure 1.](#Figure+1.)

3. Enter the necessary data to connect to the GAM database.

By now, the tool uses ADO to connect to the database, so you need the corresponding ADO client of the DBMS you want to connect to.

`[imagen omitida: wiki id 18613]`

###### [Figure 2.](#Figure+2.)

4. Enter your administrator credentials (administrators of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617)).

The only users who are allowed to execute this tool are the administrators of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) (for example, "gamadmin" user). If you try to connect with another user, an error will be thrown: "GAM: Unknown user".

`[imagen omitida: wiki id 18614]`

###### [Figure 3.](#Figure+3.)

5. In the following window, you will view all the Repositories found in the GAM database, and the available connections for each of them.

In this step, you are asked to select the path where connection.gam will be generated and the connections that will be included in the GAM database.  
You are shown a tree structure with parents and their children, where each parent is the Repository, and its children are all the available [GAM Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) of the Repository (existing in the database).  
The user can select the "GAM Repository Connections" that are going to be included in the SysConnectionConfig table in the GAM database.

`[imagen omitida: wiki id 18615]`

###### [Figure 4.](#Figure+4.)

6. Final Step: the file is generated in the specified location.

`[imagen omitida: wiki id 18616]`

###### [Figure 5.](#Figure+5.)

Finally, the connection.gam obtained has to be copied to the web application. For NET applications, copy it to the virtual directory; for JAVA, copy it to the root of the webapp in the servlets server.

Note: This tool can be launched from the GeneXus IDE, by selecting [GAM - Update Connection File](https://wiki.genexus.com/commwiki/wiki?18690) option.


|  |
| --- |
| **Backlinks** |
| [GAM - Deploy Tool](https://wiki.genexus.com/commwiki/wiki?18608) | [GAM - Update Connection File](https://wiki.genexus.com/commwiki/wiki?18690) | [GAM Deploy Tool: Export Data](https://wiki.genexus.com/commwiki/wiki?18872) |
| [GAM Deploy Tool: Import Data](https://wiki.genexus.com/commwiki/wiki?21974) | [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) | [HowTo: Connect to GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18625) |
| [HowTo: Update a repository from a GAM deploy tool package](https://wiki.genexus.com/commwiki/wiki?20929) |

---
