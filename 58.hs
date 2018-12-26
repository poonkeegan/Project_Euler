
diagfunc :: Int -> Int -> Int
diagfunc pos x = x^2 - (pos*x) + pos

br :: Int
br = 0
bl :: Int
bl = 1
tl :: Int
tl = 2
tr :: Int
tr = 3

positions :: [Int]
positions = [tr,tl,bl,br]
numseq :: [Int]
numseq = [3,5..]
circ ::  Int -> [Int]
circ n =  map ($ n) (map diagfunc positions)

diagelmts :: [Int]
diagelmts = 1:(concat (map circ numseq))

diagcirc :: Int -> [Int]
diagcirc n = take amtspiralelmts diagelmts
                where amtspiralelmts = (4*(quot (n-1) 2) + 1)


minus :: (Ord a) => [a] -> [a] -> [a]
minus [] _ = []
minus xxs [] = xxs
minus xxs@(x:xs) yys@(y:ys)
    | x > y = minus xxs ys
    | x < y = x : (minus xs yys)
    | otherwise = minus xs yys

numfilt = 2:[3,5..]
sieve :: Int -> [Int] -> [Int]
sieve n primes = 
    if p^2 >= n then primes
    else p:(sieve n (minus primes [p, 2*p..]))
        where p = head primes
primes x = sieve x (take (quot (x+1) 2) numfilt)
primelist = primes (2^20)

prob x = castdiv (length (minus celmts primelist)) (length celmts)
            where celmts = diagcirc x
                  castdiv x y = fromIntegral x / fromIntegral y
listoflen :: [Int]
listoflen = [1547,1549..]
answer (x:xs) 
    | 100 * (1 - prob x) > 90.5 = x
    | otherwise = answer xs

fullanswer = answer listoflen
