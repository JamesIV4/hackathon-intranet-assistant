## Introduction

One of the most often asked questions is where do I start when I know I have a problem. With a traditional IC server based system the obvious place is the fax server logs. The fax server is the hub for all fax transfers that aren't terminated locally by a stand-alone fax machine.  Stand-alone fax machines are normally connected as station through a gateway device.  Troubleshooting transfer problems with local stand-alone fax machines is beyond the scope of this document but generally involved logs from the attached gateways and packet captures. 

## The Fax Server

Assuming the fax is terminated on a media server you can use the fax server to locate call and status information. You can start looking for problems by filtering on the FaxServer::LogFaxAttempt() method. Below are a couple of different problem examples.

 

### Call Error

Call errors can range from benign problems like busy signals to line and number routing issues.  In the fax server log message below the failure can be traced to a call connection issue because of the existence of a FSHIError. This value comes from the TS call setup process so the fax session hasn't been started yet.  

**Timestamp (UTC-05:00)**| **Message**| **Topic**  
---|---|---  
11:10:56.7992267_0199| FaxServer::LogFaxAttempt() : LOGFAXATTEMPT  
CallId=3088506341,  
FaxId=3088503695,  
EnvelopeId=3088503696,  
Direction=Outgoing,  
Success=F,  
FSHIError=**No Available Lines** ,  
DriverError=0,  
TSError=eTsError=0x111(No Available Lines),  
FailedAttempts=1,  
CallFailType=3,  
PortName=Media Server,  
PortNum=0,  
DeviceGroup=*,  
Duration=0,  
Speed=0,  
Pages=0,  
TimeSent=11/20/12 11:10:56,  
RemoteCSID=,  
RemoteNumber=0306087890,  
LocalCSID=,  
SenderName=Theo.Nieuwstraten,  
SendWhen=0,  
Begin=19:00:00,  
End=19:00:00,  
Scheduled=12/31/69 19:00:00,  
Retries=3,  
RetryDelay=0,  
T30=,  
CurrentThreadId=7984,  
QueueId=0,  
Header=,  
SignalQuality=0,  
SignalStrength=0,  
LineNoise=0,  
EnvTimeStamp=1353018018,  
FaxTimeStamp=1353018018,  
NotifyOnSuccess=Y,  
[SuccessAddress=Theo.Nieuwstraten@inin.com](mailto:SuccessAddress=Theo.Nieuwstraten@inin.com),  
NotifyOnFailure=Y,  
[FailureAddress=Theo.Nieuwstraten@inin.com](mailto:FailureAddress=Theo.Nieuwstraten@inin.com),  
MaxBPS=0,  
CoverPageName=,  
ToCompany=,  
ToName=,  
ToPhone=,  
FromName=,  
FromFaxPhone=,  
FromVoicePhone=,  
FromCompany=,  
Comment=| faxserver.server  
  
If TS couldn't establish the call it could be due to a configuration issue. One of the more common configuration issues comes from migration of version 3.0 era handlers.  Prior to the media server being used for faxing the dial plan wasn't part of the dialing of fax calls. Since the fax server dials the calls for outbound faxes the handlers need to pass a set line group and dial string lists. If the outgoing fax handler isn't properly migrated the values will be empty.  Other types of call establishment errors can usually be traced to their root cause using the TS and SIP logs.

**Timestamp (UTC-05:00)**| **Message**| **Topic**  
---|---|---  
11:12:58.0701685_0008| OutgoingFaxCall::OutgoingFaxCall() : Outgoing Fax Call.  
Call ID: 3088506381,  
Ext: 4739,  
User: Nieuwstraten, Theo,  
StationId: TheoNieuwstratenSIP,  
UserID: Theo.Nieuwstraten,  
UserQueue: Theo.Nieuwstraten,  
Attribute Names: <Eic_AccountCode>,  
Attribute Values: <>,  
Line Group Values: <**Sip failover** >,  
Dial String Values: <**0306087890** >  
Is Intercom: 0  
Queue:| faxserver.server  
  
### Fax Protocol Error

If the call established but the fax transfer failed you will see a fax attempt log entry similar to the one below. Notice that the FSHIError reports 'TS Error: eTsError=0x0(None)'. This means the call was established successfully so that isn't the cause of the problem. This means you need to look at the other error information that directly relates to the fax stack running on the media server.   These are errors at the fax protocol level.  It's usually best to move on to the media server logs for the call if TS doesn't report an error.

