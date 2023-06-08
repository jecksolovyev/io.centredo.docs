===========
API methods
===========

.. hint:: All api requests will be send to: https://api.platform_address_here

Authorization endpoints
=======================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - POST
     - ``api/login``
     - `Authorization <methods/authorization.html>`__

Template endpoints
==================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - POST
     - ``/api/v1/template``
     - `Create template <methods/templateCreation.html>`__

Envelope endpoints
==================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - PUT
     - ``/api/v1/envelope/send``
     - `Fill envelope <methods/envelopeFill.html>`__
   * - POST
     - ``/api/v1/envelope/send``
     - `Send envelope <methods/envelopeSend.html>`__
   * - POST
     - ``/api/v1/envelope/attachment``
     - `Upload attachment or external documents <methods/uploadAttachment.html>`__
   * - GET
     - ``/api/v1/envelope/{envelopeUuid}/for-sign``
     - `Get document(s) for sign <methods/documentsForSign.html>`__
   * - GET
     - ``/api/v1/envelope/{envelopeUuid}/sign``
     - `Sign document(s) in envelope <methods/signDocument.html>`__
   * - GET
     - ``/api/v1/envelope/{envelopeUuid}/zip``
     - `Download documents <methods/downloadEnvelopeZip.html>`__
   * - POST
     - ``/api/v1/envelope/{envelopeUuid}/for-print``
     - `Get document for print. Document should be completed. <openapi/authApi.html#operation/getDocumentPrintVersionUsingGET>`__

Audit trail endpoints
=====================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - PUT
     - ``/api/v1/audittrail/envelope/{uuid}``
     - `Create audit trail record <methods/auditTrailEntryCreate.html>`__
   * - GET
     - ``/api/v1/audittrail/envelope/{uuid}``
     - `Get envelope audit trail <methods/auditTrailGetByEnvelope.html>`__
   * - GET
     - ``/api/v1/audittrail/pdf/{uuid}``
     - `Export envelope audit trail PDF file <methods/auditTrailDownloadPdf.html>`__

Mailbox endpoints
=================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - GET
     - ``/api/v1/mailbox/search``
     - `Search mailbox <methods/searchMailbox.html>`__
   * - GET
     - ``/api/v1/mailbox/{uuid}``
     - `Check envelope status <methods/checkEnvelopeStatus.html>`__

Account endpoints
=================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - POST
     - ``/api/v1/account/{accountUuid}/domain``
     - `Add new account domain <methods/account/domains.html#add-account-domain>`__
   * - PATCH
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/verify``
     - `Verify domain <methods/account/domains.html#verify-account-domain>`__
   * - PATCH
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/confirm``
     - `Confirm domain verification <methods/account/domains.html#confirm-account-domain-verification>`__
   * - PATCH
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/activate``
     - `Activate domain <methods/account/domains.html#activate-account-domain>`__
   * - PATCH
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/deactivate``
     - `Deactivate domain <methods/account/domains.html#deactivate-account-domain>`__
   * - PATCH
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}/check``
     - `Check domain <methods/account/domains.html#check-account-domain>`__
   * - DELETE
     - ``/api/v1/account/{accountUuid}/domain/{domainUuid}``
     - `Delete domain <methods/account/domains.html#delete-account-domain>`__
   * - GET
     - ``/api/v1/account/{accountUuid}/domain``
     - `Search domains <methods/account/domains.html#search-account-domains>`__
   * - GET
     - ``/api/v1/account/{accountUuid}/users/example``
     - `Get example file <methods/account/users.html#download-example-file>`__
   * - POST
     - ``/api/v1/account/{accountUuid}/users``
     - `Mass create users <methods/account/users.html#mass-create-users>`__

User/Profile endpoints
======================

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - Method
     - URL
     - Description
   * - POST
     - ``/api/v1/account/{accountUuid}/user``
     - `Create new corporate user in domain which has to be verified and activated. <newtab::openapi/authApi.html#operation/createCorporateUserUsingPOST>`__
   * - DELETE
     - ``/api/v1/account/{accountUuid}/user``
     - `Account admin can delete many corporate users at once. In case of exception, no user will be deleted. <newtab::openapi/authApi.html#operation/deleteCorporateUsersUsingDELETE>`__

.. toctree::

   methods/authorization.rst
   methods/templateCreation.rst
   methods/envelopeFill.rst
   methods/envelopeSend.rst
   methods/uploadAttachment.rst
   methods/documentsForSign.rst
   methods/signDocument.rst
   methods/downloadEnvelopeZip.rst
   methods/auditTrailGetByEnvelope.rst
   methods/auditTrailEntryCreate.rst
   methods/auditTrailDownloadPdf.rst
   methods/searchMailbox.rst
   methods/checkEnvelopeStatus.rst
   methods/account/users.rst
   methods/account/domains.rst