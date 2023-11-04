import streamlit as st
from PIL import Image
from math import*
import matplotlib.pyplot as plt
import numpy as np

st.title("Exercice sur les équations du second degré")
st.header("Comment trouver les racines d'un polynome du second degré en utilisant le langage python?")

with st.expander("1 - Algorithme en langage naturel"):
    image = Image.open('langage naturel.jpg')
    image1 = Image.open('organigramme.jpg')
    st.title("1/ Algorithme en langage naturel")
    st.image(image, caption = 'langage naturel')
    st.image(image1)
with st.expander("2 - Fonction de calcul du discriminant"):
    st.title("2/ Ecrire en Python une fonction delta(a,b,c) qui retourne le discriminant (E)")
    st.header("Ce programme permet de calculer le discriminant d'une fonction du second degré")
    def delta (a,b,c):
        Discriminant=b**2-4*a*c
        return Discriminant
    code = '''def delta (a,b,c):
        Discriminant=b**2-4*a*c
        return Discriminant'''
    st.code(code, language='python')
    a1=st.slider("a=",-10,10,1,key=1)
    b1=st.slider("b=",-10,10,1,key=2)
    c1=st.slider("c=",-10,10,1,key=3)
    st.write("discriminant =", delta(a1,b1,c1))
with st.expander("3 - Instruction 'if', 'else' et 'elif'"):
    d = '''elif'''
    st.title("3/ En python, à quoi sert l'instruction elif?")
    st.header("L'instruction 'elif' est une combinaison de 'else' et de 'if', elle sert à tester plusieurs conditions succesivement.")
    st.subheader("Exemple : On cherche à savoir quels sont les nombres premiers compris entre 1 et 10")
    code = '''a=int(input("Valeur de a"))
        if a==5 :
            print("a est un nombre premier nombres entre 1 et 10")
        elif a==1 :
            print("a est un nombre premier nombres entre 1 et 10")
        elif a==2 or 3 or 7 :
            print("a est un nombre premier nombres entre 1 et 10")
        else :
            print("a n'est pas un nombre premier compris entre 1 et 10")'''
    st.code(code, language = 'python')
with st.expander("4 - Complétion d'un programme python'"):
    st.title("4/ Compléter les lignes 4, 5 et 8 du programmes ci dessous")
    image = Image.open('enonce.jpg')
    st.image(image, caption = 'énoncé du cours')
    code = '''def nombres_solutions(a,b,c):
        discrimnant = delta(a, b, c)
        if discriminant < 0:
            return 0
        elif discriminant ==0:
            return 1
        else:
            return 2'''
    st.code(code, language = 'python')
with st.expander("5 - Application du programme complet'"):
    def delta (n1,n2,n3):
            D=n2**2-4*n1*n3
            return D

    def resolution(n1,n2,n3):    
        if n1==0:
            return "ce n'est pas une equation du 2nd degré"
        else:
            x=delta(n1,n2,n3)
            if x == 0:
                return "une racine double" , round(((-n2)/(2*n1)),2)
            elif x<0:
                return "le dicriminant est négatif donc il n'y a pas de solutions"
            else:
              
                return "le discrimant est positif donc il y a deux solutions: ",round(((-n2-sqrt(x))/(2*n1)),2),round(((-n2+sqrt(x))/(2*n1)),2)

    st.title("5/ Ecrire un autre programme qui donne les solutions losrqu'elles existent")
    code = '''from math import*
    a = int(input("quelle est la valeur de a?"))
    b = int(input("quelle est la valeur de b?"))
    c = int(input("quelle est la valeur de c?"))
    def delta (n1,n2,n3):
        D=n2**2-4*n1*n3
        return D

    if a==0:
        print("cette équation n'est pas du second degré")
    else:
        x=delta(a,b,c)
        if x == 0:
            print("le discriminant est nul donc il y a une solution:",(-b)/(2*a))
        elif x<0:
            print("le dicriminant est négatif donc il n'y a pas de solutions")
        else:
            print("le discrimant est positif donc il y a deux solutions: ",(-b-sqrt(x))/(2*a)," et",(-b+sqrt(x))/(2*a))'''
    st.code(code, language = 'python')
    st.text("Déterminer les facteurs du polynome a*x²+b*x+c")
    col1, col2 = st.columns(2)
    with col1:
        a = st.slider('a=', -100, 100, 1,key=4)
        b = st.slider('b=', -100, 100, 1,key=5)
        c = st.slider('c=', -100, 100, 1,key=6)
        st.write ( a,"x²  +",b,"x +",c ," =  0")
        D=delta (a,b,c)
        st.write ("discriminant = ",D)
        resultat = resolution(a,b,c)
        st.write(resultat)
    with col2:
        x = np.linspace(-10, 10, 70)
        y1 = a*(x)** 2+b*(x)+c
        #y2=0*x
        fig, ax = plt.subplots()
        ax.plot(x,y1)
        #ax.plot(x,y2)
        plt.title('Polynome du second degré')

        plt.axis((-10, 10, -2, 10))

        #-------Affichage de la grille------------
        grid_x_ticks = np.arange(-5,5, 0.5)
        grid_y_ticks = np.arange(-100, 100, 1)
        ax.set_xticks(grid_x_ticks , minor=True)
        ax.set_yticks(grid_y_ticks , minor=True)

        ax.grid()

        st.pyplot(fig)
    
    
    
    