**Message**| **Timestamp (UTC-04:00)**| **Topic**  
---|---|---  
FaxServer::LogFaxAttempt() : LOGFAXATTEMPT  
CallId=**1088016798** ,  
FaxId=1088017064,  
EnvelopeId=1088017065,  
Direction=Outgoing,  
Success=F,  
FSHIError=**TS Error: eTsError=0x0(None)**  
Fax Session Status:  
State: Finished  
Result: Failed To Train (Line quality prevented image transfer)  
Error: 3rdDisReceived (Got a 3rd DIS frame, he can't hear us)  
Page #: 0  
Data Rate: 2400  
Resolution: Unknown  
Encoding: Unknown  
Page Size: Unknown  
Rx pages: 0  
Rx pages errors: 0  
Rx bytes: 0  
Rx lines: 0  
Total bad lines: 0  
Tx pages: 0  
Tx bytes: 0  
Tx lines: 0  
Remote SID:   
,  
DriverError=0,  
TSError=eTsError=0x0(None),  
FailedAttempts=1,  
CallFailType=3,  
PortName=Media Server,  
PortNum=0,  
DeviceGroup=*,  
Duration=38,  
Speed=2400,  
Pages=0,  
TimeSent=03/20/14 10:21:49,  
RemoteCSID=,  
RemoteNumber=855-745-3943,  
LocalCSID=,  
SenderName=John.Pennington,  
SendWhen=0,  
Begin=19:00:00,  
End=19:00:00,  
Scheduled=12/31/69 19:00:00,  
Retries=3,  
RetryDelay=0,  
T30=,  
CurrentThreadId=25944,  
QueueId=185,  
Header=,  
SignalQuality=0,  
SignalStrength=0,  
LineNoise=0,  
EnvTimeStamp=1394338439,  
FaxTimeStamp=1394338439,  
NotifyOnSuccess=Y,  
[SuccessAddress=John.Pennington@inin.com](mailto:SuccessAddress=John.Pennington@inin.com),  
NotifyOnFailure=Y,  
[FailureAddress=John.Pennington@inin.com](mailto:FailureAddress=John.Pennington@inin.com),  
MaxBPS=0,  
CoverPageName=,  
ToCompany=,  
ToName=Amber,  
ToPhone=,  
FromName=,  
FromFaxPhone=,  
FromVoicePhone=,  
FromCompany=,  
Comment=| 10:22:28.3216985_0021| faxserver.server  
  
 

## Media Server

### Media Server Extended Status Message

**Example Message**| **Notes**  
---|---  
i3faxhpaa::impl::FaxTerminatorT38Element::trace_synopsis():Fax Session Extended Status:| You can filter on 'synopsis'. There should be an extended status and synopsis.  
State: 6, | State Values:0: Idle1: Connecting2: Negotiating3: Transmitting4: Receiving5: Disconnecting6: Finished  
Result: 14145,| 0: In Progress14140: Successful14141: No Fax - No fax detected14142: Partial - some/all transferred but a protocol error occured14143: Negotiation Failed14144: Failed To Train14145: Protocol Error14146: I/O Partial - source TIFF was missing pages (send)14147: I/O Failure  
Error: 131371, | 0: No Error - No error131301: No Carrier - No fax signal was detected for T1 seconds131302: T1 Timeout - Fax signals where present, but invalid131303: No DIS or DTC - Carrier was detected but no DIS or DTC131304: Operation Mismatch - Neither Tx or Rx was possible131305: Training Failed - Training was attempted at all available speeds and was not acceptable.131306: No Training Response - Got no response to the TCF131307: Invalid Train Response - Got invalid frame in response to TCF131308: Invalid NSx - Recognized NSF/NSS/NSC was invalid131309: Invalid DIS - Received DIS/DTC was invalid131310: Out Of Rates - FTT at all available rates131311: Page Size Mismatch - Failed due to mismatch in page size131312: Resolution Mismatch - Failed due to mismatch in resolutions131313: Encoding Mismatch - Failed due to mismatch in image encoding131314: Modem Mismatch - Failed due to mismatch in available modems131315: Invalid Remote Id - Failed due to missing ID from remote131317: No PMC - No Post Message Command Received131319: Page Size Invalid - Page size is invalid131320: Resolution Invalid - Resolution is invalid131321: Encoding Invalid - Encoding is invalid.131322: Modem Rate Invalid - Modem rate is invalid.131323: ECM Mode Invalid - ECM mode is invalid131324: Record Length Invalid - Record length is invalid.131325: Invalid DCS - DCS did not match values in DIS131326: DCS From DIS Failed - Valid DCS could not be constructed from DIS or DTC131327: No PMR - No post message response was received131328: Invalid PMR - Invalid post message response was received131329: Invalid PMC - Invalid/Unrecognized Post Message command131330: No DCN After EOP - Session complete thru EOP-MCF, but no DCN131331: CTC Failure - Operation stopped due to excessive ecm retranmissions.131332: T5 Expired - Receiver failed to become ready before T5131333: No RR Response - No response to specific frame131334: No RNR Response - Most likely other end disconnected131335: No CTC Response131336: No CTR Response131337: No EOR Response131338: No PPS Response131339: Invalid RR Response - Invalid response to specific frame131340: Invalid RNR Response - Most likely machines are out of sync131341: Invalid CTC Response - sending wrong frames131342: Invalid CTR Response131343: Invalid EOR Response131344: Invalid PPS Response131345: Rx Open Fail - Rx could not open document file for rcv131346: Bad File Format - File queued for transmit was not in TIFF-F format131347: File I/O Failure - I/O error reading/writing a document131348: Doc Missing - Document was missing when transmission was attempted.131349: File EOF - Unexpected end of file was encountered131350: ECM Get Buffer Error - ECM error getting transmit buffer131351: TIO General Error - Unspecified TIO error131352: Hardware Failure - Unspecific hardware failure131353: V.21 Tx Failure - V21 Transmission failed.131354: V.21 Rx Failure - V21 Receive started but did not complete131355: HS Tx Failure - HS Modem failed to complete131356: HS Rx Failure - HS Modem rcv started but did not complete131357: Hardware Init Failure - modem could not be initialized131358: ECM Failure - problem in ECM package131359: No Memory - Attempted to allocate memory and failed131360: No Function - Attempted to use a function that is not implemented in this version. The fax operation terminated.131361: Loss of HS Sync - No valid EOL was detected for 5 seconds session disconnected131362: Internal Failure - Internal failure timer expired. Typically result of hardware failure131363: 3rd Frame Check Error - Third frame check error without good frame131364: 3rd DIS Received - Got a 3rd DIS frame, he can't hear us131365: Canceled - session canceled by application131366: Operator Interrupt - session stopped for operation interrupt131367: PRI No Response - PRI-xx was not responeded to after 3 tries131368: Remote Disconnect131369: Unexpected Condition131370: 3rd T2 Timeout - 3rd timeout on Op Alert131371: T2 Timeout131372: Tio Page Not Found - Starting page not found in TIFF131373: TIO Early EOF - TIFF File ended early, ending page not found  
Duration: 0ns,Page #: 1,|    
Data Rate: 4,| 0: 24001: 48002: 72003: 96004: 120005: 14400  
Resolution: 8,| 1: 75 x 75 dpi2: 150 x 150 dpi4: 204 x 98 - R8 x  3.85 lines/mm8: 204 x 196 - R8 x  7.7  lines/mm16: 204 x 391 - R8 x 15.4  lines/mm32: 408 x 391 - R16 x 15.4  lines/mm64: 200 x 200 dpi128: 300 x 300 dpi256: 400 x 400 dpi512: 600 x 600 dpi  
Encoding: 2, | 1: MH COmpression2: MR Compression3: MMR Compression  
Page Size: 1,| 1: A4 - ISO A4 (210mm x 297mm); (1728pels on 215mm)2: B4 - JIS B4 (257mm x 364mm); (2048pels on 255mm)4: A3 - ISO A3 (297mm x 420mm); (2432pels on 303mm)8: A6 - ISO A6 ( 864pels on 107mm) or (1728pels on 107mm)16: A5 - ISO A5 (1216pels on 151mm)32: Letter64: Legal  
ECM is used: false,Neg frame count: 4,FTT frames: 1CFR frames: 1,MCF frames: 0,ECM mode bad frames: 0,RTN frames: 0,DCN frames: 0,**** Rx pages: 0,Rx pages errors: 0,Rx bytes: 4080,Rx lines: 0,Total bad lines: 0,Tx pages: 0,Tx bytes: 0,Tx lines: 0,Unreceived packets: 0,T.38 packets sent: 4294967230,T.38 packets received: 4294967089,Bad packets received: 0,Packets corrected: 0,Packets lost: 0,Max rate: 5,Min rate: 4,Max modem: 8,Min modem: 8,Call is completed: true,Disconnect after DCS: false,DCN from receiver: false,DCN from transmitter: false,DIS only: false,CNG only: false,FTT only: false,A Quality Pages: 0,B Quality Pages: 0,C Quality Pages: 0,Page count: 0,Block count: 0,MCF Tx count: 0,MCF Rx count: 0,RTN Tx count: 0,RTN Rx count: 0,FTT Tx count: 0,FTT Rx count: 0,CFR Tx count: 0,CFR Rx count: 0,PPR Tx count: 0,PPR Rx count: 0,CTC Tx count: 0,CTC Rx count: 0,NSC count: 0,NSF count: 0,Remote ID Type: 0,NSF length: 0,NSF received: 0| ECM - Error Correction ModeNegative Frame CounterFTT - Failure To Train CounterCFR - Confirmation To Receive CounterMCF - Message (Image) Confirmation CounterECM Frames Marked BadRTN - Retrain Negative - Image Bad and Retrain Needed CounterDCN - Disconnect Frame CounterPages ReceivedPage Errors ReceivedBytes ReceivedReceived LinesTotal bad linesPages TransmittedTransmitted BytesTransmitted Lines Not UsedNot Used        "Disconnect after DCS" If true it means that the sender commanded a set of parameters for the image transfer through the DCS but never exchanged either a FTT or CFR.  Basically it means we never got past the training stage but we did exchange the DIS/DCS.  
  
 

### Fax Session Synopsis

The most recent builds of media server include a status level trace of the fax session synopsis and extended status.  You should look at these first.  Under no circumstance should increase the trace level of the Commetrex topics on a production media server. While the Commetrex traces include the most detailed information on the fax session they are very verbose and can quickly overflow the trace buffers on the media server. This will cause trace messages to be dropped which makes the media server logs less useful in general. The Commetrex trace messages can be recovered using a pcap or media server diagnostic capture of the fax transfer.

Many times the synopsis is sufficient.  In the example below the media server is attempting to receive a fax but failing.  The notes column describes the meaning of the events to the left.

 

**Message**| **Notes**  
---|---  
i3faxhpaa::impl::FaxTerminatorT38Element::trace_synopsis(): Fax Session Synopsis:30.0ms Event: Rx Hardware Ready (2), Routine: RRDYNHRY (3), State: Wait Rx Hardware Ready (1)30.0ms Event: Info DIS (130), Routine: UNEXPECT (0), State: Idle (0)60.0ms Event: Io B1 Write Done (513), Routine: UNEXPECT (0), State: Idle (0)60.0ms Event: Io Header Write Done (525), Routine: UNEXPECT (0), State: Idle (0)3.21s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)4.59s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)4.59s Event: Tx V21 Done (15), Routine: WDSRNT21 (145), State: Wait DIS Response (3)8.04s Event: T4 Expired (14), Routine: XXXXNT4X (15), State: Wait DIS Response (3)8.04s Event: FSC Error (9), Routine: RXXXNFRX (10), State: Wait DIS Response (3)8.04s Event: Info DIS (130), Routine: UNEXPECT (0), State: Idle (0)8.13s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)9.51s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)9.51s Event: Tx V21 Done (15), Routine: WDSRNT21 (145), State: Wait DIS Response (3) | Send DIS command. In this case it was sent twice before the caller responded.  
10.92s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: Info DCS (131), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: DCS (6), Routine: WDSRNDCS (7), State: Wait DIS Response (3)12.21s Event: Neg V17 Rate 14400 (830), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: Neg MR (832), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: Neg A4 (843), Routine: UNEXPECT (0), State: Idle (0)12.21s Event: Neg Resolution 204x196 (836), Routine: UNEXPECT (0), State: Idle (0) | Receive the DCS command. This sets the parameters of the image transfer to follow. In this case the sender wants to use 14.4K with MR compression.  
15.54s Event: Rx Train Fail (87), Routine: UNEXPECT (0), State: Idle (0)15.54s Event: Rx Train Fail (55), Routine: RTCFNRFL (27), State: Receive Train (6)15.54s Event: Frame FTT (209), Routine: UNEXPECT (0), State: Idle (0)15.63s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)16.74s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)16.74s Event: Tx V21 Done (15), Routine: WDSRNT21 (145), State: Wait DIS Response (3)18.15s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: Info DCS (131), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: DCS (6), Routine: WDSRNDCS (7), State: Wait DIS Response (3)19.44s Event: Neg V17 Rate 12000 (829), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: Neg MR (832), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: Neg A4 (843), Routine: UNEXPECT (0), State: Idle (0)19.44s Event: Neg Resolution 204x196 (836), Routine: UNEXPECT (0), State: Idle (0) | FTT is Failure To Train. The sender sent a stream of training bits to determine if the commanded parameter would work reliably.  In this case they didn't so the receiver sent a FTT command back to the sender.  This causes the sender to send a new DCS so that the training can be attempted at a slower speed. The new speed to try is 12000.  
22.74s Event: Rx Train End (86), Routine: UNEXPECT (0), State: Idle (0)22.74s Event: Rx Train End (54), Routine: RTCFNERT (26), State: Receive Train (6)22.74s Event: Frame CFR (201), Routine: UNEXPECT (0), State: Idle (0)22.83s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)23.94s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)23.94s Event: Tx V21 Done (15), Routine: RISTNT21 (38), State: Receive Image Start (10)| The new training was successful. you know it was successful because of the CFR that follows. CFR is Confirmation For Receive. That is how the receiver tells the sender it understood the training signal at that speed and the sender is ok to start with the image data for that page.  
25.56s Event: Hs Rx Start (92), Routine: UNEXPECT (0), State: Idle (0)25.56s Event: Rx Image Start (58), Routine: RISTNSRI (36), State: Receive Image Start (10)28.44s Event: Hs Rx End (93), Routine: UNEXPECT (0), State: Idle (0)28.44s Event: Rx Image End (74), Routine: RIMGNERI (87), State: Receive Image (16)28.44s Event: Io Image Write (520), Routine: UNEXPECT (0), State: Idle (0)28.44s Event: Io B1 Write (509), Routine: UNEXPECT (0), State: Idle (0)28.5s Event: Io B0 Write Done (512), Routine: UNEXPECT (0), State: Idle (0)28.5s Event: Io Image Write Done (528), Routine: UNEXPECT (0), State: Idle (0) | HS Rx is High Speed Modem Receive. The commands like DIS/DCS/FTT are sent via half duplex 300 baud modem (V.21).  When it sends the image data it switches to the negotiated high speed modem which in this case is V.17.  The high speed modems cover a range of bit rates. The IO events are the image data being written to disk.  
35.46s Event: T2 Expire (59), Routine: XXXXNT2X (150), State: Function End Normal (26)35.46s Event: GoToB (10), Routine: XXXXNGOB (11), State: Function End Normal (26)35.52s Event: Fax Stopped (102), Routine: UNEXPECT (0), State: Idle (0)35.52s Event: Hardware Close (16), Routine: WCLSNCLS (17), State: Wait Hardware Close (4)35.52s Event: Io Write Last Tiff IFD (535), Routine: UNEXPECT (0), State: Idle (0)35.52s Event: Io Tiff IFD Write (515), Routine: UNEXPECT (0), State: Idle (0)35.52s Event: Io B0 Write (508), Routine: UNEXPECT (0), State: Idle (0)35.52s Event: Session Complete (1234), Routine: UNEXPECT (0), State: Idle (0)35.58s Event: Io B1 Write Done (513), Routine: UNEXPECT (0), State: Idle (0)35.58s Event: Io Write Last Tiff IFD Done (536), Routine: UNEXPECT (0), State: Idle (0)35.58s Event: Io Tiff Write Done (537), Routine: UNEXPECT (0), State: Idle (0) | Here is the error. The T2 timer has expired. What should happen is the sender will switch back to the V.21 modem and send a command that lets the receiver know if it should expect more pages. For non ECM transfers this is a MPS or EOP command.  MPS is MultiPage Signal meaning there are more pages to come.  EOP is End Of Procedure meaning that was the last page.  The receiver would then either confirm the quality of the page or fail it in response. ECM mode uses a completely different set of commands. In this case I don't see any evidence the sender ever sent the MPS or EOP so checking to see if the call is now disconnected is worth a look.  If the call is still active you will need a capture that will probably tell you the same thing. No more packets from the sender.  At that point it is something to investigate at the carrier and/or gateway.  
  
 

 

 

 

