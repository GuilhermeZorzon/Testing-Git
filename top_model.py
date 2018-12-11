# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: 10333380
    NUSP: Guilherme Zorzon

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
#------------------------------------------------------------------

# MarkovModel(), MarkovModel.laplace(), __str__()
from markov_model import MarkovModel

# math.log()
import math

class TopModel:
    
    def __init__(self, k, dict_corpora):

        self.modelos = []
        self.mkv_vec = []
        self.k = k
        self.dict_corp = dict_corpora

        for st in dict_corpora:
            self.modelos.append(st)
            self.mkv_vec.append(MarkovModel(self.k, self.dict_corp[st]))

    def __str__(self):
        string = "TopModel possui " + str(len(self.modelos)) + " modelos: "
        for i in range(len(self.modelos)):
            if(i < len(self.modelos) - 1):
                string += self.modelos[i] + ","
            else:
                string += self.modelos[i] + "\n"

        for i in range(len(self.modelos)):
            string += "Modelo " + self.modelos[i] + ":\n"
            string += self.mkv_vec[i].__str__()

        return string

    def modelo(self, nome_modelo):
        esta = False
        for i in range(len(self.modelos)):
            if(self.modelos[i] == nome_modelo):
                esta = True
                index = i
                break

        if(esta == False):
            print("modelo(): modelo '" + nome_modelo + "' não foi definido")
            return None
        else:
            return self.mkv_vec[index]

    def verossimilhanca_total(self, nome_modelo, citacao):
        esta = False 
        for i in range(len(self.modelos)):
            if(self.modelos[i] == nome_modelo):          #Checa de "nome_modelo" é um nome compatível com os modelos existentes
                esta = True
                index = i
                        
        if(esta == False):
            print("verossimilhança_total(): modelo '" + nome_modelo + "' não foi definido")
            return None

        corp = citacao
        circular = corp + corp[0:self.k]   #cria uma string circular que será analisada
        vs_total = 0

        for i in range(len(corp)):
            t = ''
            for j in range(self.k + 1):
                t += circular[i+j]
            vs_total += math.log(self.mkv_vec[index].laplace(t))   #calcula a verossimilhança total


        return vs_total

    def media_verossimilhanca(self, nome_modelo, citacao):
        esta = False 
        for i in range(len(self.modelos)):
            if(self.modelos[i] == nome_modelo):
                esta = True
                
        if(esta == False):
            print("media_verossimilhança(): modelo '" + nome_modelo + "' não foi definido")  #Apesar da função de baixo fazer esse mesmo laço de novo, se eu usasse um if(vs_media == None)
            return None                                                                      #depois de chamar ela e nome_modelo não fosse um nome compatível, já teria imprimido o erro da 
                                                                                             #função verossimilhança_total antes. Então resolvi fazer assim
        vs_media = self.verossimilhanca_total(nome_modelo, citacao)/ len(citacao)
        return vs_media

    def top_model(self, citacao):
        melhor_modelo = self.modelos[0]
        for i in range(len(self.modelos) - 1):
            if(self.media_verossimilhanca(self.modelos[i+1], citacao) > self.media_verossimilhanca(melhor_modelo, citacao)):
                melhor_modelo = self.modelos[i+1]

        return melhor_modelo, self.media_verossimilhanca(melhor_modelo, citacao)


#------------------------------------------------------------------
def main():
    corpus1 = "aabcabaacaac"
    corpus2 = "babababaabababaabaabaaaaaababaaaab"
    corpus3 = "Como é bom estudar MAC0122!"
    corpus4  = "aaabaaabaaabaaabaaab"
    print("corpus1: \n" + corpus1)
    print("corpus2: \n" + corpus2)
    print("corpus3: \n" + corpus3)
    print("corpus4: \n" + corpus4)
    print()
    
    dicio_corp1 = {"aab...": corpus1, "bab...": corpus2, "mac": corpus3}
    dicio_corp2 = {"aaab...": corpus4}
    auditor1 = TopModel(2, dicio_corp1)
    auditor2 = TopModel(3, dicio_corp2)
    print(auditor1)
    print()
    print(auditor2)
    print()

    modelo_aab = auditor1.modelo("aab...")
    print("modelo aab... em auditor 1: \n" + str(modelo_aab))
    auditor1.modelo("as")
    print()

    citacao = "aabca"
    print("citação :" + citacao)
    print()
    print("verossimilhança total - aab... auditor 1: " + str(auditor1.verossimilhanca_total("aab...", citacao)))
    print("verossimilhança total - mac auditor 1: " + str(auditor1.verossimilhanca_total("mac", citacao)))
    print("verossimilhança total - aaab... auditor 2: " + str(auditor2.verossimilhanca_total("aaab...", citacao)))
    print()
    print("verossimilhança média - aab... auditor 1: " + str(auditor1.media_verossimilhanca("aab...", citacao)))
    print("verossimilhança média - aaab... auditor 2: " + str(auditor2.media_verossimilhanca("aaab...", citacao)))
    print()

    print("Top model teste")
    melhor_modelo, media = auditor1.top_model(citacao)
    print("melhor modelo para a citação " + citacao + ": " + melhor_modelo)
    print("media correspondente: " + str(media))
    

    

if __name__ == '__main__':
    main()






        
