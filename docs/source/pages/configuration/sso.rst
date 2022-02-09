=================
SSO Configuration
=================

.. toctree::

SSO Properties (app.sso)
========================

| **enabled** - To enable sso support
| **login-auto-submit** - Stay on login form or try to submit it immediately after rendering
| **first-name-prop-name** - Mapper field name for "First Name" to retrieve from IdP ('firstName' by default)
| **last-name-prop-name** - Mapper field name for "Last Name" ('lastName' by default)
| **phone-number-prop-name** - Mapper field name for "Phone Number" ('phoneNumber' by default)

SSO SAML2 Configuration (app.sso.saml)
========================================================

| **entity-id** - ID of the Service Provider (should be {whitedoc_backend_url}/saml/metadata)
| **idp-metadata** - URL to Identity Provider metadata or Path to metadata file
| **max-authentication-age-sec** - Sets maximum time between users authentication and processing of an authentication statement (1 week by default)
| **keystore.location** - Path to JKS file with signing certificate
| **keystore.alias** - Alias of the certificate
| **keystore.password** - Password of the certificate

| **FYI**
| Each property can be set via ENVIRONMENT property by replacing '.' with '_' and in upper case, see examples:
| APP_SSO_ENABLED=true
| APP_SSO_FIRST-NAME-PROP-NAME=givenname

How to set up IdP SSO
========================================================

* Create new SAML application on IdP
* Set ACS URL {whitedoc_backend_url}/saml/SSO
* Set Entity ID {whitedoc_backend_url}/saml/metadata
* Set Sign Assertion = true
* Set Name ID format = EMAIL
* Add attribute mappings for First and Last names
* Copy IdP Metadata URL or the xml file and set to {app.sso.saml.idp-metadata}
