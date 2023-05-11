def GeraVariavel(dicionario,frase_lista,ProcuraPalavra):
	variavel1 = ProcuraPalavra(dicionario,frase_lista[0])
	variavel2 = ProcuraPalavra(dicionario,frase_lista[1])
	variavel3 = ProcuraPalavra(dicionario,frase_lista[2])
	variavel4 = ProcuraPalavra(dicionario,frase_lista[3])
	variavel5 = ProcuraPalavra(dicionario,frase_lista[4])
	arquivo = open('FrasesPossiveis.txt','w')
	for palavra1 in variavel1:
		for palavra2 in variavel2:
			for palavra3 in variavel3:
				for palavra4 in variavel4:
					for palavra5 in variavel5:
						arquivo.write('%s %s %s %s %s\n'%(palavra1,palavra2,palavra3,palavra4,palavra5))
	arquivo.close()