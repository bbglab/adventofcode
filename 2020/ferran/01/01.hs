import Control.Monad
import Data.Char
import Data.List

-- HOWTO:
-- ghci > :l 01.hs > main

searchSumTwo :: [Int] -> [Int]
searchSumTwo xs = let cartesian = [(x,y) | x <- xs, y <- xs, x < y]
                      ys = filter ((==2020) . (uncurry (+))) cartesian
                  in map (uncurry (*)) ys


searchSumThree :: [Int] -> [Int]
searchSumThree xs = let cartesian = [(x,y,z) | x <- xs, y <- xs, z <- xs, x < y, y < z]
                        ys = filter ((==2020) . (\(x,y,z) -> x+y+z)) cartesian
                    in map (\(x,y,z) -> x*y*z) ys

main = do
   ls <- fmap lines (readFile "input.txt")
   let a = fmap (\x -> read x :: Int) ls
   putStrLn (show (searchSumTwo a))
   putStrLn (show (searchSumThree a))
   
