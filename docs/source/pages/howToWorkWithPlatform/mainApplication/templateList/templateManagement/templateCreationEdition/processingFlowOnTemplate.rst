.. _processing-flow:

===============================================
What is processing flow and how to configure it
===============================================

.. toctree::


Processing flow it's an order of the lifecycle of the envelope. According to it in processing flow you can configure how to recipients will get envelope and in which sequences.
There are three types of the sequences: parallel, consistent and serial-parallel

1. Parallel flow it's AUTO mode of the flow when system make configuration of the flow by scripted rule and participants of flow receive envelope parallel and according to the role type

2. Consistent flow it's MANUAL mode of the flow when customer click on checkbox "Set order" and configure roles according to his requirements of the flow

3. Serial-parallel flow it's also MANUAL mode, but with a couple of roles with similar order

Role configuration interface
============================

Role configuration interface for AUTO flow contain the following information:

.. image:: pic_templateCreationEdition/processingFlowForm.png
   :width: 400
   :align: center

1. Role order - order of the role in the list (Available only if checkbox "Set order" set)

2. Role name - name which has been displayed for customers in template and in envelope. It's obligatory field

3. Role mailbox - mailbox of the role to which envelope will be send. Optional to fill in template, but obligatory in envelope

.. warning:: **If you fill in mailbox field for role in template it can't be changed in envelope**

4. Role type - type of role and according to the type user will be obligated to make some actions in envelope

.. warning:: **There are thee role types: Assignee, EDS signer and Copy only**

Assignee role type
==================

Assignee role it's a role which has to fill in fields in envelope or sign document electronic signature if necessary
Assignee role has to have at least one field in at least one document of the template

Order of the assignee role in the flow should be lower than order of EDS signer

EDS signer
==========

EDS signer role it's a role which has to sign document with Advanced or Qualified electronic signature
EDs signer role has to have at least one EDS field in at least one document of the template. EDS signer role can't have two EDS fields for one document

Order of the EDS signer role in the flow should be greater than order of assignee

Copy only
=========

Copy only role just receive copy of envelope and can't have fields in document

Copy only role can be set at any place of the processing flow, but not earlier than Sender


AUTO flow
=========

In AUTO flow system configure processing flow fy the following rule:

1. Assignee adds after Sender or last Assignee (if Assignee has been already added to the flow) and before EDS signer

2. EDS signer adds after Assignee (if Assignee has been already added to the flow) and before first Copy only (if Copy only has been already added to the flow). EDS signer adds after Sender if Assignee role has not added.

3. Copy only adds after last EDS signer (if EDS signer has been already added to the flow) or after last Assignee (if Assignee has been already added to the flow and EDS singer has not added), or after Sender if no role except sender added.

MANUAL flow
===========

Logic of addition roles to the flow similar to AUTO flow, but user can change the order.
To change the order user has to set checkbox "Set order" and set order using drag and drop option for roles or edit order manually.

Some restrictions of the role places in the flow:

1. Assignee cannot have order in the flow higher than first EDS signer

2. EDS signer cannot have order lower than last Assignee

3. Copy can have any order in the flow but not less than 1

