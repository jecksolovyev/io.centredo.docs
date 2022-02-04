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

SSO SAML2 Identity Provider configuration (app.sso.saml)
========================================================

| **sp-name** - Name of the Service Provider for WhiteDoc on IdP side
| **idp-metadata-url** - URL to Identity Provider metadata
| **keystore.location** - Path to JKS file with signing certificate
| **keystore.alias** - Alias of the certificate
| **keystore.password** - Password of the certificate

| **FYI**
| Each property can be set via ENVIRONMENT property by replacing '.' with '_' and in upper case, see examples:
| APP_SSO_ENABLED=true
| APP_SSO_FIRST-NAME-PROP-NAME=givenName
