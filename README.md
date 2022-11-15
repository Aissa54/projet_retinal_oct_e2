# projet_retinal_oct_e2

Nouvel arrivant comme développeur en intelligence artificielle chez la start-up MedTech en tant qu’alternant, l’entreprise remporte un appel d’offre du CHRU de Nancy pour la réalisation d'un POC (Proof Of Concept) d'une solution IA capable de diagnostiquer les maladies de la rétine à partir d'imagerie par OCT (Optical Coherence Tomography).

La tomographie par cohérence optique rétinienne (OCT) est une technique d'imagerie utilisée pour capturer des coupes transversales à haute résolution de la rétine de patients vivants. Environ 30 millions d'examens OCT sont effectués chaque année, et l'analyse et l'interprétation de ces images prennent beaucoup de temps. 

L’imagerie par OCT permet de détecter soit un épaississement de la rétine, soit la présence d’anomalie dans ou sous la rétine (œdème, néovaisseaux, atrophie, membrane, etc.) Cet examen permet d’analyser les conséquences de pathologies rétiniennes comme la dégénérescence maculaire liée à l’âge, la rétinopathie diabétique, les occlusions vasculaires, etc.

Une première version a été développée par un doctorant de l'INRIA. Il s'agit d'une API qui permet de prédire à partir d'une imagerie par OCT :
•	une néovascularisation choroïdienne
•	un Œdème maculaire diabétique
•	de multiples drusen
•	une rétine normale

La mission confiée par le CHRU Nancy est d'améliorer le modèle (en modifiant ses paramètres ou en utilisant une autre architecture) et de développer une application avec une page de prédiction (chargement d'une imagerie par OCT et affichage de la prédiction).
