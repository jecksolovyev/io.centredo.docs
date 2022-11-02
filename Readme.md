# WhiteDoc documentation manual 

## Installation of the required sources

Before installing sphinx, you have to install Python 3+ version

### Linux

1. install pip

`sudo apt install python3-pip`

2. install requirements

`pip install -r requirements.txt`

3. run command in /docs folder in order to generate HTML

`make html`


### Windows

Most Windows users do not have Python installed by default, so we begin with the installation of Python itself. To check 
if you already have Python installed, open the Command Prompt (⊞Win-r and type cmd). Once the command prompt is open, 
type python --version and press Enter. If Python is installed, you will see the version of Python printed to the screen. 
If you do not have Python installed, refer to the Hitchhikers Guide to Python’s Python on Windows installation guides. 
**You must install Python 3**.

Once Python is installed, you can install Sphinx using pip.

1. install requirements

`pip install -r requirements.txt`

2. run command in /docs folder in order to generate HTML

`make html`


## Documentation creation rules

When we want to create new documentation page we have to follow the heirarchy functionality in documentation. 

So, if we want to create documentation related to customer authorization on platform we have to create file with 
extension .rst in docs/source/pages/howToWorkWithPlatform/authorization/login folder.

After file creation we have to link it with head file of the folder (according to example it would be 
docs/source/pages/howToWorkWithPlatform/authorization/autorization.rst). 

To create link head file with child files we 
have to add to head file link to child file. It could be done two ways:

1. Link it directly within ref functionality

```
:ref:`log in <login>`
```

2. Add link to file within toctree functionality 

```
.. toctree::

pages/howToWorkWithPlatform/howToWorkWithPlatform.rst
pages/apiIntegration/apiIntegration.rst
pages/errorCodes/errorCodes.rst
pages/configuration/server.rst
```

As soon as files linked we could start fill in content of the documentation page. To fill documentation we have to use 
markdown which presented in sphinx documentation https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html.