In this example the Media Server is attempting to send a fax. The states are a bit different because we are sending. This example includes a re-training to a lower speed because of a page error.

Message| Notes  
---|---  
i3faxhpaa::impl::FaxTerminatorT38Element::trace_synopsis(): Fax Session Synopsis:|    
      
    
    60.0ms Event: Io B0 Read Done (510), Routine: UNEXPECT (0), State: Idle (0)
    
    
    60.0ms Event: Io Header Read Done (524), Routine: UNEXPECT (0), State: Idle (0)
    
    
    60.0ms Event: Io Tiff IFD Read (514), Routine: UNEXPECT (0), State: Idle (0)
    
    
    60.0ms Event: Io B1 Read (507), Routine: UNEXPECT (0), State: Idle (0)
    
    
    180.0ms Event: Io B1 Read Done (511), Routine: UNEXPECT (0), State: Idle (0)
    
    
    180.0ms Event: Io Tiff IFD Read Done (522), Routine: UNEXPECT (0), State: Idle (0)
    
    
    180.0ms Event: Io Header Read (516), Routine: UNEXPECT (0), State: Idle (0)
    
    
    180.0ms Event: Io B0 Read (506), Routine: UNEXPECT (0), State: Idle (0)
    
    
    240.0ms Event: Io B0 Read Done (510), Routine: UNEXPECT (0), State: Idle (0)
    
    
    240.0ms Event: Io Header Read Done (524), Routine: UNEXPECT (0), State: Idle (0)
    
    
    240.0ms Event: Io Tiff IFD Read (514), Routine: UNEXPECT (0), State: Idle (0)
    
    
    240.0ms Event: Io B1 Read (507), Routine: UNEXPECT (0), State: Idle (0)
    
    
    300.0ms Event: Io B1 Read Done (511), Routine: UNEXPECT (0), State: Idle (0)
    
    
    300.0ms Event: Io Tiff IFD Read Done (522), Routine: UNEXPECT (0), State: Idle (0)
    
    
    300.0ms Event: Io 1st Image Read (518), Routine: UNEXPECT (0), State: Idle (0)
    
    
    300.0ms Event: Io B0 Read (506), Routine: UNEXPECT (0), State: Idle (0)
    
    
    360.0ms Event: Io B0 Read Done (510), Routine: UNEXPECT (0), State: Idle (0)
    
    
    360.0ms Event: Io 1st Image Read Done (526), Routine: UNEXPECT (0), State: Idle (0)

