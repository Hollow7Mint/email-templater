from enum import Enum

PAGE_SIZE_DEFAULT = 20
PAGE_SIZE_MAX     = 200
TOKEN_BYTES       = 32
SESSION_TTL       = 3600          # seconds
LOCKOUT_DURATION  = 300           # seconds
MAX_LOGIN_TRIES   = 5
DB_PATH           = "data.db"
LOG_FORMAT        = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


class Role(str, Enum):
    USER  = "user"
    ADMIN = "admin"
    GUEST = "guest"


class Status(str, Enum):
    ACTIVE   = "active"
    INACTIVE = "inactive"
    PENDING  = "pending"
    BANNED   = "banned"


HTTP_OK         = 200
HTTP_CREATED    = 201
HTTP_NO_CONTENT = 204
HTTP_BAD_REQ    = 400
HTTP_UNAUTH     = 401
HTTP_FORBIDDEN  = 403
HTTP_NOT_FOUND  = 404
HTTP_CONFLICT   = 409
HTTP_SERVER_ERR = 500
