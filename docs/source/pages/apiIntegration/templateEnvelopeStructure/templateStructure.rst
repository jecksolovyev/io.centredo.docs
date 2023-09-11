==================
Template Structure
==================

.. toctree::

   templateStaticElements.rst
   templateFields.rst


.. code:: json

    {
      "access": "account",
      "archive": true,
      "categories": [
        0
      ],
      "createdAt": "string",
      "data": "string",
      "dataCreatedAt": "string",
      "dataModifiedAt": "string",
      "description": "string",
      "modifiedAt": "string",
      "name": "string",
      "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "version": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }

Template consists of two blocks:

1. Template information block.

.. code:: json

    {
      "access": "account",
      "archive": true,
      "categories": [
        0
      ],
      "createdAt": "string",
      "dataCreatedAt": "string",
      "dataModifiedAt": "string",
      "description": "string",
      "modifiedAt": "string",
      "name": "string",
      "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "version": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }


.. csv-table::
  :file: templateStructure.csv
  :widths:  10, 10, 10

2. 'data' parameter is a XML

.. code:: xml

    <template>
        <info>
            <name>TEST template</name>
            <description>TEST template</description>
            <subject/>
            <message/>
            <expire/>
        </info>
        <documents>
            <document id=\"ef247568-559a-4ec1-9ecc-6b44c9fb8215\">
                <info>
                    <title>New document</title>
                </info>
                <body>
                    <div class=\"editor-div\">
                        <field type=\"text\" name=\"TEST template 1\" roleId=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" placeholder=\"TEST template 1\"/>
                        <field type=\"number\" name=\"TEST template 2\" roleId=\"3f29b3a8-3baa-4218-80b1-5a0bb85af247\" placeholder=\"TEST template 2\" precision=\"0\"/>
                    </div>
                </body>
            </document>
            <document type=\"singleAttachment\" id=\"43d47e65-011d-4890-9eaf-c1c6d860b3b2\">
                <info>
                    <title>New External Document 1</title>
                </info>
                <body>
                    <field type=\"attachment\" name=\"990f11c1-48de-4ac8-8479-a5989d5f08dc\" roleId=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" attachmentType=\"all\"/>
                </body>
            </document>
        </documents>
        <signatures>
            <signature name=\"Test signer\" roleId=\"348c486d-2901-4ecd-be0c-9a7e6c2ae2a2\" documentId=\"ef247568-559a-4ec1-9ecc-6b44c9fb8215\"/>
            <signature name=\"Test signer\" roleId=\"348c486d-2901-4ecd-be0c-9a7e6c2ae2a2\" documentId=\"43d47e65-011d-4890-9eaf-c1c6d860b3b2\"/>
        </signatures>
        <flow>
            <roles>
                <role id=\"fd8cb669-db1d-41e1-8f6c-2ad3f8fa981a\" title=\"Sender\" type=\"sender\" order=\"0\"/>
                <role id=\"3f29b3a8-3baa-4218-80b1-5a0bb85af247\" title=\"Assignee\" type=\"assignee\" order=\"1\"/>
                <role id=\"348c486d-2901-4ecd-be0c-9a7e6c2ae2a2\" title=\"Test signer\" type=\"signer\" order=\"2\"/>
            </roles>
        </flow>
    </template>

.. csv-table::
  :file: templateStructureData.csv
  :widths:  10, 10