| At the beginning of the fax session you'll see a bunch of I/O. This is the fax stack reading in the TIFF header from the first source file. TIFF files can have more than one image in them and the IFD is a structure the identifies the structure of the image.  
      
    
    360.0ms Event: Tx Hardware Ready (4), Routine: TRDYNHTY (5), State: Wait Tx Hardware Ready (2)
    
    
    3.27s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: Info DIS (130), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: DIS (7), Routine: XXXXNDIS (19), State: Wait DIS (5)
    
    
    4.62s Event: Remote Rx (47), Routine: WDISNRRX (22), State: Wait DIS (5)
    
    
    4.62s Event: Neg V17 Rate 14400 (830), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: Neg MR (832), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: Neg Resolution 300x300 (840), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: Neg Letter (846), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.62s Event: Info DCS (131), Routine: UNEXPECT (0), State: Idle (0)
    
    
    4.71s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    6.09s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    6.09s Event: Tx V21 Done (15), Routine: WDISNT21 (25), State: Wait DIS (5)
    
    
     

| This is the standard DIS/DCS exchange. The party we called sends us their DIS and we send them the DCS so they know what to expect for modem speed, image compression, etc.  
      
    
    9.3s Event: Tx Train End (89), Routine: UNEXPECT (0), State: Idle (0)
    
    
    9.3s Event: Tx Train End (56), Routine: XXXXNT21 (16), State: Wait Train Response (9)
    
    
     

