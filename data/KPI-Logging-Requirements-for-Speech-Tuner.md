# Description

This page captures some of the basic logging requirements proposed for enabling high-level KPI measurements within the Speech Tuner tool.  For basic KPI logging, there should be a **callstart** and **callend** log entry set within the VXML code and logged by the platform.  These log entries would be fired at the start and finish of each call, respectively.  The fields for each might encompass:

## callStart 

  * ANI
  * DNIS (optional)
  * CallerType (optional)
  * ApplicationName (optional)
  * CustomerName (optional)
  * SessionID
  * StartTime



## callEnd

  * ExitType - "hangup" or "transfer"
  * ExitReason
    * AgentRequestTransfer
    * BusinessRuleTransfer
    * CallerHangup
    * SystemHangup
    * MaxNoMatch
    * MaxNoInput
    * SystemError (e.g. syntax error, missing url, backend error)
    * EarlyAbandon (caller hungup before providing any input)


  * EndTime
  * LastState - the final active state from which the call ended (dialog, decision, or backend).  If there's a generic transfer handler in the VXML code, we would probably want to be able to skip this state, picking the previous one.
  * SessionID (if logs intermix multiple calls)



 
