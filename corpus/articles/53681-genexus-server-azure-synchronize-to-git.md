---
title: "GeneXus Server Azure - Synchronize to Git"
source_id: 53681
source_url: https://wiki.genexus.com/commwiki/wiki?53681
genexus_version: "18"
---

# GeneXus Server Azure - Synchronize to Git

If you wish to track changes across your generated objects or [Sources](https://wiki.genexus.com/commwiki/wiki?53679), you can add the following job definitions to synchronize them to a Git server.

In order to clone a repository and pull changes:

```
  - job: CloneOrPull
    steps:
      - script: |
          IF EXIST "$(GIT_BRANCH)" (
            cd $(GIT_BRANCH)
            git checkout $(GIT_BRANCH)
            git pull
          ) ELSE (
            git clone https://$(GIT_USER):$(GIT_PASSWORD)@$(GIT_REPO) $(WORKING_DIR)\$(GIT_BRANCH)
          )
        workingDirectory: $(WORKING_DIR)
        name: CloneOrPull
```

To push your changes to remote:

```
  - job: PushToGit
    dependsOn: CloneOrPull
    steps:
      - script: >
          cd $(GIT_BRANCH)

          git checkout $(GIT_BRANCH)

          xcopy /E /I /Y "$(COMMIT_FOLDER)" "$(WORKING_DIR)\$(GIT_BRANCH)\$(DEPLOYMENT_UNIT)"

          git add *
        
          git commit -m "Commit build $(Build.BuildNumber)"

          git push -u origin $(GIT_BRANCH)
        workingDirectory: $(WORKING_DIR)
        name: CommitPush
```

### [Variables](#Variables)

The following are specific variable definitions required for the task. See [GeneXus Server Azure Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52099,,) for the generic variables required.

GIT\_USER: *string*  
Username of a Git account with permissions over the existing repository.

GIT\_PASSWORD: *string*  
Password or Private Access Token associated with the Git Username. PAT is recommended; add parameter as [Secret Variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops&tabs=yaml%2Cbash). Using PAT requires full repository access permissions when generated.

GIT\_REPO: *string*   
HTTPS connection repository URL. Said repository has to be previously initialized. We will be storing the tracked files here.  
Example: “dev.azure.com/GeneXusDesa/GeneXusBuild/\_git/GeneXusBuild”

GIT\_BRANCH: *string*  
Name of the branch for versioning. It has to be previously created.  
Example: “main”


|  |
| --- |
| **Backlinks** |
| [GeneXus Server Azure - Generate Sources (.NET)](https://wiki.genexus.com/commwiki/wiki?53679) |

---
