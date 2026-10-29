# Supports d'apprentissage

Comment écrire un support fait pour être appris, pour que la personne qui l'étudie seule le retienne et s'en serve
sur des problèmes nouveaux, au moindre coût. Le support, c'est la leçon, l'exemple résolu, la feuille d'exercices, la
fiche de révision, les cartes mémoire, et les questions qu'ils contiennent.

Il étend [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/README.md).
Les principes, leurs niveaux de preuve et les vérifications vivent là-bas et ne sont pas répétés ici. Les effets
d'apprentissage eux-mêmes aussi : récupération en mémoire, espacement, exemples résolus, multimédia. Ce dépôt ajoute
ce que le genre change : comment chacun de ces documents est construit, et ce qu'un programme peut y vérifier.

Cette page en anglais : [README.md](README.md). Les deux versions suivent le même état.

> **État :** le périmètre est fixé et la revue de littérature est en cours (2026-10-29) : quatre revues multivocales,
> pas encore fusionnées. Aucun gabarit et aucune vérification ne sont écrits. C'est une lecture informelle de la
> recherche et de la pratique publiées : ni une norme officielle, ni une étude évaluée par des pairs, ni un résultat
> nouveau, ni une prétention à l'état de l'art.
>
> **Comment il est fait :** avec Claude, un assistant IA d'Anthropic, sous la direction du mainteneur, comme
> reader-ergonomics. Des agents IA rédigent les revues de littérature ; chaque référence est résolue par script, et un
> chiffre lu seulement dans un résumé est marqué « (secondary) ». Les corrections sont bienvenues sous forme d'issues.

## Où il se place

```text
        utilise ──▶ (pointe vers ce dont il dépend)

 niveau 2   reader-ergonomics-learning   les gabarits des documents d'étude, et leurs vérifications
                   │
                   ▼  dérive ses gabarits du topic, épinglé à v0.4.0
 niveau 1   reader-ergonomics-topic      un gabarit, le topic, imbriqué à toute profondeur, et sa vérification
                   │
                   ▼  obéit aux principes ; la CI y lance leurs vérifications, épinglé à v1.2.0
 niveau 0   reader-ergonomics            comment un texte sert son lecteur, et sa revue des sciences de l'apprentissage
```

- **Il obéit à reader-ergonomics** et lance ses vérifications, comme toute extension
  ([extending.md](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/extending.md)).
- **Ses gabarits dériveront du
  [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/1220def7863b5e977a3edd1e30bd168fff1523a5/shapes/topic.md)** :
  un titre, un résumé qui tient lieu du document, un corps, son contenu, et ce vers quoi il pointe. Une leçon ou une
  feuille d'exercices ajoute ses propres blocs et n'en retire aucun.
- **Aucun niveau ne dépend d'un niveau au-dessus de lui.** Rien en dessous ne pointe vers ce dépôt.

## Pourquoi il existe

Les preuves sur la façon dont on apprend sont déjà passées en revue. Ce qui manque, c'est le passage de ces preuves aux
documents qu'un apprenant étudie, et un programme qui les vérifie.