| This is the training we send to the called party.  
      
    
    9.51s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    10.59s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    10.59s Event: Frame CFR (201), Routine: UNEXPECT (0), State: Idle (0)
    
    
    10.59s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    10.59s Event: CFR (17), Routine: WTTNNCFR (30), State: Wait Train Response (9)
    
    
     

| We receive the CFR from the called party.  This looks slightly different in the synopsis when we are sending the fax and not receiving it. In this case there is an extra synopsis entry for the handling of the CFR. The WTTNNCFR is an internal state that just means we were in the wait for training response state when we got the response (as expected).  
      
    
    10.89s Event: Hs Tx Start (90), Routine: UNEXPECT (0), State: Idle (0)
    
    
    10.89s Event: Tx Image Start (72), Routine: XXXXNTIB (79), State: Send Image (14)
    
    
    12.54s Event: Hs Tx End (91), Routine: UNEXPECT (0), State: Idle (0)
    
    
    12.54s Event: Tx Image End (71), Routine: XIMGNETI (80), State: Send Image (14)
    
    
    12.54s Event: End Page (68), Routine: XIMGNEPG (77), State: Send Image (14)

| We send the page via high speed modem.  
      
    
    12.54s Event: Frame MPS (211), Routine: UNEXPECT (0), State: Idle (0)
    
    
    12.63s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    13.74s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    13.74s Event: Tx V21 Done (15), Routine: WMPSNT21 (103), State: Wait MPS Response (20)
    
    
     

