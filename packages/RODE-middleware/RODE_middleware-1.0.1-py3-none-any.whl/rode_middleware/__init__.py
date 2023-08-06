# ============================================================================
__author__          =   'Manuel Nielsen'
__copyright__       =   'Copyright - The RODE Project'
__credits__         =   ['Manuel Nielsen']
__license__         =   'Proprietary and Confidential'
__maintainer__      =   'Manuel.Nielsen@health.nsw.gov.au'
# ============================================================================
# IMPORT MIDDLEWARE
# ============================================================================
from .CORS import CORS
from .ProcessResponse import ProcessResponse
from .Logging import Logging
# ============================================================================
# SET MIDDLEWARE
# ============================================================================
# This method will return the list of middleware class instances to be applied 
# into the falcon.asgi.App in the asgi.py file.
def setMiddleware(
    # The environment stage of the Resource object. If left empty it defaults 
    # to the STAGE environment variable.
    stage: str | None = None
# This method returns a list of middleware class objects.
) -> list:
    # Return the middleware class instances list.
    return [ 
        # Initiate the CORS middleware. This will handle options requests by 
        # short circuiting the routing and return the required headers for 
        # CORS scripting.
        CORS(stage), 
        # This method will process the falcon response body from the falcon 
        # request.context contents.
        ProcessResponse(stage),
        # The logging middleware will append the request details to the log 
        # files if the environment stage is production.
        Logging(stage)
    ]