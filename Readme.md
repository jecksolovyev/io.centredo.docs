# WhiteDoc documentation manual 

## Installation of the required sources

### Windows

1. Install latest version of Python from https://www.python.org/downloads/
2. Update pip to latest version: `python -m pip install --upgrade`
3. Install latest version of Setuptools: `pip install -U setuptools`
4. Install dependencies from requirements file: `pip install -r requirements.txt`
5. Update Sphinx to the latest version: `pip install -U sphinx`

### Linnux

1. Update all packages: `sudo apt update && sudo apt upgrade -y`
2. Install pip: `sudo apt install python3-pip`
3. Install latest version of Setuptools: `sudo pip install -U setuptools`
4. Install dependencies from requirements file: `sudo pip install -r requirements.txt`
5. Update Sphinx to the latest version: `sudo pip install -U sphinx`

You will have everything ready after this. To build a local copy of documentation with your latest updates run next command from /docs folder: `make html`

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
