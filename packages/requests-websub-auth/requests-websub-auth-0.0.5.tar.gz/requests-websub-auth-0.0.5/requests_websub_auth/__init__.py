from enum import Enum
from hmac import HMAC
from typing import Literal, Union

from requests.auth import AuthBase
from requests.models import PreparedRequest

class WebSubAlgorithm(Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

class WebSubAuth(AuthBase):
    """
    Performs WebSub Authenticated Content (https://www.w3.org/TR/websub/#signing-content)
    for the Python Requests package
    """

    def __init__(
        self,
        key: Union[str, bytes, bytearray],
        algorithm: WebSubAlgorithm = WebSubAlgorithm.SHA1,
    ) -> None:
        """Create a new WebSubAuth object.

        key: str, bytes or buffer, key for the keyed hash object.
        algorithm: the hashing algorith. Defaults to SHA1
        """
        if not key:
            raise ValueError(f"key may not be empty")
        if isinstance(key, str):
            key = key.encode()
        if len(key) >= 200:
            raise ValueError("key must be < 200 bytes in length")
        self.algorithm = algorithm or WebSubAlgorithm.SHA1
        self.key = key

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        hmac = HMAC(
            digestmod=self.algorithm.value, key=self.key, msg=request.body
        ).hexdigest()
        request.headers["X-Hub-Signature"] = f"{self.algorithm.value}={hmac}"
        return request
