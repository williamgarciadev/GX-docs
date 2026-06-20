---
title: "GeneXus Server Azure - Dacpac Generation"
source_id: 53684
source_url: https://wiki.genexus.com/commwiki/wiki?53684
genexus_version: "18"
---

# GeneXus Server Azure - Dacpac Generation

For certain DevOps scenarios, it might be desirable to generate a snapshot of your current Database Schema. For GeneXus development, this can be done on a mock Database to validate the pipeline execution, before reorganizing production environments.

With SQL Server, this can be achieved by using [Data-Tier Application Packages](https://learn.microsoft.com/en-us/sql/relational-databases/data-tier-applications/data-tier-applications?view=sql-server-ver16), which are self-contained and complete Database model snapshots.

Dacpacs require Microsoft SqlPackage, which you can install through PowerShell with the following command:

```
dotnet tool install -g microsoft.sqlpackage
```

To generate your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) dacpac and export it as a pipeline run artifact, add the following job to your pipeline definition:

```
  - job: GenerateDacpac
    steps:
      - powershell: >
          sqlpackage /TargetFile:".\$(kbalias).dacpac" /Action:Extract 
          /scs:"Server=$(SQL_SERVER);Initial Catalog=$(kbalias);Trusted_Connection=True;TrustServerCertificate=True;"
        workingDirectory: $(WORKING_DIR)
        name: GeneratingDacpac
        
      - publish: $(WORKING_DIR)/$(kbalias).dacpac
        artifact: $(kbalias).dacpac
        name: 'PublishArtifact'
```

It is recommended that you set up your pipeline dependency to the Build step.  
That can be accomplished by adding the following snippet to your job:

```
    dependsOn: BuildKnowledgeBase
    condition: succeeded()
```

### [Variables](#Variables)

The following are specific variable definitions required for the task:

SQL\_SERVER: *string*   
SQL Server instance name. Example: "GXP5022\SQLEXPRESS"

See [GeneXus Server Azure Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52099,,) for the generic variables required.
