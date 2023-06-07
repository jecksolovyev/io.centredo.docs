=========================
Sign document(s) with EDS
=========================

.. toctree::

Customer can sign document if document has signature field inside assigned to the particular customer. Using this endpoint customer sign document(s) with EDS.

Request
=======

To sign document send request to the following endpoint.

.. csv-table::
  :file: signDocument.csv
  :widths:  10, 41

Request structure example
=========================

.. code-block:: JSON

    [
        {
            "documentId": "string",
            "signatureName": "string",
            "signatures": [
                {
                    "data": "string",
                    "source": "binary",
                    "stamp": true
                }
            ]
        }
    ]


Response
========

If data in request is valid in response you will see Status code: **200 OK**.