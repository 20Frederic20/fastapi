from enum import Enum

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

# Autres constantes potentielles
MAX_USERS = 1000
DEFAULT_LANGUAGE = "en"
API_VERSION = "v1"

# Constantes liées à la sécurité
TOKEN_EXPIRATION_DAYS = 30
PASSWORD_MIN_LENGTH = 8

# Constantes liées aux limites de l'API
RATE_LIMIT_PER_MINUTE = 60
MAX_PAGE_SIZE = 100

# Constantes pour les codes d'erreur personnalisés
ERROR_USER_NOT_FOUND = "USER_001"
ERROR_INVALID_CREDENTIALS = "AUTH_001"

# ... autres constantes selon les besoins de votre application

