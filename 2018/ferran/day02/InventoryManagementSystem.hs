import Control.Monad
import Data.Char
import Data.List

-- parse the strings

parseLines :: FilePath -> IO [String] 
parseLines = fmap lines . readFile

-- how many times an element is found in a list

numTimes :: Eq a => a -> [a] -> Int
numTimes x = length . filter (x==)

-- is there an element in s exactly n times?

countnTimes :: Eq a => Int -> [a] -> Bool
countnTimes n s = n `elem` countList 
    where countList = [numTimes x s | x <- s]

-- do the checksum

checkSum :: [String] -> Int
checkSum s = a * b
    where a = length $ filter (True==) $ map (countnTimes 2) s
          b = length $ filter (True==) $ map (countnTimes 3) s

-- command in the IO monad

checkSumIO :: FilePath -> IO Int
checkSumIO fpath = liftM checkSum (parseLines fpath) 

-- checkSumIO "input.txt"
-- 8820
-- first part done!

-- how many mismatches between Strings

pairMatch :: String -> String -> Int
pairMatch s t = length $ filter (False==) $ zipWith (==) s t

-- find pair with exactly 1 mismatch, then take the overlap

findPair :: [String] -> String
findPair s = overlap $ head $ filter (\(x,y) -> pairMatch x y == 1) (cart2Prod s)
    where cart2Prod xs   = [(snd x, snd y) | x <- zip [1..] xs, y <- zip [1..] xs, fst x < fst y]
          overlap (s, t) = [snd x | x <- zip [1..] s, y <- zip [1..] t, x == y]

-- command in the IO monad

findPairIO :: FilePath -> IO String
findPairIO fpath = liftM findPair (parseLines fpath)

-- findPairIO "input.txt" 
-- bpacnmglhizqygfsjixtkwudr
-- second part done!
