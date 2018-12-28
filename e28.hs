

topleft :: (Integral a) => a -> a
topleft 3 = 7
topleft n = topleft (n-2) + 4 * (n-2) + 2

topright :: (Integral a) => a -> a
topright n = n^2

botleft :: (Integral a) => a -> a 
botleft n = (n-1)^2 + 1

botright :: (Integral a) => a -> a 
botright 3 = 3
botright n = botright(n-2) + 2*(n-2) + 2*(n-3)

numbers = [3,5..1001]
spiral x = sum (map x numbers)
