========================
Download the signed data
========================

.. contents:: Сontent:
   :depth: 6

---------

How to download the signed data
===============================

You can download the signature(s) of the document(s) when all participant with role "Signer". You're able to download particular document with signatures or
whole envelope with all the documents inside and all signatures inside.

To do this, just :

1. Check that envelope completed;
2. Open envelope;
3. Click on respective "download" button in the header, to download the full envelope with all signed documents;
4. Or click on respective "download" button ahead document name and you will download particular document with all signatures;

As soon as you click on the document download button archive with the documents will be uploaded.


You can also download all envelopes en masse:

1. Press button "Mailbox" on the left sidebar;
2. Choose envelopes which you want to download. You can download only completed envelopes;
3. Press button "Download completed envelopes" for downloading;

.. image:: pic_download/downloadEnvelopeOnListingPage.png
   :width: 400
   :align: center

What are you downloading?
=========================

You download the archive with the zip extension.

* If you have downloaded a specific document.
Inside the archive will be a file with the extension .pdf, a file with the extension .xml, and two files with captions in .p7s format.

* If you downloaded the entire envelope.
There will be several folders inside the archive (if the envelope consists of several documents).
Folder names match document names accordingly.
Inside their folders are the above-mentioned files (pdf, xml and p7s), as well as the AuditTrail file and the signing document certificate.


The signing document certificate
================================

In The signing document certificate you can find information about the document(s) and about the signer(s).

1. Document information section contains:

* Envelope UUID
* Envelope subject
* Document ID
* Title of the document
* Date of the document - it is date of creation of envelope
* Template UUID
* Template version
* File name
* Number of signatures
* Electronic version of the document - link to the version of the document


2. Section about the signer contains:

* Owner
* Organization
* Position
* ITN - Identification code
* Certificate serial number
* Date of signing
* File name - signed file with extension
