import Data.List
import Control.Arrow

-- HOWTO run through GHCi
-- ghci > :l *.hs > main

main = do
    str <- readFile "input.txt"
    (lines >>> map (read :: String -> Int) >>> getBlueprint >>> dynamic [] >>> last >>> show >>> putStrLn) $ str

getBlueprint :: [Int] -> [[Int]]
getBlueprint xs = [map (\x -> fromEnum $ ((pivot - x >= 0) && (pivot - x <= 3))) ls | pivot <- ls] where
                  ls = (0: (sort xs)) ++ [(maximum xs) + 3]

-- dynamic programming following the blueprint

dynamic :: [Int] -> [[Int]] -> [Int]
dynamic [] (x:xs)  = dynamic [1] xs
dynamic acc (x:xs) = dynamic (acc ++ [sum $ zipWith (*) x acc]) xs
dynamic acc []     = acc
