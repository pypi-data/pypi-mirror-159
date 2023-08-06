import configparser
from classes.errors import OKException
from classes.status import Status


def get_token(scope='default'):
    """
    Retrieves the API token from the SCA3S config file
    based on a given scope.
    """
    config = configparser.ConfigParser()
    try:
        config.read('~/.sca3s/config')
    except:
        raise OKException(Status.CONFIG_NOT_FOUND)
    try:
        return config[scope]
    except:
        raise OKException(Status.ENVIRONMENT_NOT_FOUND)
