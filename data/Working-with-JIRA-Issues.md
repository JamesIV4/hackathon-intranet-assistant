## Description

* * *

When working on a JIRA Issue the flow that is used is based on the type of issue being worked on. The majority of the time the issue being worked on is a New Feature or a Bug. Once the issue is assigned it is the assigned persons responsibility to see it through resolution. Seeing it through resolution can vary as to what needs to happen with the Issue while the work is being performed. The typical process for an Issue is outlined below.

* * *

* * *

* * *

## Process

* * *

  1. JIRA Issue is assigned to an individual by a team leader or manager that determines they have the right skill set to resolve the issue or are the component owner for the issue being opened.  

     1. The Status change here on the issue will be from 'Waiting for Review' to 'Accepted'
  2. The individual assigned the Issue will move the issue into an 'In Progress' state and begin working.
     1. If at some point during that time the assignee realizes or deems the issue to not belong with them then they could assign it to the correct person adding a comment as to why they have assigned the issue to that person.
  3. The work is done, now what?
     1. Local testing of the changes made need to happen to determine that the goals of the Issue have been completed or resolved.
     2. At this point it needs to be submitted into Source Control via the command line or Perforce Visual Client
     3. Once submitted the status of the issue needs to be moved from 'In Progress' to 'Integration Test'
  4. I've locally tested and submitted my changes, now what?
     1. Once the changes have gone through a build they need to be tested again and verified that the goals of the Issue have been met.
     2. After that testing is complete the Issue may be marked as 'Resolved-FITC'
        1. FITC - Fixed, Integration Test Complete.



* * *

* * *

* * *

 
