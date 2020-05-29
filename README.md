# Flask_Api

**Lancement de l'application**

    $ export FLASK_APP = main.py
    $ flask run

**Port**

    Le serveur HTTP intégré à **FLASK** fonctionne sur le port **5000**
   
   
__Services__
  * *Estimation des taux de CELAN*
    Ce service prend en paramètre l'année de prédiction et l'équipe et retourne sous format JSON les valeurs CELAN pour chaque équipe pour chaque mois de l'année choisie.
  
  
  *  *Estimation de stock*
        Ce service ne prend rien en paramètre, il étudie les progressions du stock durant les mois passée, et prédit alors la quantité du stock pour le mois prochain ( le résultat retourné est sous format JSON).