| Switched back to V.21 modem to send the MPS signal indicating this isn't the last page.  WMPSNT21 is the internal state name for the fax stack. In this case it means the MPS is finished sending via V.21 and we are transitioning to waiting for a response from the called party.  
      
    
    13.92s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.0s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.0s Event: Frame MCF (210), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.0s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.0s Event: MCF (32), Routine: WMPSNMCF (100), State: Wait MPS Response (20)
    
    
     

| We received the MCF command from the called party confirming the page image.  Like the CFR handling above you will see this logged in two parts when we are the image sender. First is the reception of the raw command data via V.21 modem. Second we see the internal state handling of the event (WMPSNMCF).  It just means we received the MCF after we sent a MPS.  
      
    
    15.3s Event: Hs Tx Start (90), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.3s Event: Tx Image Start (72), Routine: XXXXNTIB (79), State: Send Image (14)
    
    
    15.45s Event: Hs Tx End (91), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.45s Event: Tx Image End (71), Routine: XIMGNETI (80), State: Send Image (14)
    
    
    15.45s Event: End Page (68), Routine: XIMGNEPG (77), State: Send Image (14)

| Sent 2nd page.  
      
    
    15.45s Event: Frame MPS (211), Routine: UNEXPECT (0), State: Idle (0)
    
    
    15.54s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    16.65s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    16.65s Event: Tx V21 Done (15), Routine: WMPSNT21 (103), State: Wait MPS Response (20)

