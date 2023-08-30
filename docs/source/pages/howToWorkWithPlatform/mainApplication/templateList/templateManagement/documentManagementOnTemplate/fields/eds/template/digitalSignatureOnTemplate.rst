================================
Electronic signature on template
================================

.. toctree::

---------

Electronic signature is a field with specific role relation which can be added to the document. You may add one electronic signature field to the one document for one signer role.

Electronic signature types
==========================
We supports 3 types of electronic signature:

1. Standard electronic signature (E-ink field);
2. Advanced electronic signature (AES);
3. Qualified electronic signature (QES);

Qualified Electronic Signature is an Advanced Electronic Signature that meets additional requirements.

With a QES, a qualified certificate is needed to attest to the authenticity of an electronic signature and serve as proof of the identity of the signatory.
The signature itself must also be created using special hardware and software, known as a Qualified Signature Creation Device (QSCD). This ensures that:

1. The signatory is the only one with control of the key used to create the electronic signature;
2. The signature data is managed by a Qualified Trust Service Provider (QTSP)
3. The signature data is unique and protected from forgery.

While Simple Electronic Signatures and Advanced Electronic Signatures both have their place, QES provides the strongest legal evidence when it comes to disputes over digital transactions, for example, and can help to protect both the consumer and the business against fraud.

How to add signer role
======================

To add signature role to the template follow the instructions:

1. Press button "Add signer" and new section with "Signers" appears;
2. Fill the required field "Role" with role details (f.e.: name of the role);
3. Confirm addition.

As soon as you did the steps above you can add document and add the field "EDS" to the document.

Which actions we can do with signature roles?
=============================================

Signer flow is similar to the Assignee flow. You can make similar actions with Signer flow as with Assignee flow except set a role as a copy.
So, you can do the following:

1. Add or remove role from the flow;
2. Add default mailbox as a role;
3. Set the order of the signers. You can set order or left it as default and all signers receive the document at the same time.

You can add as many signers as you need but we support only 30 recipients in the flow, including the assignee roles.

Electronic signature addition to the document
=============================================

To use the electronic signature on the document you have to add signer role. You may add only one electronic signature for one role on the one document.

You can add EDS field to any document in envelope. To do this:

1. Drag and drop the field to the document
2. Set unique field name
3. Select the role of the signer who has to set a signature
4. Set the placeholder if needed (this placeholder will be shown on the template/envelope instead of field name)
5. If you expect only qualified electronic signature you should enable "Qualified" attribute
6. If you expect a stamp in addition to the signature you should enable "Require stamp" attribute
7. If you want to specify TIN number of signer you should select "TIN" checkbox (Taxpayer Identification Number)
    7.1 "TIN" checkbox will be disabled if you don't have at least one required text, dictionary or lookup field in your template
    7.2 After selecting the checkbox you should select document where your matching field is located and select field (field should be required and have type of text, dictionary or lookup)

You will see that new "Required signatures" block will appear above the document.

.. image:: pic_digitalSignature/signatureOnTemplate.png
   :width: 400
   :align: center

Electronic signature removing from the document
===============================================

You can remove electronic signature from the document in two ways:

1. Using field menu. Click on the button and in the right bottom corner, click on the "Delete" button;
2. You may delete the role and if it is last role in the flow the signature field deletes automatically with role.

If you delete the role with assigned electronic signature field(s) you have to re-assign the field to another role if such is presented. If not role will be
deleted with fields.

General view of the electronic signature field and signer role
==============================================================

In the processing flow roles divided according to the colors palette. Signatures on the signature block will be added according to the color in the flow.
If you change order the color of the button(s) will be changed too.

Common information related to signer roles
==========================================

Signers in the processing flow will be able to set signature on the envelope only when all assignees fill the document data.
