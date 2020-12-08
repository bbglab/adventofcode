import Control.Monad
import Data.Char
import Data.List

-- HOWTO:
-- ghci > :l 01.hs > main

seatCode :: String -> Int
seatCode xs = let toDecimal = \xs-> foldl (+) 0 [x * 2^(i-1) | (x, i) <- zip xs [1..]]
                  row = toDecimal $ reverse [if x=='B' then 1 else 0 | x <- take 7 xs]
                  col = toDecimal $ reverse [if x=='R' then 1 else 0 | x <- (reverse . take 3 . reverse) xs] 
              in  8 * row + col                  


seatGap :: [Int] -> [(Int,Int)]
seatGap xs = filter ((==2) . (\(x,y) -> x-y)) [(x,y) | (x,y) <- zip (tail ys) (ys)] where
                 ys = sort xs


main = do
   ls <- fmap lines (readFile "input.txt")
   let codes = map seatCode ls
   let highest = maximum codes
   let gaps = seatGap codes
   putStrLn (show highest)
   putStrLn (show gaps)
