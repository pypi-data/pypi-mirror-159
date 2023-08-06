Installation
------------

Requirements:

* Python 3.8+
* `RDKit <https://www.rdkit.org/docs/>`_ (2020.03+)
* `Pandas <https://pandas.pydata.org/>`_
* `NumPy <https://numpy.org/>`_
* `sklearn <https://scikit-learn.org/stable/>`_
* `tqdm <https://tqdm.github.io/>`_
* `CReM <https://github.com/DrrDom/crem>`_ (0.2.9+)
* `OpenBabel <https://openbabel.org/docs/dev/Installation/install.html>`_ (3.1.0+)

.. note::

    If you have OpenBabel and RDKit already installed you could try with ``conda install moldrug``.
    But if it is not the case or some version conflicts occurred, think about installed in a isoleated enviroment
    as it will be show in brief.
    

It is recomendable to install through ``conda``::

    $ conda create -n moldrug
    $ conda activate moldrug
    $ conda install -c ale94mleon -c conda-forge -c bioconda moldrug

.. warning::

    Ussually pip has the lates stable version. But we are working to constantlly update the conda packege.
    Future plans are deployed inside conda-forge.

Another possible way is direclly install from pip. But in this case you must have a correct installation
of OpenBabel, RDKit and autodock-vina. One posibility is::

    $ conda create -n moldrug
    $ conda activate moldrug

Then install the dependencies libraries::

    conda install -y -c conda-forge rdkit">=2022.0"
    conda install -y -c conda-forge openbabel">=3.1.0"
    conda install -y -c bioconda autodock-vina

In the future we will consider to use the python modules `vina <https://pypi.org/project/vina/>`_ and `meeko <https://pypi.org/project/meeko/>`_
. Finally::

    # To get the version on developing
    pip install git+https://github.com/ale94mleon/moldrug.git@main

or::

    # To get the last "stable" version. This project is still in beta state.
    pip install moldrug
    
We are currently working in a ``docker`` container. But you could use the `Docker configuration file on GitHub <https://github.com/ale94mleon/MolDrug/blob/main/Dockerfile>`__. 
and ``pip install moldrug`` inside it.