| Switched back to V.21 to send the MPS signal. More pages to come.  
      
    
    16.83s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: Frame RTN (219), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: RTN (51), Routine: WMPSNRTN (101), State: Wait MPS Response (20)
    
    
    17.91s Event: Neg Lower Rate (820), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: GoToD (76), Routine: XXXXNGTD (94), State: Wait MPS Response (20)

| We received a RTN from the called party. They didn't like the quality of the received image and want to retrain at a lower speed.  The GoToD indicates we need to send a new DCS so the called party knows what to expect for the retraining it requested.  
      
    
    17.91s Event: Neg V17 Rate 12000 (829), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: Neg MR (832), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: Neg Resolution 300x300 (840), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: Neg Letter (846), Routine: UNEXPECT (0), State: Idle (0)
    
    
    17.91s Event: Info DCS (131), Routine: UNEXPECT (0), State: Idle (0)
    
    
    18.0s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    19.38s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    19.38s Event: Tx V21 Done (15), Routine: WDISNT21 (25), State: Wait DIS (5)

| We are now telling the called party to expect 12000 bits/sec  
      
    
    19.68s Event: Tx Train Start (88), Routine: UNEXPECT (0), State: Idle (0)
    
    
    22.59s Event: Tx Train End (89), Routine: UNEXPECT (0), State: Idle (0)
    
    
    22.59s Event: Tx Train End (56), Routine: XXXXNT21 (16), State: Wait Train Response (9)

| Send the training at 12000. Wait for a response from the called party.  
      
    
    22.8s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    23.88s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    23.88s Event: Frame CFR (201), Routine: UNEXPECT (0), State: Idle (0)
    
    
    23.88s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    23.88s Event: CFR (17), Routine: WTTNNCFR (30), State: Wait Train Response (9)

| Received CFR so we are clear to send at the new speed.  
      
    
    24.18s Event: Hs Tx Start (90), Routine: UNEXPECT (0), State: Idle (0)
    
    
    24.18s Event: Tx Image Start (72), Routine: XXXXNTIB (79), State: Send Image (14)
    
    
    24.33s Event: Hs Tx End (91), Routine: UNEXPECT (0), State: Idle (0)
    
    
    24.33s Event: Tx Image End (71), Routine: XIMGNETI (80), State: Send Image (14)
    
    
    24.33s Event: End Page (68), Routine: XIMGNEPG (77), State: Send Image (14)

| 3rd page sent at high speed.  
      
    
    24.33s Event: Frame MPS (211), Routine: UNEXPECT (0), State: Idle (0)
    
    
    24.42s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    25.53s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    25.53s Event: Tx V21 Done (15), Routine: WMPSNT21 (103), State: Wait MPS Response (20)

