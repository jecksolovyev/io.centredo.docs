===================
FTPS/SFTP protocols
===================

Server structure
================

- cinbox/ - folder for incoming document, with special settings
- coutbox/ - folder for outgoing documents, with special settings
- error/ - folder for document which can't be processed
- inbox/ - folder for incoming document
- outbox/ - folder for outgoing documents

Connection properties
=====================
To connect FTP server customer should use autogenerated credential from integration page **/admin/integrations/list**

#. Login
#. Password
#. Host
#. Port

Notes for using
===============

Customer can use different data exchange formats. If customer used WD data exchange format he should use /inbox and /outbox as a working folders, when he used different format as working folder should be /cinbox and /coutbox.
