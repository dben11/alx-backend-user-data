#!/usr/bin/env python3
"""Basic auth class"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """_summary_
    """

    def extract_base64_authorization_header(
	    self, authorization_header, str) -> str:
	"""_summary_

	Args:
		str: _description_

	Returns:
		str:_description_
	"""
	if authorization_header is None:
	    return None
	if not isinstance(authorization_header, str):
	    return None
	if not authorization_header.startswith("Basics"):
	    return None
	else:
	    return authorization_header.split(' ')[1]
