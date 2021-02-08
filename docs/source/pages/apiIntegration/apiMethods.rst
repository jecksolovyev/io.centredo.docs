===========
API methods
===========

.. toctree::


.. hint::
    All api requests will be send to: https://api.centredo.com/

Authorization
=============
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**         |                                            **Description**                                      |
+===========+===============================+=================================================================================================+
| POST      | ``api/login``                 | `Authorization <methods/authorization.html>`__                                                  |
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+


How to send envelope
====================

+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
|**Method** |       **Request URL**                           |                          **Description**                                      |
+===========+=================================================+===============================================================================+
| POST      | ``/api/v1/template``                            | `Create template <methods/templateCreation.html>`__                           |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| GET       | ``/api/v1/mailbox/search``                      | `Search mailbox <methods/searchMailbox.html>`__                               |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| POST      | ``/api/v1/envelope/send``                       | `Send envelope <methods/envelopeSend.html>`__                                 |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| GET       | ``/api/v1/mailbox/{uuid}``                      | `Check envelope status <methods/checkEnvelopeStatus.html>`__                  |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| GET       | ``/api/v1/envelope/{envelopeUuid}/zip``         | `Download documents <methods/downloadEnvelopeZip.html>`__                     |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| GET       | ``/api/v1/envelope/{envelopeUuid}/for-sign``    | `Get document(s) for sign <methods/documentsForSign.html>`__                  |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+
| GET       | ``/api/v1/envelope/{envelopeUuid}/sign``        | `Sign document(s) in envelope <methods/signDocument.html>`__                  |
+-----------+-------------------------------------------------+-------------------------------------------------------------------------------+



Create template
===============

+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**         |                                           **Description**                                       |
+===========+===============================+=================================================================================================+
| POST      | ``/api/v1/template``          | `Create template <methods/templateCreation.html>`__                                             |
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+


Search mailbox
==============

+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **URL запиту**          |                                           **Description**                                       |
+===========+===============================+=================================================================================================+
| GET       | ``/api/v1/mailbox/search``    | `Search mailbox <methods/searchMailbox.html>`__                                                 |
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+


Upload attachment or external document
======================================

+-----------+---------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **URL запиту**            |                                           **Description**                                       |
+===========+=================================+=================================================================================================+
| POST      | ``/api/v1/envelope/attachment`` | `Upload attachment or external documents <methods/uploadAttachment.html>`__                     |
+-----------+---------------------------------+-------------------------------------------------------------------------------------------------+

Send envelope
=============

+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**         |                                           **Description**                                       |
+===========+===============================+=================================================================================================+
| POST      | ``/api/v1/envelope/send``     | `Send envelope <methods/envelopeSend.html>`__                                                   |
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+

Check envelope status
=====================

+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+
|**Method** |       **Request URL**         |                                           **Description**                                       |
+===========+===============================+=================================================================================================+
| GET       | ``/api/v1/mailbox/{uuid}``    | `Check envelope status <methods/checkEnvelopeStatus.html>`__                                    |
+-----------+-------------------------------+-------------------------------------------------------------------------------------------------+

Account
=====================

.. list-table::
   :widths: 1 1 98
   :header-rows: 1

   * - Method
     - Request URL
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

User/Profile
=====================

.. list-table::
   :widths: 1 1 98
   :header-rows: 1

   * - Method
     - Request URL
     - Description
   * - POST
     - `/api/v1/account/{accountUuid}/user <openapi/authApi.html#operation/createCorporateUserUsingPOST>`__
     - Create new corporate user in domain which has to be verified and activated.
   * - DELETE
     - `/api/v1/account/{accountUuid}/user <openapi/authApi.html#operation/deleteCorporateUsersUsingDELETE>`__
     - Account admin can delete many corporate users at once. In case of exception, no user will be deleted.
User/Profile
=====================

.. list-table::
   :widths: 1 1 98
   :header-rows: 1

   * - Method
     - Request URL
     - Description
   * - POST
     - ``/api/v1/user/domain``
     - `Create new corporate user <methods/user/userManagement.html#create-corporate-user>`__
   * - DELETE
     - ``/api/v1/user/domain``
     - `Delete corporate users <methods/user/userManagement.html#delete-corporate-users>`__
