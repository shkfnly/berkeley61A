(define (map fn lst)
    (cons (fn (car lst))
    (map fn (cdr lst))
    ))

(define (reduce fn s lst)
    (if (null? lst) s
      (fn (car lst) (reduce fn s (cdr lst)))
))


(define (entry tree)
  (car tree)
  )

(define (left tree)
 (car (cdr tree))
 )

(define (right tree)
 (cdr (cdr tree))
 )

(define (btree-sum tree)
 (if (null? tree)
      0
      (+ (entry tree) (btree-sum (left tree)) (btree-sum (right tree))

 )))


(define (insert element lst position)
    (if (< position 1)
     (cons element lst)
     
     (cons (car lst) (insert element (cdr lst) (- position 1)))


     ))


(define (duplicate lst)
 (if (null? lst) lst
  (cons (car lst) (cons (car lst) (duplicate (cdr lst))
   ))))

 


 
