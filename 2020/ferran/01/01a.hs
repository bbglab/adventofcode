import Control.Arrow

-- HOWTO run through GHC interactive:
-- ghci > :l 01-terse.hs > main

main = do
    text <- readFile "input.txt"
    (lines >>> map (read :: String -> Int) >>> searchSumTwo >>> show >>> putStrLn) $ text

searchSumTwo :: [Int] -> Int
searchSumTwo (x:xs) = if (2020 - x) `elem` xs then (2020 - x) * x else searchSumTwo xs
