===================================
Invitation to the envelope by email
===================================

.. toctree::

---------

It's possible to invite participant of the envelope flow by email. Participants which invited by email have to follow the envelope invitation link from email.

Invite participant to envelope by email from the draft page
===========================================================

* Open draft of the envelope without predefined processing flow and participant there
* To the input of the particular role enter the participant email address (you're able to left the email address and don't choose the mailbox from drop-down list)
* After completion of the envelope configuration you're able to send envelope
* At the modal window you will see the alert message which says that you try to send envelope to email
* Just confirm and envelope will be send

Invite participant to envelope by email from the template management page
=========================================================================

* Open template management page of the particular template
* Open roles edition form
* Set the email to the input and apply changes

States of the envelope with invitation
======================================

Until participant doesn't do any action with invitation envelope stack at the step of the processing flow with particular role.
Envelope which has been sent directly to the email could be finished in three cases:

* If participant accept invitation to the envelope processing flow and complete or reject envelope
* If participant doesn't accept invitation than envelope follow to the expired state after expiration date
* If sender or somebody from the processing flow reject the envelope

Participants which could be invited to an envelope
==================================================

We're able to invite to an envelope such as customers of the platform and non-registered users. The one difference is flow of the envelope invitation acceptence.

* If you leave the email address at the input at the processing flow, participant will be invited by email
* If you select the mailbox from the drop-down list at the processing flow, participant will get envelope as usual

Auto Deposit Function
=====================

The envelope sent by email can be assigned to mailbox automatically with Auto Deposit function.

* Open 'User Profile'
* Select proper mailbox in 'Auto Deposit Mailbox'
* All envelopes will go to this mailbox automatically without invitations
* By default 'Auto Deposit Mailbox' is set to user's personal mailbox
