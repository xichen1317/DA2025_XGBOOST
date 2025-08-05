# !pip install snowflake-connector-python cryptography --quiet

from cryptography.hazmat.primitives import serialization
import snowflake.connector

# Load your uploaded private key
with open("private_key.pem", "rb") as key_file:
    p_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None  # use password=b"your_password" if your key is encrypted
    )

private_key_bytes = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

conn = snowflake.connector.connect(
    account = "MARS-MARSSNACKINGDIVISION_US",
    user = "xi.chen3@effem.com",
    role = "SF_MW_HUMAN_INTELLIGENCE_DEVELOPER_WRITE",
    warehouse = "MW_HUMAN_INTELLIGENCE_DATASCIENCE_WH",
    database = "MW_DATALAKE_HUMAN_INTELLIGENCE",
    schema = "PERSISTENT",
    private_key = private_key_bytes
)