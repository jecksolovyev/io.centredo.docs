================
Permissions list
================

.. toctree::

Permissions it's an entity which allows to user see or do some view or action. In this file you will find all permissions existed on platform.

Permissions divided on two general parts. There are account and mailbox permissions. 

* Account permissions correspond to views and functionality of admin panel.

* Mailbox permissions correspond to views and functionality of main application (such as mailbox page, tempalte, dictionary and etc.)

Account permissions
===================

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Permission name
     - Permission code
     - Description
   * - userAssignToAccount
     - 10000
     - Allows to user add permissions or roles to account
   * - userUnassignFromAccount
     - 10001
     - Allows to user remove permissions from the account and remove user from account with special functionality
   * - rolesManage
     - 10002
     - Allows to user create, clone and edit roles in particular account
   * - rolesDelete
     - 10003
     - Allows to user remove roles in particular account
   * - mailboxManage
     - 10004
     - Allows to user create and edit mailboxes in particular account
   * - mailboxArchive
     - 10005
     - ...
   * - mailboxDelete
     - 10006
     - Allows to user remove mailboxes in particular account
   * - accountManage
     - 10007
     - Allows to user manage account settings of the particular account
   * - accountDelete
     - 10008
     - Allows to user remove particular account (for which applied permissions)
   * - aliasCreate
     - 10009
     - Allows to user create and edit mailbox aliases in particular account
   * - aliasDelete
     - 10010
     - Allows to user remove mailbox aliases in particular account
   * - userAssignToMailbox
     - 10011
     - Allows to user add permissions or roles to mailboxes
   * - userUnassignFromMailbox
     - 10012
     - Allows to user remove permissions from the mailboxes and remove user from mailboxes with special functionality
   * - userListView
     - 10013
     - Allows to user view page with users list
   * - rolesListView
     - 10014
     - Allows to user view page with roles list
   * - mailboxListView
     - 10015
     - Allows to user view page with mailboxes list
   * - domainListView
     - 10100
     - Allows to user view page with domains list
   * - domainManage
     - 10101
     - Allows to user add and edit domains configuration in particular account
   * - corporateUserManage
     - 10120
     - Allows to user manage corporate users which belong to particular account
   * - accountView
     - 10130
     - Allows to user view page with account settings

Mailbox permissions
===================

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Permission name
     - Permission code
     - Description
   * - templateManage
     - 1000
     - Allows to user create, clone and edit tempaltes in particular mailbox
   * - templateArchive
     - 1001
     - Allows to user remove tempaltes in particular mailbox
   * - templateListView
     - 1002
     - Allows to user view page with templates list and elements on dashboard which related to template list (block with recently used templates)
   * - envelopeManage
     - 2000
     - Allows to user create and update drafts of the envelopes in particular mailbox
   * - envelopeSend
     - 2001
     - Allows to user send envelope drafts in particular mailbox
   * - envelopeArchive
     - 2002
     - Allows to user archive and unarchive envelopes in particular mailbox
   * - envelopeSign
     - 2003
     - Allows to user fill envelope fields including digital signatures in envelope processing flow in particular mailbox
   * - envelopeListView
     - 2004
     - Allows to user view page with envelopes list and elements on dashboard which related to envelope list (counters and wwaiting for you block)
   * - categoryManage
     - 3000
     - Allows to user create, update and move categories in particular mailbox
   * - categoryDelete
     - 3001
     - Allows to user remove categories in particular mailbox
   * - dictionaryManage
     - 5000
     - Allows to user create, update dictionaries and add, update columns in dictionaries in particular mailbox
   * - dictionaryArchive
     - 5001
     - Allows to user remove dictionaries and remove columns inside dictionary in particular mailbox
   * - dictionaryRowManage
     - 5002
     - Allows to user add and update rows inside dictionaries in particular mailbox
   * - dictionaryRowDelete
     - 5003
     - Allows to user remove rows inside dictionaries in particular mailbox
   * - dictionaryListView
     - 5004
     - Allows to user view page with dictionaries list
   * - labelManage
     - 6000
     - Allows to user create and update labels in particular mailbox
   * - labelDelete
     - 6001
     - Allows to user remove labels in particular mailbox
   * - labelAssignManage
     - 6002
     - Allows to user assign and unassign labels from envelopes in particular mailbox
   * - contactManage
     - 8000
     - Allows to create and update contacts in particular mailbox
   * - contactDelete
     - 8001
     - Allows to user remove contacts in particular mailbox
   * - contactListView
     - 8002
     - Allows to user view page with contacts list
   * - integrationView
     - 9000
     - Allows to user view page with integration list (located in admin panel)
   * - integrationManage
     - 9001
     - Allows to user configure integration and create, update and delete integration rules for particular mailbox
   * - scenarioList
     - 10000
     - Allows to user view page with scenarios list
   * - scenarioManage
     - 10001
     - Allows to user create, update, clone scenarios in particular mailbox
   * - scenarioDelete
     - 10002
     - Allows to user remove scenarios in particular mailbox
