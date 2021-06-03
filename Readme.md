# WhiteDoc official manual 

Before installing sphinx, you have to install Python 3+ version

Linux

1. install sphinx
   
`sudo apt-get install python3-sphinx`

2. install pip

`sudo apt install python3-pip`

3. install theme

`pip3 install sphinx_bootstrap_theme`

4. install plugin to generate API based on OpenAPI specs

`pip3 install sphinxcontrib-redoc`

5. run command in /docs folder in order to generate HTML

`make html`


Windows

Most Windows users do not have Python installed by default, so we begin with the installation of Python itself. To check if you already have Python installed, open the Command Prompt (⊞Win-r and type cmd). Once the command prompt is open, type python --version and press Enter. If Python is installed, you will see the version of Python printed to the screen. If you do not have Python installed, refer to the Hitchhikers Guide to Python’s Python on Windows installation guides. You must install Python 3.

Once Python is installed, you can install Sphinx using pip.

1. install sphinx

`pip install -U sphinx`

2. install theme

`pip install sphinx_bootstrap_theme`

3. install plugin to generate API based on OpenAPI specs

`pip install sphinxcontrib-redoc`

4. run command in /docs folder in order to generate HTML

`make html`

