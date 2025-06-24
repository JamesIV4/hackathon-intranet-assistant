Our PureCloud test org was setup according to  and the parent page for enabling features and products .

## Org details

Org id: 5c96c307-15eb-4f49-98c2-04654051a325

Short org name: speechtech

adminEmail: pureconnectspeechtech@[genesys.com](http://genesys.com)

admin password: Testing1234!

name: SpeechTechUser

Login (linked from [here](https://confluence.inin.com/display/~Komal.Patel/Service+Delivery+-+How+To+-+Create+a+New+Org+and+Enable+Collaborate+Pro%2C+Communicate%2C+Engage%2C+PureVoice#Tabs-619984657)): <https://apps.inindca.com/directory/#/login>

Note: since this org is in a lower environment (not production), there may be stability issues contributing to an issue you may be seeing when testing.  Please check the PureCloud chat groups, "Lower Environment Stability" and "Breaking Changes" to make sure your issue is not related to the lower environment (e.g., DCA).

## Steps taken to create and setup the org

  1. Stage the org (does not require VPN access):
     1. POST to <https://apps.inindca.com/onboarding/api/provisioning/stageNewOrg> (application/json content-type in header), with body:  

        1. {  
"firstName":null,  
"lastName":null,  
"emailAddress":"pureconnectspeechtech@[genesys.com](http://genesys.com)",  
"orgName":"Speech Tech",  
"locale":"en-us",  
"_includeEmailBodyInResponse": true,  
"_skipEmailSending": true  
}
     2. For example, using Postman:
        1.         2.      3. In the response body, search for the word "job" and copy the number between '=' and '&'
        1.   2. Complete provisioning (does not require VPN access)  

     1. POST to <https://apps.inindca.com/onboarding/api/provisioning/completeProvisioning> with body:
        1. {  
"jobId":"8c4a8722-390b-453f-857a-c957a9f3623a",  
"adminEmail":"pureconnectspeechtech@[genesys.com](http://genesys.com)",  
"adminPassword":"Testing1234!",  
"name":"SpeechTechUser",  
"otherUsers":  
[],  
"locale":"en-us",  
"disableOrgAutoJoin":true,  
"_skipEmailSending": true,  
"enableHipaaFeatures": false  
}
     2.      3. ... which gives the response of (save the org ID to use further below):
     4. {  
"orgId": "5c96c307-15eb-4f49-98c2-04654051a325",  
"jobId": "8c4a8722-390b-453f-857a-c957a9f3623a",  
"orgShortName": "speechtech"  
}

  3. Enable features
     1. First connect to the region in question, in this case DCA.
     2. Note: replace {{Region}} with inindca, for example, as well as {{orgid}} with your organization ID given in the response during provisioning.  See step 3 here for reference: 
     3. Contact Center
        1. POST to <http://directory>.{{Region}}/directory/v1/organizations/{{orgid}}/features/contactCenter
        2. ... with the body of: {"enabled":true}
        3.      4. Unified Communications
        1. POST to <http://directory>.{{Region}}/directory/v1/organizations/{{orgid}}/features/unifiedCommunications
        2. ... with the body of: {"enabled":true}
        3.      5. Etc. for any additional features you may need.
  4. Enable products
     1. First connect to the region in question, in this case DCA. 
     2. Note: products are enabled through the Donut service, see step 4 for a list of common products and how to get a list of all: .  To enable a product, instead of a POST request, use a PUT request to <https://donut>.{{Region}}/v2/organizations/{{orgid}}/products/{product}, where {product} should be replaced with the product name (no body request required).
     3. Products enabled: these were the products enabled for our team
        1. communicate, engage1, engage, engage3  

        2. For example, to enable the 'communicate' product, send a PUT request to <https://donut>.[us-east-1.inindca.com](http://us-east-1.inindca.com)/v2/organizations/5c96c307-15eb-4f49-98c2-04654051a325/products/communicate
        3. After all products are enabled, a list of enabled products can be seen with a GET request to: <https://donut.us-east-1>.inindca.com/v3/organizations/5c96c307-15eb-4f49-98c2-04654051a325/products, where 5c96c307-15eb-4f49-98c2-04654051a325 is the orgid.


