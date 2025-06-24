## 

# TDM Fax

## TDM Fax Standards

Several ITU standards established over the years

Type| Standards| Comments  
---|---|---  
Group 1/2 Analog Fax| ITU T.2/T.3| Withdrawn July 1996 (obsolete)  
Group 3 Digital Fax| ITU T.30 / T.4| What most people think of as fax  
Group 4 Fax - ISDN| ITU T.30 / T.6| Designed for 64kbit/sec digital ISDN  
  
### Group 3 Fax Standards

#### Fax Procedure

  * T.30: Defines transmission procedure
  * T.4: Defines the image coding and modulation
  * T.6: Superset of T.4 (color, ECM, MMR Compression)  
  




#### Modem Standards

  * V.17: 14400, 12000, 9600, 7200 bits/sec PSK
  * V.21: 300 bits/sec for control messages
  * V.27: 4800, 2400 bits/sec PSK
  * V.29: 9600, 7200, 4800 bits/sec QAM



### Group 3 Fax Procedure

The ITU T.30 standard defines 5 phases to a fax transfer

  * Phase A: Call Establishment
  * Phase B: Pre-Message Procedure
  * Phase C: Message Transmission
  * Phase D: Post-Message Procedure
  * Phase E: Call Release



#### Phase A - Call Establishment

Typically the calling device dials a remote number and wait for a line connection. The calling device transmits a CNG tone (1100Hz, 0.5 seconds on, 3.0 seconds off).  The called device detects the tone and transmits a CED tone (2100Hz, 1 second on, 3 seconds off). The standard defines manual connection options but they aren't used by our implementation.

#### Phase B - Pre-Message Procedure (Negotiation)

Called Device sends its Digital Identification Signal (DIS). Optionally CSI and NSF also. Informs caller of device capabilities including modulation types, error correction modes, etc. Optional Called Subscriber Information (CSI) international number of the called subscriber. Non-Standard Facilities (NSF) used for non-standard communication beyond ITU standard. Calling Device Responds with its Digital Command Signal (DCS). Optionally TSI frame can be sent. Selects capabilities of called terminal to use. Optional TSI is the transmitting terminal ID. Calling Device transmits training and TCF zero string at high speed using the modem selected via the DCS frame. Called device transmits Confirmation to Receive (CFR), Failure To Train (FTT), etc.

#### Phase C - Message Transmission

The image is transferred at high speed using the modem selected during phase B.

#### Phase D - Post-Message Procedure

 

After image is transmitted handshakes status/next phase.

  * End Of Procedure (EOP): Release call


  * End of Message (EOM): Loop to Phase B


  * Multi-Page Signal (MPS): Loop to Phase C



  
T.4 Error Correction Mode uses PPS Versions  
Partial Page Signal (PPS): PPS-EOP, PPS-EOM, PPS-MPS

#### Phase E - Call Release

The call from the fax protocol point of view is released via the DCN (disconnect) command frame. The call can also get released manually the same as any other call (hang-up). The protocol expects to run to completion including the DCN however. If the DCN fails to propagate through from the sender to receiver it can result in a loss of state synchronization between the two fax terminals. The DCN is the way the receiving fax terminal know the sender received the last page confirmation.

### Error Correction Mode (ECM)

Optional method for sending image data.  Breaks the image into HDLC frames and multiple fields. Each field holds 256 or 64 octets (8-bit bytes) of image data. A 16-bit frame checking sequence (FCS) is used to check for transmission errors.

### Fax Image Compression Types

#### Modified Huffman (MH)

One dimensional RLE compression of line data. It is most efficient when the line is mostly whitespace. This compression is defined in the ITU T.4 standard. It included end of line (EOL) information that allows re-synchronization of the image at the end of each line in case of errors. 

#### Modified Read (MR)

Two dimensional compression of line data. The 1st line is RLE encoded like MH. The following lines are compared to the previous and the differences encoded. The number of reference lines is limited.  This compression is defined in the ITU T.4 standard.  It included end of line (EOL) information that allows re-synchronization of the image at the end of each line in case of errors.

#### Modified Modified Read (MMR)

Same as MR but allows more reference lines to be used. More efficient than either MH or MR but lacks EOL symbols so loss of sync can be catastrophic to the image. Sound only be used along with error correction (ECM). The Commetrex stack used on the media server will not negotiate MMR unless ECM is being used.  This compression is defined in the ITU T.6 standard.

### Fax Standard Timer Types

The fax standard defines several different "timers" which determine timeouts for various protocol actions. You may notice references to these timers in error logs for failed sessions.

Name| Timeout| Notes  
---|---|---  
T0| 60 sec+/- 5 sec| Allowed wait time for an answer from the remote fax. When a fax machine calls out it will wait this long for a recognized response from the fax machine receiving the call. Normally the called side will respond with the CED tone or potentially with a DIS command. Our system expects to do CED tone detection outside the fax session. It most likely this timer will terminate with the DIS.  
T1| 35 sec+/-5 sec| DIS/DCS negotiation timer.  
T2| 6 sec+/- 1 sec| Fax V.21 command timeout. Amount of time a fax machine will wait for the next command.  
T3| 10 sec+/- 5 sec| Procedure interrupt timeout  
T4| 3 sec+/- 15%| Fax V.21 command response timeout. When a command is sent that expects a response this timer is used.  
T5| 60 sec+/- 5 sec| ECM busy wait timeout. This is the amount of time a transmitting fax machine will wait for the receiver.  
  
 

# FOIP - Fax Over IP

There are three primary methods for sending a fax over an IP network (FOIP). 

  * T.30/T.4/G.711 pass-through of modulated fax audio stream
  * T.37 Store and Forward Fax
  * T.38 Real Time Fax Relay



## T.30 Fax Pass-through

Unable to use a low bit rate codec Modem needs high bit rate to work. Usually only G.711 will work and only up to 14.4K. Easy for packet loss to disrupt transmission. Modems don't tolerate loss of carrier, shifting latency, and silence suppression. Actual fax data rate (before modem) is much lower than G.711 bit rate. Waste of bandwidth.

## FOIP using T.37

  * Store and Forward Faxing.
  * Reliable
  * Transmission is not real-time
  * Fax appears to send successfully however that is no guarantee of delivery.
  * The two endpoints don't negotiate capabilities leading to potentially unexpected results.
  * Not used by ININ



## FOIP using T.38

 

  * Real-Time Fax over IP
  * Designed to work like a traditional group 3 fax.
  * Allows negotiation of modem rates, image attributes, etc.
  * Modulated modem data is not sent. Control packets simulate modem control and data.
  * Still needs to work within timing constraints of T.30.
  * Packet latency and loss can be masked using several techniques.


  1.      1. T.30 allows for pauses just before the end of a row. This can be used to adjust for jitter
     2. If packet redundancy or FEC is used this can allow enough time for packet recovery.
     3. For control messages the HDLC frames don't get passed until fully received. HDLC flow control used between frames.



 

 

 

 

# HMP Fax (xIC 3.0 and earlier)

 

# Media Server Fax (xIC 4.0 and later)

 

 

V.21

This is used to send commands between fax terminals at 300 baud.  

## V.29

High speed modem, allowing 4800, 7200, and 9600 bit/s transfer modes. This is one of the high speed modems the fax protocol uses for image transfers.

## V.17

High speed modem, allowing 12K and 14.4K bit/s transfer modes. This is one of the high speed modems the fax protocol uses for image transfers.

## V.33

Not supported by the media server at this time. Used to support speeds greater than 14.4kbits/s.

## V.34

Not supported by the media server at this time. Used to support speeds greater than 14.4kbits/s.

 
