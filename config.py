# Citizen Tech Shop :: configuracao (INTENCIONALMENTE VULNERAVEL - treino)
# [VULN] segredos e chaves hardcoded (detectaveis por Gitleaks)

DEBUG = True

# Banco de dados
DB_HOST = "10.0.0.20"
DB_USER = "admin"
DB_PASSWORD = "SuperSecret123!"                 # [VULN] senha hardcoded

# Credenciais de nuvem (valores de EXEMPLO/FAKE - documentacao AWS)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"                              # [VULN]
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"     # [VULN]

# Tokens de terceiros (falsos)
STRIPE_API_KEY = "stripe_demo_placeholder"           # [VULN]
SLACK_TOKEN = "slack_demo_placeholder"  # [VULN]
JWT_SECRET = "citizen-tech-jwt-signing-secret-do-not-share"           # [VULN]
