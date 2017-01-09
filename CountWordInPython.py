
# -*-coding:utf-8 -*

#import os # On importe le module os

"""Count words."""
from operator import itemgetter

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s = s.lower()
    ponct = [".", "!", ":", "?", ","]
    
    for elt in ponct:
        s=s.replace(elt,'')
    print("Liste extraite ", s)        
    
    listOcc = s.split(' ')
    print("Liste separee ", listOcc)
    nbOcc = []
    i = 0
    while i < len(listOcc):
        for elt in listOcc:
            eltRecherche = elt
            nbelt = 0
            for elt2 in listOcc:
                if elt2 == eltRecherche: 
                    nbelt = nbelt + 1
                        
            # Critère d'ajout
            ajout = "NO"
            for elt3 in nbOcc:
                mot,indice = elt3
                if mot == eltRecherche :
                    ajout = "OK"
                
            if ajout == "NO" :
                nbOcc.append((eltRecherche, nbelt))        
            
            i = i + 1
            
##        for i, elt in enumerate(nbOcc):  
##            print("À l'indice {} se trouve {}.".format(i, elt))

    
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    print(" ------------------------ ")
    print("\nResultat avant trie : \n ", nbOcc)
    
    # Ranger dans l'ordre alphabétique
    nbOcc = sorted(nbOcc, key=itemgetter(0), reverse=False)
    # Ranger dans l'ordre décroissant selon l'occurrence
    nbOcc.sort(key=itemgetter(1), reverse=True)
    

    print(" ------------------------ ")
    print("\nResultat apres trie : \n ", nbOcc)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = nbOcc[:n]
    print("RESULTAT FINAL : --------- ")
    print(" +++++++++++++++++++++++++++++++++++++++++++++ ")
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    
    print count_words("cat bat,: mat cat bat cat.?", 3)
    print(" +++++++++++++++++++++++++++++++++++++++++++++ ")
    
    print count_words("betty bought a bit of butter but the butter was bitter", 3)
    print(" +++++++++++++++++++++++++++++++++++++++++++++ ")

if __name__ == '__main__':
    test_run()

input("Appuyez sur ENTREE pour fermer ce programme...")
#os.system("pause")

