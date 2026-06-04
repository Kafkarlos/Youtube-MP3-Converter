# Tube

Ferramenta CLI Simples para baixar audio do YouTube

## Dependências

- yt-dlp
- ffmpeg

## Dependẽncias Python

- inquirerpy

## Uso

```bash
python src/main.py
```

ou

```bash
python src/main.py URL
```

### Argumentos opcionais

Você pode executar o arquivo com alguns argumentos junto.

| ARG       | DESCRIÇÃO                               |
|-----------|-----------------------------------------|
| --quality | Define a qualidade do áudio (kbps)      |
| --confirm | pula a etapa de confirmação do download |

Exemplo:
```bash
python main.py URL --qualty 192 --confirm
```

## Créditos

Esse projeto foi originalmente projetado por [Kafkarlos/Youtube-MP3-Converter](https://github.com/Kafkarlos/Youtube-MP3-Converter).

Essa versão adiciona melhorias de interface, usabilidade e organização do código.
