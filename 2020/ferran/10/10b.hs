import Data.List
import Control.Arrow

-- HOWTO run through GHCi
-- ghci > :l *.hs > main

main = do
    str <- readFile "input.txt"
    (lines >>> map (read :: String -> Int) >>> func >>> show >>> putStrLn) $ str

-- "func" fills up an accumulator list using
-- a blueprint that gives all the recurrence dependencies

func :: [Int] -> [Int]
func xs = foldl (\acc xs -> acc ++ [sum $ zipWith (*) acc xs]) [1] blueprint
              where
                  blueprint = tail [map (\x -> fromEnum $ ((pivot - x >= 0) && (pivot - x <= 3))) ls | pivot <- ls]
                  ls = (0: (sort xs)) ++ [(maximum xs) + 3]
