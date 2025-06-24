# Fax Call Rings Through to Client

## Description

Incoming call from a fax machine plays the CNG (CalliNG) tone but it is still routed through to the client. The 

This is caused by the 'CUSTOM::Ringback Only' being set true. This attribute is supposed to disable the name prompt when someone calls them directly but should allow faxes to come through. In reality it is currently broken in Clay SU2. The tone detection will be completed and the fax forwarded to the fax server. When the fax server tries to initiate the fax it will fail. The blind transfer logic may be at fault?

## Referenced Incident Cases

ININ Ticket #26881

## Workaround

Disable 'CUSTOM::Ringback Only'
