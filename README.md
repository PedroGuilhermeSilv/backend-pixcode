

# Gerador de QR Code PIX Backend

Um serviço backend em FastAPI que gera QR codes para pagamentos PIX (sistema de pagamento instantâneo brasileiro).

## Funcionalidades

- Gera QR codes PIX com valores e chaves personalizados
- Faz upload das imagens QR code para armazenamento compatível com S3
- Retorna URLs públicas dos QR codes gerados

## Pré-requisitos

- Python 3.11
- PDM (gerenciador de pacotes Python)
- Credenciais de armazenamento compatível com AWS/S3

## Configuração

1. Instale o PDM se ainda não tiver:
```sh
pip install pdm
```

2. Instale as dependências:
```sh
pdm install
```

3. Crie um arquivo 

.env

 com suas credenciais de armazenamento:
```sh
SECRET_ID_TEBI=sua_chave_de_acesso
SECRET_KEY_TEBI=sua_chave_secreta
```

## Executando a Aplicação

Inicie o servidor de desenvolvimento:
```sh
pdm run uvicorn src.fastapi.app.main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Endpoints da API

### Gerar QR Code PIX
```
POST /pix-qrcode

{
    "value": "100.00",
    "key": "sua-chave-pix"
}
```

Resposta:
```json
{
    "image_url": "https://storage.url/qrcode.png"
}
```