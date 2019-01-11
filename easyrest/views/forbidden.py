"""This module describes 403 page controller which will be triggered
when HTTPForbidden exception is raised.
It sends json with error title and error message in error field.
"""

from pyramid.view import forbidden_view_config

from ..scripts.json_helpers import wrap


@forbidden_view_config(renderer='json')
def forbidden_view(error, request):
    """
    Overrided forbidden view for adding specific information to it.
    :param error: object represents error
    :param request: standard Pyramid request object
    :return: dictionary
    """
    return wrap([], False, "%s: %s" % (error.title, error.args[0]))