| Ce qui existe | Où | Ce qui manque |
|---|---|---|
| les effets d'apprentissage, chacun avec son niveau de preuve et sa taille d'effet | reader-ergonomics, [learning science](https://github.com/Tewf/reader-ergonomics/tree/6d4e324157b17862aa5c5158fde0ba02db992729/evidence/learning-science) | comment s'écrit une question, une carte ou une feuille d'exercices |
| des guides en prose pour enseignants et auteurs | guides de pratique et livres, situés par les revues | une vérification qu'un programme peut lancer |
| des gabarits de leçon vérifiés par programme | [The Carpentries Workbench](https://github.com/carpentries/pegboard) | ses vérifications lisent les titres, les blocs et les liens, pas ce que la leçon enseigne |

## Périmètre

| | Quoi | Pourquoi |
|---|---|---|
| dedans | un support écrit étudié seul : une leçon ou un chapitre, une série d'exemples résolus, une feuille d'exercices, une fiche de révision, un paquet de cartes mémoire, et les questions qu'ils contiennent | le lecteur est l'apprenant, et l'objet est le document, comme dans reader-ergonomics |
| dedans | le support qu'un enseignant écrit pour d'autres, et celui que l'apprenant écrit pour lui-même | les deux se lisent de la même façon, seul et de nouveau plus tard |
| dedans | les gabarits de ces documents, et les vérifications qu'un programme peut y lancer | ce qu'un programme peut vérifier, un programme le vérifie |
| dehors | savoir si une technique d'apprentissage marche | passé en revue dans reader-ergonomics, et lié d'ici |
| dehors | l'enseignement en direct : cours magistraux, exposés, programmation en direct | [reader-ergonomics-presentations](https://github.com/Tewf/reader-ergonomics-presentations) |
| dehors | les algorithmes qui planifient les révisions | évalués dans reader-ergonomics ; un paquet en utilise un, ce dépôt n'en construit pas |
| dehors | les tuteurs intelligents, les plateformes et les tuteurs IA | du logiciel et du dialogue, un autre objet |
| dehors | la conception d'examens notés et leur statistique | un autre domaine ; seules les règles qui valent aussi pour une question d'auto-test sont dedans |
| dehors | la conception de programmes et de cursus | l'unité est ici un document, ou le support d'un cours |

## Les quatre revues

Chaque revue demande comment le document est écrit pour qu'une technique atteigne l'apprenant, pas si la technique
marche. Chacune est une [revue de littérature multivocale](evidence/README.md#method) : recherche et pratique ensemble, chaque source grise notée
pour sa qualité.

| Revue | Question | État |
|---|---|---|
| practice-questions | comment s'écrivent, se placent et se corrigent les questions d'un support d'étude | en cours |
| flashcards | comment s'écrivent et s'entretiennent des cartes à réviser à intervalles espacés | en cours |
| exercise-sets | comment une série d'exercices est ordonnée et soutenue, de l'exemple résolu au problème | en cours |
| instructional-text | comment un texte explicatif se construit autour de son contenu : objectifs, termes, résumés, encadrés | en cours |

Pourquoi quatre, et où chaque travail est passé en revue : [décision 0002](decisions/0002-four-reviews.md).

## Repris des dépôts voisins

Liés à un commit épinglé, jamais copiés ([one place per fact](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/collection/one-place-per-fact.md)).

| De | Quoi | Sert à |
|---|---|---|
| reader-ergonomics | les principes, la revue des sciences de l'apprentissage, les vérifications, la feuille de style, le contrat des extensions | chaque document d'ici ; la CI |
| reader-ergonomics-topic | le topic et son premier gabarit dérivé, la fiche de décision ; la méthode de revue de ses trois revues | les gabarits à venir ; [decisions](decisions/) ; les quatre revues |
| reader-ergonomics-software-design | la méthode de lecture des sites de questions-réponses | le volet Q/R de chaque revue |
| reader-ergonomics-presentations | l'enseignement en direct, qui reste là-bas ; des contextes qui surchargent une base pour un public | la frontière ; un modèle pour les vitesses de lecture d'une fiche de révision, à tester |

## Contenu

| Partie | Contient |
|---|---|
| [decisions](decisions/) | une fiche par choix qui façonne ce dépôt, chacune ouverte par la décision en une phrase |
| [evidence](evidence/) | les quatre revues, une fois fusionnées, et la bibliographie |

## Suite

1. Fusionner les quatre revues ; faire vérifier chaque chiffre dans sa source par des agents qui ne l'ont pas écrit ;
   faire noter une source grise sur cinq par un second évaluateur.
2. Écrire les gabarits que les revues soutiennent, chacun dérivé du topic, et les vérifications qu'un programme peut y
   lancer.
3. Les tester sur de vrais supports d'étude : les livres de solutions expliquées de
   [University-Coursework](https://github.com/Tewf/University-Coursework).

## Le vérifier

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py chemin/vers/ce/depot
```

La CI lance les mêmes vérifications à chaque envoi, et une exécution échoue à la moindre erreur ([checks.yml](https://github.com/Tewf/reader-ergonomics-learning/blob/master/.github/workflows/checks.yml)).
Chaque envoi sur master construit aussi le site, [tewf.github.io/reader-ergonomics-learning](https://tewf.github.io/reader-ergonomics-learning/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-learning/blob/master/.github/workflows/pages.yml)).

## Licence

Le code sous [Apache License 2.0](LICENSE) ; la prose sous [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Réutilisez-le
librement, en citant ce dépôt ; [CITATION.cff](CITATION.cff) donne une citation si besoin.
