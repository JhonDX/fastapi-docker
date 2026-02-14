SELECT
	ti."Titulo_id" AS id,
	ti."Tipo_titulo",
	mo."Data_resgate",
	mo."Vencimento_titulo",
	ti."Validade_titulo",
	mo."Tipo_evento",
	mo."Quantidade",
	mo."Valor" AS valor_total
FROM titulo AS ti
LEFT JOIN movimentacao AS mo
    ON ti."Titulo_id" = mo."Titulo_id";