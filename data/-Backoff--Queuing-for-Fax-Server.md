Here is a first cut at adding a fax rate throttle.  Refer to the sequence diagram below. First a couple of requirement assumptions.

## SCR

This work is related to SCR 77500.

<http://bugzilla.inin.com/bugzilla/show_bug.cgi?id=77500>

##  Requirements / Assumptions

  * The IC server is sized to handle the licensed number of fax calls in addition to the voice call volume. We mainly want to cut the burst of call attempts especially when a large queue of faxes is added. Faxes without covers and a large number of recipients will be especially taxing.
  * Fax server will limit the number of simultaneous faxes based on the fax license limits and the fax group limits. The fax server will NOT reserve licenses using the license manager however it will track changes to the total number of licenses. TS is currently reserving licenses.  Since only one fax server is running for each IC server we should be able to stay in sync.
  * The following error types can be generated during a call attempt on the outgoing call thread: 
    * Out of licenses (return from TS not the internal fax server count)
    * Not licensed for fax. In theory the fax call attempt won't get made in the first place but there is a race on changes to the license status so it could happen.
    * Outbound call limit exceeded. All lines in use for this set of line groups/dial strings.
    * Call failed to complete 
      * No answer
      * Busy
      * No dial tone
      * Media server sent "fax complete" but error during transmission so retry needed.
    * Disconnected or cancelled
    * TS timeout (MS/TS down?)
    * Allocate call ID failed.
  * New configuration parameters. 
    * Max Fax Call Rate - The maximum number of calls attempts per second allowed. This parameter would be available via IA/DS.
    * Call Resource Retry Count - Number of times the call thread will attempt to place the call before it is sent back to the queue. Available through DS. Not directly set by the user.



## Description

Dialer has similar requirements in that they need to limit the number of concurrent calls and limit the call rate.  In dialer the limits are directly set by the user. For the fax server the concurrent session limit will be based on the total number of fax licenses.The call rate will be controlled by an IA/DS. The call rate will also apply to retries the call thread makes before re-queuing the fax. 

The call thread will retry the call allocation, make call, or fax initiate requests up to a configured limit if the error is resource relate (i.e. no lines, licenses available, or timeout).  Other error conditions will cause re-queuing of the fax with the envelope's retry count incremented.

## Sequence Example

Fax Server Backoff Queuing SequenceL
