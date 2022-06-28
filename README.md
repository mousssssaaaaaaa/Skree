# 


## Baseline

### Ontwerp
Als baseline oplossing voor de casus Protein Pow(d)er hebben wij gebruik gemaakt van de random module van python. Het random algoritme maakt een willekeurige keuze voor het volgende punt van de ketting. De opties hiervoor zijn omhoog, omlaag, links, rechts, boven en onder (voor in 3d). Voordat het random aloritme een keuze maakt sluiten wij echter de opties uit waarbij de ketting overlapt. In bepaalde situaties zal de ketting hierdoor vastlopen doordat er geen opties beschikbaar zijn, in dit geval resetten wij het programma. In het onderstaande voorbeeld wordt een vastgelopen situatie weergeven waarbij de ketting een tunnel is ingelopen en daardoor geen mogelijke richtingen kan kiezen zonder in overlap te eindigen. 

![Screenshot 2022-06-21 at 12 15 05](https://user-images.githubusercontent.com/65379947/174776196-fc20661c-c950-492a-bd8a-df68ce3e6f6e.png)


### Resultaat
De onderstaande grafiek laat zien dat bij afspelen van 10.000 willekeurige oplossingen de score (hoeveelheid hydrofobe bindingen) normaal verdeeld is. De grafiek begint bij een score van nul waardoor de normaal verdeling alleen aan de rechterkant zichtbaar is. Het resetten van het programma na vastlopen heeft geen gevolgen op de verdeling van de score omdat de ongeldige resultaten worden vervangen door alternatieven met gelijke kansen als wanneeer het resetten niet was gebeurd. Wij hebben een algoritme getest waarbij de algoritme een stapje terugzet in plaats van gereset wordt met als gevolg dat de stapje terug -algoritme en reset-algoritme tot dezelfde verdeling komen. Het resetten van verkeerde oplossingen leidt echter tot een snellere uitwerking bij het afspelen van grote steekproeven. 

![Screenshot 2022-06-21 at 12 50 53](https://user-images.githubusercontent.com/65379947/174782718-ec7e37cb-b2e1-4841-a8c8-ef7e6118f8da.png)


##### Door Nienke, Moussa en Jason
