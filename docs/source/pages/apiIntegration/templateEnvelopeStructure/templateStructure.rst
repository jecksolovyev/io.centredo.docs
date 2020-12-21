==================
Template Structure
==================

.. toctree::

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

2. Data block

.. code:: xml

   { "data": "
    <template>
        <info>
            <name>TEST TEMPLATE</name>
            <description>TEST TEMPLATE</description>
            <subject/>
            <message/>
            <expire/>
        </info>
        <documents>
            <document id="52616c26-e515-49c6-9ab4-bd088ca1fcda">
                <info>
                    <title>New Document</title>
                </info>
                <body>
                    <field type="text" name="TEST FIELD 1" roleId="f0d25c5e-e1fe-4759-8f81-ccfaeefb6eb9" placeholder="TEST FIELD 1"/>
                    <field type="text" name="TEST FIELD 2" roleId="d070cfb5-366c-466c-a9f7-986e6361ef37" placeholder="TEST FIELD 2"/>
                </body>
            </document>
        </documents>
        <flow>
            <roles>
                <role id="f0d25c5e-e1fe-4759-8f81-ccfaeefb6eb9" title="Sender" type="sender" order="0"/>
                <role id="d070cfb5-366c-466c-a9f7-986e6361ef37" title="Assignee" type="assignee" order="1"/>
            </roles>
        </flow>
    </template>"


.. csv-table::
  :file: templateStructureData.csv
  :widths:  10, 10
