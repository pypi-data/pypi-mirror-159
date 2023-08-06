import os
from getpass import getpass
from typing import Optional

from h2o_experiment_tracking.auth.authenticator import (
    Authenticator,
    OIDCAuthenticator,
    HAICAuthenticator,
)
from h2o_experiment_tracking.constants import (
    H2O_CLOUD_ENVIRONMENT,
    PLATFORM_TOKEN_ENDPOINT,
    PLATFORM_CLIENT_ID,
    H2O_EXP_TRACK_AUTH_OIDC_URL,
    H2O_EXP_TRACK_AUTH_OIDC_CLIENT_ID,
    H2O_EXP_TRACK_AUTH_OIDC_HOSTNAME,
    H2O_EXP_TRACK_AUTH_OIDC_CLIENT_SECRET,
)


def check_auth_env_configs() -> Optional[Authenticator]:
    if H2O_EXP_TRACK_AUTH_OIDC_URL in os.environ:
        if H2O_EXP_TRACK_AUTH_OIDC_CLIENT_ID in os.environ:
            # DCR disabled
            auth = OIDCAuthenticator(
                os.environ[H2O_EXP_TRACK_AUTH_OIDC_URL],
                hostname=os.environ[H2O_EXP_TRACK_AUTH_OIDC_HOSTNAME],
                dcr_enabled=False,
                client_id=os.environ[H2O_EXP_TRACK_AUTH_OIDC_CLIENT_ID],
                client_secret=os.environ[H2O_EXP_TRACK_AUTH_OIDC_CLIENT_SECRET],
            )
        else:
            # DCR enabled
            auth = OIDCAuthenticator(os.environ[H2O_EXP_TRACK_AUTH_OIDC_URL])
        return auth
    elif (
        H2O_CLOUD_ENVIRONMENT in os.environ
        and PLATFORM_TOKEN_ENDPOINT in os.environ
    ):
        token_gen_url = (
            os.environ[H2O_CLOUD_ENVIRONMENT] + "/auth/get-platform-token"
        )
        print(f"Visit {token_gen_url} to get your platform token")

        token_endpoint = os.environ[PLATFORM_TOKEN_ENDPOINT]
        token_endpoint_without_slash = (
            token_endpoint[:-1]
            if token_endpoint.endswith("/")
            else token_endpoint
        )
        userinfo_endpoint = (
            "/".join(token_endpoint_without_slash.rsplit("/")[:-1])
            + "/userinfo"
        )

        return HAICAuthenticator(
            getpass("Enter your platform token: "),
            token_endpoint,
            userinfo_endpoint,
            os.environ[PLATFORM_CLIENT_ID],
        )
    return None
