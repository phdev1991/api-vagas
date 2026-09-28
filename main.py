from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()


class Vaga(BaseModel):
    titulo: str
    empresa: str
    localizacao: str
    modalidade: Literal["remoto", "presencial", "hibrido"]


vagas = [
    {
        "id": 1,
        "titulo": "Desenvolvedor Python Júnior",
        "empresa": "Tech Recife",
        "localizacao": "Recife - PE",
        "modalidade": "remoto"
    },
    {
        "id": 2,
        "titulo": "Desenvolvedor Backend",
        "empresa": "Startup Nordeste",
        "localizacao": "São Paulo - SP",
        "modalidade": "hibrido"
    }
]


@app.get("/")
def raiz():
    return {"mensagem": "API de vagas no ar!"}


@app.get("/vagas")
def listar_vagas(
    modalidade: str | None = None,
    empresa: str | None = None,
    localizacao: str | None = None
):
    resultado = vagas

    if modalidade:
        resultado = [
            vaga for vaga in resultado
            if vaga["modalidade"].lower() == modalidade.lower()
        ]

    if empresa:
        resultado = [
            vaga for vaga in resultado
            if empresa.lower() in vaga["empresa"].lower()
        ]

    if localizacao:
        resultado = [
            vaga for vaga in resultado
            if localizacao.lower() in vaga["localizacao"].lower()
        ]

    return {
        "mensagem": "Lista de vagas",
        "total": len(resultado),
        "vagas": resultado
    }

@app.get("/vagas/{vaga_id}")
def buscar_vaga(vaga_id: int):
    for vaga in vagas:
        if vaga["id"] == vaga_id:
            return vaga

    raise HTTPException(
        status_code=404,
        detail="Vaga não encontrada"
    )


@app.post("/vagas", status_code=201)
def criar_vaga(vaga: Vaga):
    nova_vaga = {
        "id": len(vagas) + 1,
        **vaga.model_dump()
    }

    vagas.append(nova_vaga)

    return nova_vaga


@app.put("/vagas/{vaga_id}")
def atualizar_vaga(vaga_id: int, vaga_atualizada: Vaga):
    for indice, vaga in enumerate(vagas):
        if vaga["id"] == vaga_id:
            dados_atualizados = vaga_atualizada.model_dump()
            dados_atualizados["id"] = vaga_id

            vagas[indice] = dados_atualizados

            return {
                "mensagem": "Vaga atualizada com sucesso",
                "vaga": vagas[indice]
            }

    raise HTTPException(
        status_code=404,
        detail="Vaga não encontrada"
    )
@app.delete("/vagas/{vaga_id}")
def excluir_vaga(vaga_id: int):
    for indice, vaga in enumerate(vagas):
        if vaga["id"] == vaga_id:
            vaga_excluida = vagas.pop(indice)

            return {
                "mensagem": "Vaga excluída com sucesso",
                "vaga": vaga_excluida
            }

    raise HTTPException(
        status_code=404,
        detail="Vaga não encontrada"
    )

@app.delete("/vagas/{vaga_id}")
def excluir_vaga(vaga_id: int):
    for indice, vaga in enumerate(vagas):
        if vaga["id"] == vaga_id:
            vaga_excluida = vagas.pop(indice)

            return {
                "mensagem": "Vaga excluída com sucesso",
                "vaga": vaga_excluida
            }

    raise HTTPException(
        status_code=404,
        detail="Vaga não encontrada"
    )