#     PARTIE2.
#      2.1)
#     a) L'expression récursive pour la fonction divinRec(a, b)
#     est 1 + divinRec(a - b, b) (on va devoir ajouter 1 à chaque appel 
#     jusqu'à ce que a soit inférieur ou égal à b).
#     Le critère d'arrêt est lorsque a est inférieur ou égal à b, 
#     dans ce cas, le compilateur nous renvoie 0


#     b)Voici la fonction recursive divinRec prenant en prametre a et b

def divinRec(a, b):
    if a <= b:
        return 0
    else:
        return 1 + divinRec(a - b, b)


#  2.2)
#  a) Le critère d'arrêt pour la fonction factorial(a, b) est lorsque b 
#     est égal à zéro, car 0! = 1.

#  b) Voici l'implémentation de la fonction factorial(a, b) :

def factorial(a, b):
    if b == 0:
        return 1
    else:
        return a * factorial(a, b - 1)
    
    
#   c) Combien y'a t-il d'appel recursive    
#     Pour a et b il y'aura 4 appels recursifs
