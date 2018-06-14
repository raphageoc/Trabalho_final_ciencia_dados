# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models


class Despesas(models.Model):
    ano_empenho = models.TextField(blank=True, null=True)
    dt_empenho = models.TextField(blank=True, null=True)
    cd_fonte = models.TextField(blank=True, null=True)
    ds_fonte = models.TextField(blank=True, null=True)
    cd_funcao = models.TextField(blank=True, null=True)
    ds_funcao = models.TextField(blank=True, null=True)
    cd_programa = models.TextField(blank=True, null=True)
    ds_programa = models.TextField(blank=True, null=True)
    cd_acao = models.TextField(blank=True, null=True)
    ds_acao = models.TextField(blank=True, null=True)
    cd_subelemento = models.TextField(blank=True, null=True)
    ds_subelemento = models.TextField(blank=True, null=True)
    cd_orgao = models.TextField(blank=True, null=True)
    ds_orgao = models.TextField(blank=True, null=True)
    cd_despesa = models.TextField(blank=True, null=True)
    ds_despesa = models.TextField(blank=True, null=True)
    codigo_despesa_grupo = models.TextField(blank=True, null=True)
    ds_grupo = models.TextField(blank=True, null=True)
    codigo_despesa_modalidade = models.TextField(blank=True, null=True)
    ds_modalidade = models.TextField(blank=True, null=True)
    codigo_despesa_elemento = models.TextField(blank=True, null=True)
    ds_elemento = models.TextField(blank=True, null=True)
    cpf_cnpj = models.TextField(blank=True, null=True)
    nr_empenho = models.TextField(blank=True, null=True)
    licitacao = models.TextField(blank=True, null=True)
    vl_empenhado = models.TextField(blank=True, null=True)
    cd_item = models.TextField(blank=True, null=True)
    ds_item = models.TextField(blank=True, null=True)
    ds_unidade = models.TextField(blank=True, null=True)
    quantidade = models.TextField(blank=True, null=True)
    vl_preco_unitario = models.TextField(blank=True, null=True)
    vl_total = models.TextField(blank=True, null=True)
    protocolosup = models.TextField(blank=True, null=True)
    dt_transacao = models.TextField(blank=True, null=True)
    a = models.TextField(blank=True, null=True)
    b = models.TextField(blank=True, null=True)
    vl_liquidado = models.TextField(blank=True, null=True)
    vl_devolvido = models.TextField(blank=True, null=True)
    vl_anulado = models.TextField(blank=True, null=True)
    vl_pago = models.TextField(blank=True, null=True)
    vl_consignado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despesas'


class Empresas(models.Model):
    cpf_cnpj = models.TextField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas'
