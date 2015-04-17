# -*- coding: utf-8 -*-
# Copyright (c) 2014 Spotify AB
import os

import six

from .errors import LoadRAMLFileError
from .loader import RAMLLoader


def load_file(raml_file):
    try:
        with _get_raml_object(raml_file) as raml:
            return RAMLLoader().load(raml)
    except IOError as e:
        raise LoadRAMLFileError(e)


def load_string(raml_str):
    return RAMLLoader().load(raml_str)


def _get_raml_object(raml_file):
    """
    Returns a file object.
    """
    if raml_file is None:
        msg = "RAML file can not be 'None'."
        raise LoadRAMLFileError(msg)

    if isinstance(raml_file, six.text_type) or isinstance(
            raml_file, bytes):
        return open(os.path.abspath(raml_file), 'r')
    elif hasattr(raml_file, 'read'):
        return raml_file
    else:
        msg = ("Can not load object '{0}': Not a basestring type or "
               "file object".format(raml_file))
        raise LoadRAMLFileError(msg)