| Switched back to V.21 to send the MPS signal. More pages to come.  
      
    
    25.71s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.79s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.79s Event: Frame MCF (210), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.79s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.79s Event: MCF (32), Routine: WMPSNMCF (100), State: Wait MPS Response (20)

| Image was confirmed by the called party. Ok to continue.  
      
    
    26.79s Event: Io 1st Image Read (518), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.79s Event: Io B1 Read (507), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.85s Event: Io B1 Read Done (511), Routine: UNEXPECT (0), State: Idle (0)
    
    
    26.85s Event: Io 1st Image Read Done (526), Routine: UNEXPECT (0), State: Idle (0)

| More disk I/O reading image information.  
      
    
    27.09s Event: Hs Tx Start (90), Routine: UNEXPECT (0), State: Idle (0)
    
    
    27.09s Event: Tx Image Start (72), Routine: XXXXNTIB (79), State: Send Image (14)
    
    
    33.93s Event: Hs Tx End (91), Routine: UNEXPECT (0), State: Idle (0)
    
    
    33.93s Event: Tx Image End (71), Routine: XIMGNETI (80), State: Send Image (14)
    
    
    33.93s Event: End Page (68), Routine: XIMGNEPG (77), State: Send Image (14)

| Next page sent  
      
    
    33.93s Event: Frame MPS (211), Routine: UNEXPECT (0), State: Idle (0)
    
    
    34.02s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    35.13s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    35.13s Event: Tx V21 Done (15), Routine: WMPSNT21 (103), State: Wait MPS Response (20)

| Switched back to V.21 to send the MPS signal. More pages to come.  
      
    
    35.31s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    36.39s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    36.39s Event: Frame MCF (210), Routine: UNEXPECT (0), State: Idle (0)
    
    
    36.39s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    36.39s Event: MCF (32), Routine: WMPSNMCF (100), State: Wait MPS Response (20)

| Image was confirmed by the called party. Ok to continue.  
      
    
    36.69s Event: Hs Tx Start (90), Routine: UNEXPECT (0), State: Idle (0)
    
    
    36.69s Event: Tx Image Start (72), Routine: XXXXNTIB (79), State: Send Image (14)
    
    
    42.33s Event: Hs Tx End (91), Routine: UNEXPECT (0), State: Idle (0)
    
    
    42.33s Event: Tx Image End (71), Routine: XIMGNETI (80), State: Send Image (14)

| Next page sent  
      
    
    42.33s Event: Last Document (69), Routine: XIMGNLST (78), State: Send Image (14)
    
    
    42.33s Event: Frame EOP (206), Routine: UNEXPECT (0), State: Idle (0)
    
    
    42.42s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    43.53s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    43.53s Event: Tx V21 Done (15), Routine: XXXXNT21 (16), State: Wait EOP Response (21)

| That was the last page so end the EOP.  
      
    
    43.71s Event: V21 Rx Start (81), Routine: UNEXPECT (0), State: Idle (0)
    
    
    44.79s Event: V21 Rx Frame (94), Routine: UNEXPECT (0), State: Idle (0)
    
    
    44.79s Event: Frame MCF (210), Routine: UNEXPECT (0), State: Idle (0)
    
    
    44.79s Event: V21 Rx End (82), Routine: UNEXPECT (0), State: Idle (0)
    
    
    44.79s Event: MCF (32), Routine: WEOPNMCF (104), State: Wait EOP Response (21)

| Page confirmed.  
      
    
    44.79s Event: Frame DCN (204), Routine: UNEXPECT (0), State: Idle (0)
    
    
    44.88s Event: V21 Tx Start (83), Routine: UNEXPECT (0), State: Idle (0)
    
    
    45.99s Event: V21 Tx End (84), Routine: UNEXPECT (0), State: Idle (0)
    
    
    45.99s Event: Tx V21 Done (15), Routine: XDCNNT21 (29), State: Send DCN (8)
    
    
    46.05s Event: Fax Stopped (102), Routine: UNEXPECT (0), State: Idle (0)
    
    
    46.05s Event: Hardware Close (16), Routine: WCLSNCLS (17), State: Wait Hardware Close (4)
    
    
    46.05s Event: Io Tiff Read Done (539), Routine: UNEXPECT (0), State: Idle (0)
    
    
    46.05s Event: Session Complete (1234), Routine: UNEXPECT (0), State: Idle (0)

| Since that was the last page and we got a confirmation all we need to do is send the disconnect.  
  
 

 

 

 
