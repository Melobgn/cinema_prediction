import mysql.connector

mysql.connector.connect(
                host = "dbcinapps.mysql.database.azure.com",
                user = "Spies",
                password = "Simplon1948",
                database = "dbcinapps",
                ssl_ca="/home/kevin/Bureau/DigiCertGlobalRootCA.crt.pem"
            )


