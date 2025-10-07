import pytest

from endereco import validar_endereco

def test_endereco_valido():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "1000",
		"cidade": "São Paulo",
		"estado": "SP",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is True

def test_endereco_invalido_cep():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "1000",
		"cidade": "São Paulo",
		"estado": "SP",
		"cep": "0131-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_invalido_estado():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "1000",
		"cidade": "São Paulo",
		"estado": "Sao Paulo",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_invalido_numero():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "10A0",
		"cidade": "São Paulo",
		"estado": "SP",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_invalido_rua():
	endereco = {
		"rua": "Av",
		"numero": "1000",
		"cidade": "São Paulo",
		"estado": "SP",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_invalido_cidade():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "1000",
		"cidade": "S",
		"estado": "SP",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_faltando_campo():
	endereco = {
		"rua": "Avenida Paulista",
		"numero": "1000",
		"cidade": "São Paulo",
		"cep": "01310-100"
	}
	assert validar_endereco(endereco) is False

def test_endereco_tipo_incorreto():
	endereco = [
		"rua", "Avenida Paulista",
		"numero", "1000",
		"cidade", "São Paulo",
		"estado", "SP",
		"cep", "01310-100"
	]
	assert validar_endereco(endereco) is False
