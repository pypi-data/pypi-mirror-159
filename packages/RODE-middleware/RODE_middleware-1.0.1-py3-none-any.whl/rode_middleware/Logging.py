# ============================================================================
__author__          =   'Manuel Nielsen'
__copyright__       =   'Copyright - The RODE Project'
__credits__         =   ['Manuel Nielsen']
__license__         =   'Proprietary and Confidential'
__maintainer__      =   'Manuel.Nielsen@health.nsw.gov.au'
# ============================================================================
# IMPORT PACKAGES
# ============================================================================
import datetime
import os
# ============================================================================
# DEFINE MIDDLEWARE
# ============================================================================
# This class inherits all the features of the classes.Core object. 
#
# The Logging middleware is responsible for the logging of request activity to 
# the system log files. This logging will only occur when the CI pipeline 
# stage is production.
class Logging:
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
    # Falcon will fire this method after handling the request via the resource 
    # class.
    async def process_response_async(
        # The instance of the object that has been created.
        self: type, 
        # The instance of the falcon.request object. This is scoped to each 
        # individual request.
        req: type, 
        # The instance of the falcon.response object. This is scoped to each 
        # individual request.
        resp: type, 
        # The instance of the routing handler object. 
        resource: type, 
        # The status of the request object. Set as True if no exceptions were 
        # raised during route handling.
        req_succeeded: bool
    # This method does not return any value.
    ) -> None:
        # Perform CI pipeline stage check and ONLY perform logging if CI 
        # pipeline stage is production.
        if self.STAGE == 'production':
            log_dir: str = os.environ.get('LOGS') \
                if os.environ.get('LOGS') \
                else '/logs'
            # Set timestamps for logging. Timestamps run on the timezone set
            # in the container.
            # Currently UTC [MN - 2022-01-21].
            today: str = datetime.date.today().strftime('%Y-%m-%d')
            now: str = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            # Get user for logging from request context.
            try: user: dict | None = req.context.user
            except: user = req.auth
            # Set log string for the request
            log_string: str = '\n{}|{}:{}|{}|{}'.format(
                now,
                req.method,
                req.uri,
                resp.status,
                user
            )
            # Create daily file for logging if it does not exist.
            try: open(f'{log_dir}/{today}.txt', 'r')
            except Exception:
                with open(f'{log_dir}/{today}.txt', 'w+') as fp:
                    fp.write('DATETIMESTAMP|METHOD:URI|RESPONSE|USER')
            # Append the log string to the daily log file.
            with open(f'{log_dir}/{today}.txt', 'a') as fp:
                fp.write(log_string)
