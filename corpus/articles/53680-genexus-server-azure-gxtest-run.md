---
title: "GeneXus Server Azure - GXtest Run"
source_id: 53680
source_url: https://wiki.genexus.com/commwiki/wiki?53680
genexus_version: "18"
---

# GeneXus Server Azure - GXtest Run

You can add [GXtest](https://wiki.genexus.com/commwiki/wiki?38327) to your DevOps process in order to validate incremental correctness by running tests automatically in your pipeline.

If there are any failures in your test suite, the pipeline run will fail accordingly. In addition, test results can be published in multiple output formats as a pipeline run artifact.

To add a test run to your execution, add the following job to your pipeline definition (see [GXtest MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?40738) for more details):

```
  - job: RunTestSuite
    steps:
      - script: >
          $(MSBUILD) "$(BL_PATH)\AzureCICD.msbuild" -target:RunTestSuite /p:WorkingDirectory=$(KB_PATH) 
          /p:TestType=$(TEST_TYPE) /p:testObjectsList=$(TEST_LIST) /p:ServerKbAlias=$(KB_ALIAS)
          /p:ServerUsername=$(GXSERVER_USER) /p:ServerPassword=$(GXSERVER_PASS) /p:TestFilePath="$(WORKING_DIR)\JUnitTestResult.xml"
        name: RunTests
      
      - publish: "$(WORKING_DIR)/JUnitTestResult.xml"
        artifact: "JUnitTestResult.xml"
        name: 'PublishArtifact'
```

It is recommended that you set up your pipeline dependency to the Build step. Additionally, you may add an unconditional job trigger.  
That can be accomplished by adding the following snippet to your job:

```
    dependsOn: BuildKnowledgeBase
    condition: or(succeeded(), eq(${{parameters.forceTests}}, True))
```

Parameter definition can be added as a root tag anywhere in your pipeline, as follows:

```
parameters:
- name: forceTest
  displayName: Force Test Execution
  type: boolean
  default: false
  values:
  - true
  - false
```

### [Variables](#Variables)

The following are specific variable definitions required for the task. See [GeneXus Server Azure Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52099,,) for the generic variables required.

TEST\_TYPE: *{All, Unit, Web, UI, SD}*  
Specifies the type of test to run. Set:  
All: to run all enabled Unit tests first, then enabled web UI tests, and at last, all enabled SD UI tests. **Default value.**  
Unit: to run all enabled Unit tests.  
Web: to run all enabled web UI tests.  
SD: to run all enabled SD tests.  
UI: to run all enabled web and SD UI tests.

TEST\_LIST: *string*   
List of test object names separated by semicolons(;): Unit tests, UI tests, and Test Suites  
Specifies the tests to build before the execution.
