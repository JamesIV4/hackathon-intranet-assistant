## Description

Each Speech Project will use the estimation statistic of "Original Estimate" which is estimated time vs. time recorded. To understand this configuration please review the following link from Atlassian's Documentation Page, [Confgurating, Estimation, and Tracking](https://confluence.atlassian.com/display/AGILE/Configuring+Estimation+and+Tracking).

**Note: Enter Time Estimate PRIOR to starting progress on ANY issue, Epic, New Feature, Task, or Bug.**

The estimate field is only available while the issue is in the plan mode. Once it has been moved into work mode, i.e. placed into a Sprint it will no longer have the ability to modify the estimated time via the method described below.

_Caveat:  If it is forgotten it can be added by editing the SCR and updating the "Orginal Estimate" field but this should NOT be done if at all possible to ensure proper tracking of time._

* * *

### New Feature

#### Recording the Estimated Time

* * *

Hovering over the word Unestimated will cause a little pencil/pen icon to appear to the right. The unit of time here is story points so I entered to 2 for the sake of these instructions.

* * *

* * *

 

#### Recording Work Logged

* * *

Once Work is logged against this issue then the Remaining time will reduce.

##### Method 1: Logging Work on Individual Issues

  1. Open the JIRA Issue.
  2. Click the Ellipses Button in the Sidebar View or via the More menu option.  
  

  3. Click Log Work  
  




##### Method 2: JIRA Filter and Keyboard

  1. Use the following filter for your issues in the following statuses, In Progress, Investigation, and Integration Testing.
     1. trueInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27status in (Open, "In Progress", Investigation, "Integration Testing") AND assignee in (currentUser()) ORDER BY status DESC 
  2. Use the arrow keys or the 'j' key navigate the issues list.
  3. Use the period key to open the actions menu of the selected item.
  4. Press the 'L' key to initial the Log Work Dialog



##### Log Work Dialog

  1. Enter time spent
  2. Date Started
     1. If you can / need to block out the time exactly you can do so here.
     2. You can also log work in the past.
  3. Remaining Estimate - Leave Default of "Adjust Automatically"
  4. Enter a Work Description if necessary.



 

* * *

* * *

 

### Dev Sub-Tasks - Estimated vs. Time Logged

* * *

  1. Select the sub-task
  2. Click Edit and the following window will appear  
  

     1. If the estimate fields are missing click the 'Configure Fields' and click the checkbox next to 'Time-Tracking'
  3. Enter the time estimate for this task
     1. This should be based upon the breakdown of the Feature and its correlation to the statement of work and the hours sold.
  4. Click Update.



* * *

* * *

 

 
