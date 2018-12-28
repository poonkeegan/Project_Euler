
digit :: Int -> Int -> Int -> Int
digit b x n = mod (div x (b^(pred n))) b

decdig :: Int -> Int -> Int
decdig = digit 10

bindig :: Int -> Int -> Int
bindig = digit 2

factcount :: Int -> Int -> Int
factcount count 0 = count
factcount count n = factcount (count * n) (pred n)

fact :: Int -> Int
fact = factcount 1


lencount :: Int -> Int -> Int -> Int
lencount count _ 0 = count
lencount count b n = lencount (succ count) b (div n b)

lennum :: Int -> Int -> Int
lennum _ 0 = 1
lennum x y = lencount 0 x y

binlen :: Int -> Int
binlen = lennum 2
declen :: Int -> Int
declen = lennum 10

decdigits x = map (decdig x) (let xlength = declen x 
                                in [xlength, (xlength - 1) .. 1])

factsum x = sum(map fact (decdigits x))
n = 100000
numbers = [3 .. n]
equiv = [x | x <- numbers, x == factsum x]
answer = sum equiv
main = do
    print answer
    
