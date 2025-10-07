import re

def validar_endereco(endereco: dict) -> bool:

    if not isinstance(endereco, dict):
        return False

    campos = ["rua", "numero", "cidade", "estado", "cep"]
    if not all(campo in endereco for campo in campos):
        return False

    campo_rua = bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]{3,}", endereco["rua"]))
    campo_numero = bool(re.fullmatch(r"\d+[A-Za-z]?", str(endereco["numero"])))
    campo_cidade = bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]{2,}", endereco["cidade"]))
    campo_estado = bool(re.fullmatch(r"[A-Za-z]{2}", endereco["estado"]))
    campo_cep = bool(re.fullmatch(r"\d{5}-?\d{3}", endereco["cep"]))

    return all([campo_rua, campo_numero, campo_cidade, campo_estado, campo_cep])
