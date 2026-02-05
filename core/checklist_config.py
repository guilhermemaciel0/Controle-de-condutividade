CHECKLIST = {
	"diaria": {
		"Operação geral": [
			{"id": "torre_em_operacao", "label": "Torre em operação", "type": "bool"},
			{"id": "ventilador_ok", "label": "Ventilador ok (sem ruído/vibração)", "type": "bool"},
			{"id": "sem_vazamentos", "label": "Sem vazamentos visíveis", "type": "bool"},
		],
		"Reservatório da torre": [
			{"id": "nivel_normal", "label": "Nivel normal", "type": "bool"},
			{"id": "agua_clara", "label": "Água clara (sem limo/algas)", "type": "bool"},
			{"id": "sem_espuma", "label": "Sem espuma excessiva", "type": "bool"},
			{"id": "mau_cheiro", "label": "Sem mau cheiro", "type": "bool"},
			{"id": "boia", "label": "Boia funcionando", "type": "bool"},
		],
		"Produtos Químicos": [
			{"id": "qm_tr_637", "label": "QM TR 637 - Nível", "type": "choice", "options": "Bom", "Médio", "Baixo", "Vazio"},
			{"id": "qm_bac_674", "label": "QM BAC 674 - Nível", "type": "choice", "options": ["Bom", "Médio", "Baixo", "Vazio"]},
			{"id": "qm_cf_803", "label": "QM CF 803 - Nível", "type": "choice", "options": ["Bom", "Médio", "Baixo", "Vazio"]},
			{"id": "dosadores", "label": "Dosadores", "type": "bool"},
			{"id": "mangueira_interna", "label": "Mangueira interna OK", "type": "bool"},
			{"id": "mangueiras", "label": "Integridade das mangueiras", "type": "bool"},
		],
		"Condutividade - Torre de Resfriamento (circuito aberto)": [
			{"id": "medicao_realizada", "label": "Medição realizada", "type": "bool"},
			{"id": "valor_cond_tr", "label": "Valor (µS/cm)", "type": "number"},
		],
		"Blowdown (dreno manual)": [
			{"id": "cond_acima", "label": "Condutividade acima do limite", "type": "bool"},
			{"id": "dreno_ligado", "label": "Válvula do dreno acionada", "type": "bool"},
			{"id": "cond_apos_dreno", "label": "Condutividade após dreno", "type": "number"}, 
		],
	},

	"semanal": {
		"Circuito fechado - CF 803": [
			{"id": "cf803_coleta", "label": "Coleta realizada", "type": "bool"},
			{"id": "cf803_ponto", "label": "Ponto (retorno/antes do filtro zeólita)", "type": "text"},
			{"id": "cf803_valor", "label": "Valor (µS/cm)", "type": "number"},
		],
		"Filtro zeólita": [
			{"id": "retrolavagem", "label": "Retrolavagem automática operando", "type": "bool"},
			{"id": "alarmes_falhas", "label": "Sem alarmes / falhas visíveis
			{"id": "perca_agua", "label": "Sem perda excessiva de água", "type": "bool"},
		],
		"Controle microbiológico": [
			{"id": "limo_visivel", "label": "Presença de limo no reservatório da torre de resfriamento", "type": "choice", "options": ["Sim", "Não"]},
			{"id": "odor", "label": "Presença de odor", "type": "choice", "options": ["Sim", "Não"]},
		],

	},
	"mensal": {
		"Inspeção física": [
			{"id": "reservatorio_limpo", "label": "Reservatório da torre está limpo", "type": "choice", "options": ["Sim", "Não"]},
		],
	},
}

LIMITES = {
	"cond_tr_alvo_min": 1200,
	"cond_tr_alvo_max": 2000,
	"cond_tr_max": 2500,
	"cf803_alvo_min": 80,
	"cf803_alvo_max": 200,
	"cf803_aceitavel_max": 300,
	"cf803_risco_corrosao": 50, 
}
