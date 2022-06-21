# Skree

### Nienke, Moussa en Jason


## Baseline

### Ontwerp
Als baseline oplossing voor de casus Protein Pow(d)er hebben wij gebruik gemaakt van de random module van python. Het random algoritme maakt een willekeurige keuze voor het volgende punt van de ketting. De opties hiervoor zijn omhoog, omlaag, links, rechts, boven en onder (voor in 3d). Voordat het random aloritme laten kiezen sluiten wij echter de opties uit waarbij de ketting overlapt. In bepaalde situaties zal de ketting hierdoor vastlopen doordat er geen opties beschikbaar zijn, in dit geval herstarten wij het programma. In het onderstaande voorbeeld wordt een situatie weergeven waarbij de ketting een tunnel is ingelopen en daardoor geen mogelijke richtingen kan kiezen zonder in overlap te eindigen. 

![Screenshot 2022-06-21 at 12 15 05](https://user-images.githubusercontent.com/65379947/174776196-fc20661c-c950-492a-bd8a-df68ce3e6f6e.png)


### Resultaat


Aan het einde van het vak presenteer je een goede oplossing voor je case. Dat brengt altijd de vraag met zich mee, wat is goed? Het antwoord weten we ook niet. Toch zijn er wel manieren om de kwaliteit van een oplossing over te brengen. Eén daarvan is om je oplossing te vergelijken met andere oplossingen. Stel je de ruimte met mogelijke oplossingen voor en stel dat we daar willekeurig steekproeven uit kunnen nemen. Op basis daarvan kan je een heleboel vertellen, bijvoorbeeld wat de score is van een gemiddelde oplossing, of misschien zelfs de verdeling van de score.

Voor deze milestone is het daarom de taak om een algoritme te implementeren dat willekeurige oplossingen genereert en daarmee resultaten produceert. In het ideale geval is dit een uniforme steekproef uit de oplossingsruimte. Waarschijnlijk lukt dat niet helemaal, omdat er bijvoorbeeld een vooroordeel (bias) in het willekeurige proces zit, of omdat je concessies moet doen omwille van bijvoorbeeld tijd of geheugen. Daarom vragen we je om op één kantje met maximaal 400 woorden de resultaten te laten zien, toe te lichten wat de resultaten betekenen en waarom deze afwijken of zelfs af moeten wijken van een uniforme steekproef.


