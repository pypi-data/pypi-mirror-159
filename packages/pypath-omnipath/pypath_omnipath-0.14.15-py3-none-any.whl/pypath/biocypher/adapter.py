#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a module to exemplarise an adapter class used in creating a 
BioCypher-compatible graph database from pypath objects. It is called from
the "create_and_update_db.py" script in this directory.

Copyright 2021, Heidelberg University Clinic

File author(s): Dénes Türei
                Sebastian Lobentanzer
                ...

Distributed under GPLv3 license, see LICENSE.txt.
"""


import os
import yaml
import importlib as imp

import biocypher

import pypath.core.network as pypath_network
import pypath.resources.network as pypath_netres
import pypath.share.session as _session


class BiocypherAdapter(_session.Logger):
    """
    The connection can be defined in three ways:
        * Providing a ready ``neo4j.Driver`` instance
        * By URI and authentication data
        * By a YML config file

    Args:
        driver (neo4j.Driver): A ``neo4j.Driver`` instance, created by,
            for example, ``neo4j.GraphDatabase.driver``.
        db_name (str): Name of the database (Neo4j graph) to use.
        db_uri (str): Protocol, host and port to access the Neo4j server.
        db_auth (tuple): Neo4j server authentication data: tuple of user
            name and password.
        config_file (str): Path to a YML config file which provides the URI,
            user name and password.
        network (pypath.core.network.Network): A network database object.
        wipe (bool): Wipe the database after connection, ensuring the data
            is loaded into an empty database.
    """


    def __init__(
        self,
        driver = None,
        db_name = None,
        db_uri = 'neo4j://localhost:7687',
        db_user = None,
        db_passwd = None,
        wipe = False,
        offline = False,
        network = None,
    ):

        _session.Logger.__init__(self, name = 'bcy_adapter')

        self.bcy = biocypher.Driver(
            driver = driver,
            db_name = db_name,
            db_uri = db_uri,
            db_user = db_user,
            db_passwd = db_passwd,
            wipe=wipe,
            offline=offline,
        )

        if network:

            self.set_network(network)


    def reload(self):
        """
        Reloads the object from the module level.
        """

        modname = self.__class__.__module__
        mod = __import__(modname, fromlist = [modname.split('.')[0]])
        imp.reload(mod)
        new = getattr(mod, self.__class__.__name__)
        setattr(self, '__class__', new)


    def set_network(self, network):

        self._log('Added new network.')
        self.network = network


    def build_python_object(self):
        """
        Builds a network database with two datasets: 'pathway' and
        'mirna_target'. Intended to be an example. The dataset is preloaded
        to avoid waiting time when applying multiple database tests.
        The resulting network database is stored under the :py:attr:`network`
        attribute.
        """

        n = pypath_network.Network()

        # load single pypath network components
        # TODO which are the ones representing the "entire" pypath?
        exclude = {'TRIP', 'CellChatDB', 'ncRDeathDB', 'DIP', 'Wojtowicz2020'}
        
        n.load(pypath_netres.pathway, exclude=exclude)
        # i want to exclude the ones that make trouble. why is the name not
        # the same as the designation in the output? where can one get all 
        # the names in a convenient manner? eg, the name of 'trip' is 'TRIP',
        # but I needed to go through several modules of code to find out.

        # another question: how do I know which netres objects are relevant?
        # -> omnipath/builtins.json & classes.json

        n.load(pypath_netres.mirna_target, exclude=exclude)
        # n.load(pypath_netres.interaction, exclude=exclude)
        # n.load(pypath_netres.ligand_receptor, exclude=exclude)

        self.set_network(n)


    def translate_python_object_to_neo4j(self, network = None):
        """
        Loads a pypath network into the biocypher (Neo4j) backend.

        Args:
            - network (pypath.core.network.Network): A network database 
              object. If `None`, the value of :py:attr:`network` will be 
              used.
        """

        network = network or self.network

        if not network:

            self._log('No network provided.')
            return

        # create id-type tuples for nodes
        # to enable translation between pypath and biocypher notation
        # TODO: other node properties (as dict?)
        def gen_nodes(nodes):
            for n in nodes:
                _id = self._process_id(n.identifier)
                _type = n.entity_type
                _props = {"taxon": n.taxon}
                yield (_id, _type, _props)
        id_type_tuples = gen_nodes(network.nodes.values())
        self.bcy.add_nodes(id_type_tuples)

        # create id-type tuples for edges
        # to enable translation between pypath and biocypher notation
        # TODO: other edge properties (as dict?)
        def gen_edges(edges):
            for e in edges:
                _src = self._process_id(e.id_a)
                _tar = self._process_id(e.id_b)
                _type = e.type
                yield (_src, _tar, _type)
        src_tar_type_tuples = gen_edges(network.generate_df_records())
        self.bcy.add_edges(src_tar_type_tuples)


    def write_to_csv_for_admin_import(self, network = None, db_name=None):
        """
        Loads a pypath network into the biocypher (Neo4j) backend using
        the fast Admin Import function, which requires text files that 
        need to be properly formatted since it turns off safety measures
        at import.

        Args:
            - network (pypath.core.network.Network): A network database 
              object. If `None`, the value of :py:attr:`network` will be 
              used.
        """

        network = network or self.network

        if not network:
            self._log("No network provided.")
            return

        # write nodes
        def gen_nodes(nodes):
            for n in nodes:
                _id = self._process_id(n.identifier)
                _type = n.entity_type
                _props = {"taxon": n.taxon, "label": n.label}
                yield (_id, _type, _props)
        id_type_tuples = gen_nodes(network.nodes.values())

        self.bcy.write_nodes(id_type_tuples, db_name=db_name)

        # write edges
        def gen_edges(edges):
            for e in edges:
                _src = self._process_id(e.id_a)
                _tar = self._process_id(e.id_b)
                _type = e.type
                _props = {"effect": e.effect, "directed": e.directed}
                yield (_src, _tar, _type, _props)
        src_tar_type_tuples = gen_edges(network.generate_df_records())

        self.bcy.write_edges(src_tar_type_tuples, db_name=db_name)

        self.bcy.write_import_call()


    def _process_id(self, identifier):
        """
        Replace critical symbols in pypath ids so that neo4j doesn't throw
        a type error.
        """
        return str(identifier).replace('COMPLEX:', 'COMPLEX_')


    def load(self, obj):
        """
        Loads any compatible object into the biocypher (Neo4j) database.

        Args:
            obj: An object from this module compatible with the current
                adapter. Currently the following database objects are
                supported:
                    * :py:class:`pypath.core.network.Network`
        """

        if hasattr(obj, 'nodes') and hasattr(obj, 'interactions'):

            self.translate_python_object_to_neo4j(network = obj)
