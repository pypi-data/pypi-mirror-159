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
import json
# ============================================================================
# SET MIDDLEWARE OBJECT
# ============================================================================
# This class inherits all the features of the classes.Core object. 
#
# The Process Response middleware is responsible for creating the JSON body of 
# the response object from the Falcon response context object. It will also 
# add basic response data in the body.
class ProcessResponse:
    # The initialisation method of the object. This will be called when a new 
    # instance of the class if created. 
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
    # Falcon will fire this method after handling the request via the 
    # resource class.
    async def process_response_async(
        # The instance of the object that has been created.
        self: type, 
        # The instance of the falcon.Request object. This is scoped to each 
        # individual request.
        req: type, 
        # The instance of the falcon.Response object. This is scoped to each 
        # individual request.
        resp: type, 
        # The instance of the routing handler object. 
        resource: type, 
        # The status of the request object. Set as True if no exceptions were 
        # raised during route handling.
        req_succeeded: bool
    # This method does not return any value.
    ) -> None:
        # Only create a response body if resource response succeeded.
        if '200' in resp.status:
            # Get the route URI from the Falcon request object and strip the 
            # http schema.
            _route: str = req.uri.split('//')[1]
            # Set the base response object with the request method and route 
            # URI.
            _data: dict = { 'endpoint': f'{req.method}: {_route}' }
            # If cookies are present set cookie headers for response.
            cookies: dict = req.context.pop('cookies', {})
            if cookies:
                # Set the base arguments for the cookie generation.
                base_options: dict = {
                    'secure': True,
                    'path': '/',
                    'domain': 'forske.org',
                    'http_only': True
                }
                # Set cookies.
                for key in cookies:
                    age: int = 360 if key == 'token' else 86400
                    resp.set_cookie(
                        key,
                        cookies[key],
                        **base_options,
                        max_age=age
                    )
            # Set requester information for the response with a default of 
            # None | null.
            _data['user'] = req.context['user'] \
                if 'user' in req.context.keys() \
                else None
            _data['self'] = req.context['self'] \
                if 'self' in req.context.keys() \
                else None
            # Set the response media as a JSON object.
            resp.media = { **_data, **req.context }