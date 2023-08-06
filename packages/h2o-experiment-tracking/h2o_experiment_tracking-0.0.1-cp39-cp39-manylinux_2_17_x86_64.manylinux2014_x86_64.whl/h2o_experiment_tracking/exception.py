from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import (
    INTERNAL_ERROR,
    TEMPORARILY_UNAVAILABLE,
    ENDPOINT_NOT_FOUND,
    PERMISSION_DENIED,
    REQUEST_LIMIT_EXCEEDED,
    BAD_REQUEST,
    INVALID_PARAMETER_VALUE,
    RESOURCE_DOES_NOT_EXIST,
    INVALID_STATE,
    RESOURCE_ALREADY_EXISTS,
    ErrorCode,
)

ERROR_CODE_TO_HTTP_STATUS = {
    ErrorCode.Name(INTERNAL_ERROR): 500,
    ErrorCode.Name(INVALID_STATE): 500,
    ErrorCode.Name(TEMPORARILY_UNAVAILABLE): 503,
    ErrorCode.Name(REQUEST_LIMIT_EXCEEDED): 429,
    ErrorCode.Name(ENDPOINT_NOT_FOUND): 404,
    ErrorCode.Name(RESOURCE_DOES_NOT_EXIST): 404,
    ErrorCode.Name(PERMISSION_DENIED): 403,
    ErrorCode.Name(BAD_REQUEST): 400,
    ErrorCode.Name(RESOURCE_ALREADY_EXISTS): 400,
    ErrorCode.Name(INVALID_PARAMETER_VALUE): 400,
}


class ExperimentTrackingException(MlflowException):
    """
    Generic exception thrown to surface failure information about external-facing operations.
    The error message associated with this exception may be exposed to clients in HTTP responses
    for debugging purposes. If the error text is sensitive, raise a generic `Exception` object
    instead.
    """

    pass


class RestException(ExperimentTrackingException):
    """Exception thrown on non 200-level responses from the REST API"""

    def __init__(self, json):
        error_code = json.get("error_code", ErrorCode.Name(INTERNAL_ERROR))
        message = "%s: %s" % (
            error_code,
            json["message"] if "message" in json else "Response: " + str(json),
        )
        super().__init__(message, error_code=ErrorCode.Value(error_code))
        self.json = json


class ExecutionException(ExperimentTrackingException):
    """Exception thrown when executing a project fails"""

    pass


class MissingConfigException(ExperimentTrackingException):
    """Exception thrown when expected configuration file/directory not found"""

    pass


CHANGING_LOGGED_PARAM_MESSAGE = """INVALID_PARAMETER_VALUE: Changing param values is not allowed. \
    Param with key='{}' was already logged with value='{}' for run ID='{}'. \
    Attempted logging new value '{}'."""


CHANGING_LOGGED_PARAMS_MESSAGE = """INVALID_PARAMETER_VALUE: Changing param values is not allowed. \
    Params with keys='{}' were already logged for run ID='{}'. """
