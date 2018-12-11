# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Guilherme Zorzon
    NUSP: 10333380

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
class MarkovModel:

    def __init__(self, k, corpus):

        self.corpus = corpus
        self.k = k
        
        str_temp = corpus       #String temporária para que possa ser modificada
        cont = 0                
        vet_alphab = []         #vetor que guarda as letras do alfabeto

        while(len(str_temp) > 0):
            i = 0
            while( i < len(vet_alphab) and str_temp[0] >= vet_alphab[i]):    #faz com que o vetor fique ordenado em ordem crescente
                i += 1
            vet_alphab.insert(i, str_temp[0])
            str_temp = str_temp.replace(str_temp[0], "")                     #tira as letras já vista da string temporária
            cont += 1

        self.no_simb = cont
        self.alph = vet_alphab
        self.circular = self.corpus + self.corpus[0:self.k]                  #Crio uma string circular cortando só o que preciso de corpus e adicionando ao final

    def alphabet(self):
        string = "'"
        for char in self.alph:     #Crio a string apenas para atender ao padrão de saída imposto no EP
            string += char

        string += "'"
        return string
        

    def N(self, t):
        conta_seq = 0
        if(len(t) != (self.k) and len(t) != (self.k + 1)):
            return None
        
        for i in range(len(self.corpus)):
            var = True
            for j in range(len(t)):
                if(t[j] != self.circular[j + i]):
                    var = False
            if(var == True):
                conta_seq += 1

        if(conta_seq == 0):                      #Se a string se encaixar nos padrões pedidos (len = k ou k+1) e não se encontrar em self.corpus, na verdade ela deve retornar None
            return None
        return conta_seq


    def laplace(self, t):
        if(len(t) != (self.k + 1)):
            return None
        temp = t[:-1]                           #Crio uma string de tamanho k para obter N(pal)
        s1 = self.N(t)                          #N(pal + c)
        s2 = self.N(temp)                       #N(pal)
        if(s1 == None):
            s1 = 0
        if(s2 == None):
            s2 = 0
            
        return (s1 + 1)/(s2 + len(self.alph))   #len(self.alph) é o tamanho do vetor que contém as letras do alfabeto ( = A)


    def __str__(self):
        vec_comparak = []
        vec_comparak2 = []
        
        string = "alfabeto tem " + str(len(self.alph)) + " símbolos\n"
        
        #Os dois laços abaixo criam dois vetores com todos as strings t de len = k ou k+ 1
        #ordenados em ordem alfabética, sem repetição
        for i in range(len(self.corpus)):
            j = self.circular[i: i+self.k]
            m = 0
            while(m < len(vec_comparak) and j > vec_comparak[m]):   #coloca em ordem alfabética
                m += 1
            if(m == len(vec_comparak) or j != vec_comparak[m]):     #garante que não há repetição
                vec_comparak.insert(m, j)

        for i in range(len(self.corpus)):
            j = self.circular[i: i+self.k+1]
            m = 0
            while(m < len(vec_comparak2) and j > vec_comparak2[m]):
                m += 1
            if( m == len(vec_comparak2) or j != vec_comparak2[m]):
                vec_comparak2.insert(m, j)
        
        for i in range(len(vec_comparak)):
            string += '"' + vec_comparak[i] + '"   ' + str(self.N(vec_comparak[i])) + "\n"
        for i in range(len(vec_comparak2)):
            string += '"' + vec_comparak2[i] + '"  ' + str(self.N(vec_comparak2[i])) + "\n"
        
        return string
        
#------------------------------------------------------------------
def main():
    corpus1 = "aabcabaacaac"
    corpus2 = "babababaabababaabaabaaaaaababaaaab"
    corpus3 = "Como é bom estudar MAC0122!"
    print("corpus1: \n" + corpus1)
    print("corpus2: \n" + corpus2)
    print("corpus3: \n" + corpus3)
    print()
    
    modelo1 = MarkovModel(2, corpus1)
    modelo2 = MarkovModel(4, corpus2)
    modelo3 = MarkovModel(0, corpus3)

    print(modelo1)
    print()
    print(modelo2)
    print()
    print(modelo3)
    print()

    print("alfabeto 1: \n" + modelo1.alphabet())
    print("alfabeto 2: \n" + modelo2.alphabet())
    print("alfabeto 3: \n" + modelo3.alphabet())
    print()

    print("N de 'aa' para o modelo1: " + str(modelo1.N("aa")))
    print("N de 'aab' para o modelo1: " + str(modelo1.N("aab")))
    print("N de 'aaa' para o modelo1: " + str(modelo1.N("aaa")))
    print("N de 'baaa' para o modelo2: " + str(modelo2.N("baaa")))
    print("N de 'aabaa' para o modelo1: " + str(modelo2.N("aabaa")))
    print()

    print("laplace de 'aaa' para modelo1: \n" + str(modelo1.laplace("aaa")))
    print("laplace de 'aab' para modelo1: \n" + str(modelo1.laplace("aab")))
    print("laplace de 'aac' para modelo1: \n" + str(modelo1.laplace("aac")))
    print()


if __name__ == '__main__':
    main()



    

    
            
            
        
        









    
