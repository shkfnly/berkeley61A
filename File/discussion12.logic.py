(fact (equal ?thing1 ?thing2))



(fact (complement adenine thymine))
(fact (complement cytosine guanine))



(fact (pokemon (name bulbasaur) (number 001) (color green) (type grass)))
(fact (pokemon (name bulbasaur) (number 001) (color green) (type grass)))
(fact (pokemon (name bulbasaur) (number 001) (color green) (type grass)))
(fact (pokemon (name bulbasaur) (number 001) (color green) (type grass)))
(fact (pokemon (name bulbasaur) (number 001) (color green) (type grass)))

(fact (member ?item (?x . ?r)))
(fact (member ?item (?y . ?r))
      (member ?item ?r))

(fact (match ?string1 ?string2))
      (match (?string1 . ?r) (?string2 . ?r))
      (match ?r ?r)

(fact (every-other (?x . ?r) ?y ))
      (every other ?x  (?r . ?r))


(fact (mapped (complement (?x . ?r)))
      (mapped (complement (?r ?y)))