

digitpower :: Floating a => a -> a -> a
digitpower x k = if x >= 10.0**((k-1)/k) 
                    then (digitpower x (k + 1)) + 1
                    else 0

