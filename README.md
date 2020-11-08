# The-Books-Library

The project goal is to automatically generate an HTML page that lists the name, author, genre and summary of a book. 
The only parameter needed is the name of the book. The HTML page keeps track on the number of books that have been added (and presumably read).

To use the script, type:

```
$ python book_library.py "Name of a book"
```

Example:

```
$ python book_library.py "La Vie Devant Soi"
```

The output should be:

```
Adding a new book:
Name:  La Vie Devant Soi
Author(s):  Romain Gary, Émile Ajar
Genre:  Fiction
Description:  La vie devant soi raconte l’histoire, dans le quartier de Belleville, à Paris, d’un petit garçon arabe orphelin, Momo, et d’une dame juive, âgée, malade, Madame Rosa,
 qui garde dans son appartement des enfants dont les mères travaillent ou ont disparu.Dès la publication du livre d’Émile Ajar, Momo et Madame Rosa sont devenus célèbres, presque d
es personnages publics, et le roman a été aussitôt traduit dans une multitude de pays.C’est que ce roman, qui provoque constamment le rire et les larmes, porte en lui toutes les qu
estions, tous les drames et tous les rêves du monde d’aujourd’hui.Lorsqu’à la fin du livre la police enfonce la porte de la cave où le petit Momo veille le corps de Madame Rosa qu’
il n’a pas voulu laisser conduire à l’hôpital, ces deux protagonistes d’un immense amour atteignent une fois pour toute la dimension de Légende, parce que face aux oppressions et a
ux injustices ils ont lutté jusqu’au bout, par la lumière et l’intelligence et par la force du cœur.La vie devant soi a reçu le prix Goncourt en 1975.
```
