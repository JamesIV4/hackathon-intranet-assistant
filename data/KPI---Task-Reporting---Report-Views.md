## **KPI Reporting**

Here's a rough look at what a KPI report might look like.  There is typically a standard set covering containment.  In addition, there can be a customer specific set depending on their needs (and what's possible in the logging):

 

KPIs (Containment)  
---  
   Contained| 85.0%  
           Self-Service| 70.0%  
           No Self-Service| 15.0%  
     Transferred| 15.0%  
           Agent Requests|   8.0%  
           Business Rule   transfers|   5.0%  
           Error-Based transfers  |   2.0%  
KPIs (Custom)|    
---|---  
Caller Intent Recognition Rate (non-agent)| 82.9%  
Authentication Rate| 52.5%  
Repeat Caller Rate (within 24 hrs)| 31.7%  
Early Abandons| 8.1%  
Call Duration| 86.7 sec  
Average Number of Dialog Turns   per Call| 5.76  
  
## **Task Reporting**

Task reporting looks a bit differently.  Typically, you will have one high-level table that reports on all of the tasks, followed by individual tables breaking down each task in more detail:

 

**Task Performance**  
---  
Task| Usage   Rate| Completion Rate| Caller  Hang-up| Other   Exit  
Entry to the Application| 100.0%| 100.0%| 0.0%| 0.0%  
Caller Intent Capture| 79.4%| 82.9%| 5.9%| 11.2%  
Authentication| 70.1%| 48.3%| 15.2%| 36.5%  
PayABill| 31.7%| 89.5%| 4.5%| 6.0%  
ChangePin| 13.9%| 87.5%| 3.3%| 9.2%  
  
**Task Details:   ChangePin**

Success| Count| Percent  
---|---|---  
Callers   successfully confirm PIN change| 3,910| 87.5%  
**Total    Completions**| **3,910**| **87.5%**  
Early   Exit Points| Count| Percent  
---|---|---  
Max recognition errors in GW6000_GetNewPIN_DM| 80| 3.8%  
Hang-ups at GW6000_GetNewPIN_DM| 70| 3.3%  
Operator requests at GW6000_GetNewPIN_DM| 62| 2.9%  
Max timeout errors in GW6000_GetNewPIN_DM| 30| 1.4%  
Other| 24| 1.1%  
**Total    Exits**| **266**| **12.5%**
