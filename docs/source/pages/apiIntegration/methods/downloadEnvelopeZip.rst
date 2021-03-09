============
Download ZIP
============

.. toctree::

Each customer who has access to envelope can download it. Customer can download full envelope or specific document from this envelope.


For download zip customer should send next api request.

.. csv-table::
  :file: downloadZip.csv
  :widths:  10, 41

Depends on query parameter customer can control what he will download:

1. Send request without query parameter - download full envelope(all documents which contain envelope)
2. Send request with documentID in query parameter - download only document which specified in query parameter


In response will be send zip archive with documents