# Getting started with PyCaosDB #

## Installation ##

### Requirements ###

PyCaosDB needs at least Python 3.8.  Additionally, the following packages are required (they will
typically be installed automatically):

- `lxml`
- `PyYaml`
- `PySocks`

Optional packages:
- `keyring`
- `jsonschema`

### How to install ###

#### Linux ####

Make sure that Python (at least version 3.8) and pip is installed, using your system tools and
documentation.

Then open a terminal and continue in the [Generic installation](#generic-installation) section.

#### Windows ####

If a Python distribution is not yet installed, we recommend Anaconda Python, which you can download
for free from [https://www.anaconda.com](https://www.anaconda.com).  The "Anaconda Individual Edition" provides most of all
packages you will ever need out of the box.  If you prefer, you may also install the leaner
"Miniconda" installer, which allows you to install packages as you need them.

After installation, open an Anaconda prompt from the Windows menu and continue in the [Generic
installation](#generic-installation) section.

#### MacOS ####

If there is no Python 3 installed yet, there are two main ways to
obtain it: Either get the binary package from
[python.org](https://www.python.org/downloads/) or, for advanced
users, install via [Homebrew](https://brew.sh/). After installation
from python.org, it is recommended to also update the TLS certificates
for Python (this requires administrator rights for your user):

```sh
# Replace this with your Python version number:
cd /Applications/Python\ 3.9/

# This needs administrator rights:
sudo ./Install\ Certificates.command
```

After these steps, you may continue with the [Generic
installation](#generic-installation).

#### Generic installation ####

To install PyCaosDB locally, use `pip3` (also called `pip` on some systems):

```sh
pip3 install --user caosdb
```

---

Alternatively, obtain the sources from GitLab and install from there (`git` must be installed for
this option):

```sh
git clone https://gitlab.com/caosdb/caosdb-pylib
cd caosdb-pylib
pip3 install --user .
```

For installation of optional packages, install with an additional option, e.g. for 
validating with the caosdb json schema:

```sh
pip3 install --user .[jsonschema]
```

## Configuration ##

The configuration is done using `ini` configuration files.  The content of these configuration files
is described in detail in the [configuration section of the documentation](https://docs.indiscale.com/caosdb-pylib/configuration.html).

## Try it out ##

Start Python and check whether the you can access the database. (You will be asked for the
password):

```python
In [1]: import caosdb as db
In [2]: db.Info()
Please enter the password:  # It's `caosdb` for the demo server.
Out[2]: Connection to CaosDB with 501 Records.
```

Note: This setup will ask you for your password whenever a new connection is created. If you do not
like this, check out the "Authentication" section in the [configuration documentation](configuration.md).

Now would be a good time to continue with the [tutorials](tutorials/index).

## Run Unit Tests

- Run all tests: `tox` or `make unittest`
- Run a specific test file: e.g. `tox -- unittests/test_schema.py`
- Run a specific test function: e.g. `tox -- unittests/test_schema.py::test_config_files`

## Documentation ##

Build documentation in `build/` with `make doc`.

### Requirements ###

- `sphinx`
- `sphinx-autoapi`
- `recommonmark`

### Troubleshooting ###
If the client is to be executed directly from the `/src` folder, an initial `.\setup.py install --user` must be called.
