# ============================================================================
__author__          =   'Manuel Nielsen'
__copyright__       =   'Copyright - The RODE Project'
__credits__         =   ['Manuel Nielsen']
__license__         =   'Proprietary and Confidential'
__maintainer__      =   'Manuel.Nielsen@health.nsw.gov.au'
# ============================================================================
# IMPORT PACKAGES
# ============================================================================
import falcon
# ============================================================================
# DEFINE MIDDLEWARE
# ============================================================================
# This class inherits all the features of the classes.Core object. 
#
# This middleware object is designed to return the initial CORS request that 
# allows for querying from systems with a different domain name entry.
class CORS:
    # The initialisation method of the object. This will be called
    # when a new instance of the class if created. 
    def __init__(
        # The instance of the object that is being created.
        self: type, 
        # The environment stage of the Resource object. If left empty it 
        # defaults to the STAGE environment variable.
        stage: str | None = None
    # This method does not return any value.
    ) -> None:
        # Initiate the class by running the parent __init__ method.
        self.STAGE: str = stage
    # Process request before routing.
    async def process_request_async(
        # The instance of the object that has been created.
        self: type, 
        # The instance of the falcon.request object. This is scoped to each 
        # individual request.
        req: type, 
        # The instance of the falcon.response object. This is scoped to each 
        # individual request.
        resp: type
    # This method does not return a value.
    ) -> None:
        # Set the CORS response headers.
        resp.set_headers({
            # This header allows requests to services to originate from 
            # anywhere. The security for the application is managed within the 
            # request processes.
            'Access-Control-Allow-Origin': '*',
            # This header specifies which http methods are allowed to be 
            # routed.
            'Access-Control-Allow-Methods':
                'GET,POST,PUT,PATCH,OPTIONS,DELETE',
            # This header specifies which http headers are allowed when 
            # routing.
            'Access-Control-Allow-Headers': '*'
        })
        # Return response 200 if method is OPTIONS for CORS test.
        if req.method == 'OPTIONS': 
            # This shortcuts the application routing and will go straight to 
            # processing the response.
            raise falcon.http_status.HTTPStatus(
                # The status code to return.
                falcon.HTTP_200
            )