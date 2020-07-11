# msg-code-challenge

This is my solution for the coding challenge of https://get-in-it.de and MSG. 
The challenge is located here: https://www.get-in-it.de/coding-challenge

## What is it about

The task was to find the shortest path from the MSG HQ in Munich over all MSG locations,
back to the MSG HQ in Munich. This problem resembles the "Traveling Salesman Problem".
Therefore we can apply known algorithms to this problem.

The provided data has been in CSV-format (unaltered):
```csv
Nummer,msg Standort,Straße,Hausnummer,PLZ,Ort,Breitengrad,Längengrad
1,Ismaning/München (Hauptsitz),Robert-Bürkle-Straße,1,85737,Ismaning,48.229035,11.686153
2,Berlin,Wittestraße,30,13509,Berlin,52.580911,13.293884
3,Braunschweig,Mittelweg,7,38106,Braunschweig,52.278748,10.524797
4,Bretten,Edisonstraße,2,75015,Bretten,49.032767,8.698372
5,Chemnitz,Zwickauer Straße,16a,09122,Chemnitz,50.829383,12.914737
6,Düsseldorf,Gladbecker Straße,3,40472,Düsseldorf,51.274774,6.794912
7,Essen,Am Thyssenhaus,1.3,45128,Essen,51.450577,7.008871
8,Frankfurt,Mergenthalerallee,73-75,65760,Eschborn,50.136479,8.570963
9,Görlitz,Melanchthonstraße,19,02826,Görlitz,51.145511,14.970028
10,Hamburg,Dammtorwall,7a,20354,Hamburg,53.557577,9.986065
11,Hannover,Hildesheimerstraße,265-267,30519,Hannover,52.337987,9.769706
12,Ingolstadt,Pascalstraße,4,85057,Ingolstadt,48.784417,11.399106
13,Köln/Hürth,Max-Planck-Straße,40,50354,Hürth,50.886726,6.913119
14,Lingen (Ems),Kaiserstraße,10b,49809,Lingen,52.519154,7.322185
15,Münster,Schulstraße,22,48149,Münster,51.969304,7.61428
16,Nürnberg,Südwestpark,60,90449,Nürnberg,49.429596,11.017404
17,Passau,Dr. Hans-Kapfinger-Straße,30,94032,Passau,48.571989,13.453256
18,Schortens/Wilhelmshaven,Beethovenstraße,46,26419,Schortens,53.537779,7.936809
19,St. Georgen,Leopoldstraße,1,78112,St. Georgen,48.126258,8.325873
20,Stuttgart,Humboldtstraße,35,70771,Leinfelden-Echterdingen,48.694648,9.161239
21,Walldorf,Altrottstraße,31,69190,Walldorf,49.295011,8.649036
```

## Solution

The solution is the following path:

```
Ismaning/München (HQ)
Passau
Chemnitz
Görlitz
Berlin
Braunschweig
Hannover
Hamburg
Schortens/Wilhelmshaven
Lingen (Ems)
Münster
Essen
Düsseldorf
Köln/Hürth
Frankfurt
Walldorf
Bretten
St. Georgen
Stuttgart
Nürnberg
Ingolstadt
Ismaning/München (HQ)
```

## How to run this code

This project uses Python3.
I suggest you install the requirements in an own development environment, called virtualenv. There are plenty of tutorials in the internet for this, so I don't get into this in more detail.
If you have a working virtualenv, just install all dependencies via the freezed `requirements_freezed.txt` file:

`$ pip install -r requirements_freezed.txt`

If you have all requirements you can make sure, that everything runs correctly via calling the tests:

`$ python challenge_test.py`

The tests should succeed. It should look like this:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
```

If this is the case, go ahead and execute the actual challenge via:

`$ python challenge.py`

This will automatically load the CSV-file in this repository and calculates the challenge result.
It should return a result data object, similar to this one:
```json
{'total_distance': '2337220 miles', 'start_position': 'Ismaning/München (Hauptsitz)', 'route': ['Ismaning/München (Hauptsitz)', 'Passau', 'Chemnitz', 'Görlitz', 'Berlin', 'Braunschweig', 'Hannover', 'Hamburg', 'Schortens/Wilhelmshaven', 'Lingen (Ems)', 'Münster', 'Essen', 'Düsseldorf', 'Köln/Hürth', 'Frankfurt', 'Walldorf', 'Bretten', 'St. Georgen', 'Stuttgart', 'Nürnberg', 'Ingolstadt', 'Ismaning/München (Hauptsitz)']}
```

## Implementation details

### We see, that you used a library for calculating the TSP. Why?

I see no benefit in reimplementing existing solutions and I am a busy person. This challenge was a nice opportunity for me
to write some Python (after weeks working on my [Google Summer of Code](https://summerofcode.withgoogle.com/organizations/5599302627360768/) project in Go).
Furthermore I never used Google's optimization research library `OR-tools` before, so I took this challenge as offer for having a look on it.

### But, we wanted that you implement your own solution..

Then you should either use different problems, that are not one-to-one replacable against algorithms or you should specify this exactly in your Code Challenge guidelines.
Your own guidelines said:

```
* Correctness of algorithm
* Choice of algorithm
* Readability
* Executability 
```

I think I have covered all of your aspects with my solution, even if I didn't implement the TSP problem myself.
By the way nice examples for problems that are not one-to-one solvable with existing libraries are:

* https://adventofcode.com/
* https://codingcompetitions.withgoogle.com/kickstart

Maybe you want to focus on such problems the next time ;)

## Code Challenge Feedback

I like to give you some feedback, too. It is my second [https://get-in-it.de](https://get-in-it.de) code challenge this year.
I see nothing wrong with my solution from last year ([https://github.com/shibumi/b3-r7-r4nd7](https://github.com/shibumi/b3-r7-r4nd7))
and still I am sure you didn't even thought about my solution, because I did not implement the algorithm myself. I really think you should be
more precise regarding what you want actually want to challenge. Your decisions should be data-driven. What do you want to test?
Do you want to test possible Job applicants for rewriting existing implementations? I think this is a really bad way of testing possible
job applicants and you will very likely make wrong decisions. Instead of picking persons, who know their toolset and know which tool they need to
pick for an existing problem, you are looking for persons who always tries to solve a problem without help from others.
Time is money and with respect to this challenge I have solved the challenge in under 5 hours, where as people who implement everything theirself
might spend much more time on it. This is one of the reasons why German companies are so bad in performing compared to bigger US companies.
All in all If I would be the company, I would just construct more complex code problems (like the ones from [Advent of Code](https://adventofcode.com/)).
These code problems are challenging and it's difficult to apply libraries on the problem, without further work.




