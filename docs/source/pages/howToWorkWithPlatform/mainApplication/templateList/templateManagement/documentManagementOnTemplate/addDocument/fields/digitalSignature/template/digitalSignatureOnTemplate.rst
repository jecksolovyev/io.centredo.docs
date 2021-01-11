=============================
Digital signature on template
=============================

.. toctree::

---------

Digital signature it's a field with specific role relation which can be added to the document. You may add one digital signature field to the one document 
for one signer role.

How to add signer role
======================

To add signature role to the template follow the instructions:

1. Press button "Add signer" and new section with "Signers" appeares;
2. Fill the required field "Role" with role details (f.e.: name of the role);
3. Confirm addition.

As soon as you did the steps above you can add document and add the field "EDS" to the document.

Which actions we can do with signature roles?
=============================================

Signer flow is definetly similar to the Assignee flow. You can make similar actions with Signer flow as with Asignee flow except set a role as a copy.
So, you can do the following:

1. Add or remove role from the flow;
2. Add default mailbox as a role;
3. Set the order of the signers. You can set order or left it as default and all signers receive the document at the same time.

You can add as many signers as you need but we support only 30 recipients in the flow, including the assignee roles.

Digital signature addition to the document
==========================================

To use the digital signature on the document you have to add signer role. You may add only one digital signature for one role on the one document.

You can add EDS field to any document in envelope. To do this:

1. Drag and drop the field to the document;
2. Set unique field name;
3. Select the role of the signer who has to set a signature;
4. Set the placeholder if needed (this placeholder will be shown on the template/envelope)

On the template new block above document appeares. You will see the block "Required signatures" with signatures.

.. image:: pic_digitalSignature/signatureOnTemplate.png
   :width: 400
   :align: center

Digital signature removing from the document
============================================

You can remove digital signature from the document in two ways:

1. Using field menu. Click on the button and in the right bottom corner, click on the "Delete" button;
2. You may delete the role and if it is last role in the flow the signature field deletes automatically with role.

If you delete the role with assigned digital signature field(s) you have to re-assign the field to another role if such is presented. If not role will be 
deleted with fields.

General view of the digital signature field and signer role
===========================================================

In the processing flow roles divided according to the colors palitra. Signatures on the signature block will be added according to the color in the flow.
If you change order the color of the button(s) will be changed too.

Common infromation related to signer roles
==========================================

Signers in the processing flow will be able to set signature on the envelope only when all assignees fill the document data.
