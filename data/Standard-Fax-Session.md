## Introduction

The image below is from Wireshark. It shows the command and data flows between the two fax terminals when the pages are being sent without ECM.   Commands such as DIS/DCS use the 300 baud V.21 modem (half duplex) but all image information is sent with a faster (high speed) modem. The media server supports speeds up to 14.4K using a V.17 modem. You will notice that commands start with a V.21 preamble and send with a 'no-signal' packet.  The V.21 preamble corresponds to a bit sequence that is sent prior to the standard of commands in T.30 (audio). The no-signal packet represents the quiet period that follows the end of the command. In general T.38 is a way to represent the T.30 protocol via packets instead of audio.

This page is meant to provide an example of a normal fax transmission.  More details can be found by reading the ITU T.30 standard along with the related T.4, T.6, and T.38 standards.

## Call Establishment

The session starts with the exchange of tones.  The caller is normally the sender of the page.  When the call is connected called party will send out a CED (**C** all**ED**) tone sequence.  The caller will respond with a CNG (**C** alli**NG**) tone sequence. 

## Session Negotiation 

The next step is for the called terminal to send a DIS and optionally a CSI.  The DIS is used to tell the caller what capabilities the receiver has. This includes modems, compression types, etc. The CSI can be used to identify the called terminal usually in the form of a phone number. Once the caller receives the DIS command it will respond with a DCS and optionally a TSI command(s). The DCS is used by the sender to tell the receiver how it plans to send the images including the modems, compression, etc.  The DCS is based on the information the sender received in the DIS. The TSI command can be used to identify the calling terminal usually in the form of a phone.

Soon after the caller sends the DCS command it will switch the to the selected high speed modem to send training information. In the example below the sender starts at 9600 baud using a V.29 modem. Training is used to gauge if the current line conditions will permit the reliable transmission of an image at the selected speed. It contains a predetermined bit pattern that lasts 1.5 seconds. If the called fax terminal receives the training information without error it will respond with the CFR.  This tells the sender it's ok to start the transmission. 

## Image Transfer

After the sender receives the CFR command it will begin sending the image data for the first page.  The image starts with a bit pattern to sync up the image data followed by the image.  The image is compressed using one of three formats: MH, MR, or MMR. MH and MR compression is supported by all fax machines.  Each line is run length encoded with an end of line (EOL) symbol at the end.  Since each line is a standard 1728 pixels wide the EOL can be used to judge when a line has been received correctly and where to start the next line when errors are found.  When MMR  compression is used the EOL isn't included which makes re-synchronization impossible. MMR compression should be avoided without ECM for this reason.  

One the sender completes the image transfer it switches back to the V.21 modem to send either a MPS or EOP command.  The MPS command tells the receiver it should expect more pages. The EOP command indicates the last page has been sent.  It is then up to the receiver to judge the quality of the page.  In this case the page was received correctly so the receiver responds with the MCF command.  There are other commands to indicate the page was rejected and if training at a different speed is required. 

## Call Completion

After the sender indicates the final page has been sent via the EOP command and the receiver has confirmed the page, the sender will transmit a final DCN command that indicates the call should be disconnected.  It's important that the receiver gets this command because without it the receiver has no way on knowing if the sender received the final page confirmation.  This could mean the sender would fail the session when the receiver would mark it ok without further information.  I've seen bugs in the past caused by the premature disconnect of a call before the final DCN.  This can happen when on part is satisfied with the transfer but the commands haven't propagated completely through the gateways. The two terminals can end up with different results in this case.

 

 
