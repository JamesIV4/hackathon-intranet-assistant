3

# Description

* * *

TBD

# Database Table Details

* * *

These three database tables will be added to the IC database.

Show Table GraphicKPI DB Table Graphictrue

KPI DB Table Graphic

 

## Database Type Descriptions

The following table outlines the database types for the different columns in the tables and the tables those columns relate to. 

Show Data Types Data Types

Data Types

 

## Database Record Examples

The following is an example of what the database tables will look like when using the two step approach for the Event(StartCall | EndCall) and Task(StartTask | EndTask) tables with an initial insert and later update statement.

Show Record ExamplesRecord Examplestrue

Record Examples

 

 

KPI Database Example Records970eventDisplays single and multi-record examples for the type of StartCall and EndCallIVR_SPEECH_EVENT

KPI_DB_ExampleTables.xlsxfalseIVR_SPEECH_EVENT5

taskDisplays single and multi-record examples of the task type StartTask and EndTaskIVR_SPEECH_TASK

KPI_DB_ExampleTables.xlsxfalseIVR_SPEECH_TASK5

callpathDisplays the single record example of the CallPath typeIVR_SPEECH_PATH

KPI_DB_ExampleTables.xlsxfalseIVR_SPEECH_PATH5

## Interaction Handler Implementation

* * *

The following graphic depicts when a database write will occur when using the initial insert when StartCall / StartTask / CallPath occurs as well as when the row is updated at the EndCall / EndTask event.

Show DesignDB Writes

DB Writes

SQL Statements used in Custom Logging Passthrough tool step SQLStatements

SQLStatements

# Questions, Risks and Concerns

* * *

**Scalability**  scalabilitytrue

scalability

A speech application will potentially process thousands of calls a great deal of which could be concurrent. I'm curious as to what scalability issues I might run into and the following question came up during the meeting with Trent. I'm sure there are more things I'm not thinking of....

**Q:  **Will there be scalability issues with causing an IP delay resulting in an IP hang?

**A:  **It depends upon the call volume/throughput, 1000 calls a second... possibly, 1000 calls a minute / hour / day.... unlikely.

**Thoughts:**

The preferred method in my opinion is to use the single record approach as that will provide the most robustness for database sizing and read performance with respect to reporting.

**Switchover  ** switchovertrue

switchover

**Q:**  What will happen if a switchover occurs?

**A:**  All calls in the IVR will be lost as occurs in CIC today?

* * *

**Q:**  How does IC handle database inserts for calls that are lost during a switchover?

**A:  **The [PMQ](https://confluence.inin.com/display/CIC/Working+with+PMQ) process handles situations in which the DB is unavailable. It writes out the sql statements (inserts, updates, deletes) to a PMQ file (a text file) and will process the records when the database is available. This could still result in incomplete data, i.e. StartCall or StartTask rows that didn't reach the Update Row command. But that is inevitable in the event of a switchover.

**Statistics Model for Data Inserts**  statistics_modeltrue

statistics_model

The statistics that IC adds are based upon an interval that is defined by a server parameter within Interaction Administrator. This parameter defines the intervals, the minimum initial value being 15 minutes and in 15 minute increments, at which statistical data is added to the database. This method introduces an i3Timestamp that records the time at which the data was inserted.

**Q:**  Would / Could KPI Logging use this model?

**A:**  Yes.

* * *

**Q:**  Will a 15 minute delay on statistics be okay for the customer?

**A:**  They are used to this now so the precedent is already set. Using this method we all but eliminate the performance hit to IP which would be caused by doing all of the insert work real-time.

     Add interval offset so that these inserts don't occur at the same time as StatServer or WFM.

* * *

**Q:**  How would this work?

**A:**  A file would be created with all of the SQL statements. Then a new handler which is timer based will consume the statistic interval server parameter and update the database using that flat file.

**Indexing**  indexingtrue

indexing

**Q:**  Which columns should be indexed?

**A:**  Start Times, End Times, ANI, and DNIS for sure. Then the customer can add indexes based on the data they wish to report on most often. For Speech Tuning needs an index shouldn't be needed. This is something that can be discussed with the rest of the team though.

**Purging Records**  purgingtrue

purging

This is configurable by the customer and for IC and I believe is defaulted to 400 days.

**Q:**  Should a purging schedule exist for these tables? 

**A:**  ???

**Separate Database Structure**  db_structuretrue

db_structure

**Q:  **Should this information be stored in a different database, database server, etc?

**A:**  For the current iteration / phase this isn't something that is possible but definitely could be something investigated for later phases.
