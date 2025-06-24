In this meeting we went over SIP to the Media Server configuration.

  * Add configuration for digest authentication (needed on both sides).
  * Even though SBCs do not support TLS at the moment we still need to add configurations for it as it is the only way we can securely support SRTP to the media server.
  * By default the media server will use the command server notifier address for SIP. We will provide a checkbox to override this and if checked we will have a text field where the user can type in a custom address.
  * On the IC server, the SIP listener in the mediaserverapi needs to default to the same adapter that notifier uses. We have to find out if the name of the interface currently being used by notifier is available.


  * We need to figure out how to generate certificates to use for TLS on the media server.


