from twitter.account import Account

# Pega aquí los valores exactos que copiaste del navegador
auth_token = "PEGA_AQUI_TU_AUTH_TOKEN"
ct0 = "PEGA_AQUI_TU_CT0"

cookies = {
    "auth_token": auth_token,
    "ct0": ct0
}

# Inicializa la cuenta usando la sesión de cookies
account = Account(cookies=cookies)

# Prueba publicando un tweet
account.tweet("Hola mundo, probando mi bot desde la API.")

print("¡Tweet publicado exitosamente!")