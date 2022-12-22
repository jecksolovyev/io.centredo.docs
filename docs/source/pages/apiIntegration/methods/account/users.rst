=======================
Account corporate users
=======================

.. toctree::

.. role:: red

Account can have corporate users, which belongs to account's domain names. Before you can create multiple users you should download a file example, make changes in it and upload after that.


1. Download example file
========================

Returns example XLSX binary with all available roles, permissions and mailboxes for account.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - GET
   * - Request URL
     - ``/api/v1/account/{accountUuid}/users/example``
   * - **Headers**
     -
   * - Authorization :red:`*`
     - Bearer TOKEN
   * - **Request**
     -
   * - accountUuid :red:`*`
     - Target account UUID

2. Mass create users
====================

Receives XLSX file and create users with permissions. Will return 200 if OK.

.. list-table::
   :widths: 1 99
   :header-rows: 1

   * - Endpoint
     -
   * - Method
     - POST
   * - Request URL
     - ``/api/v1/account/{accountUuid}/users``
   * - **Headers**
     -
   * - Authorization :red:`*`
     - Bearer TOKEN
   * - Content-Type :red:`*`
     - multipart/form-data
   * - **Request**
     -
   * - accountUuid :red:`*`
     - Target account UUID
   * - Body :red:`*`
     - XLSX binary