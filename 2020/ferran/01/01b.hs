import Control.Arrow

-- HOWTO run through GHC interactive:
-- ghci > :l 01-terse.hs > main

main = do
    text <- readFile "input.txt"
    (lines >>> map (read :: String -> Int) >>> searchSumThree >>> show >>> putStrLn) $ text


searchSumThree :: [Int] -> Int
searchSumThree (x:xs) = case f (2020-x) xs of
                          Nothing -> searchSumThree xs
                          Just y -> x*y

f :: Int -> [Int] -> Maybe Int
f n (y:ys) = if (n-y) `elem` ys then Just ((n-y)*y) else f n ys
f _ [] = Nothing
