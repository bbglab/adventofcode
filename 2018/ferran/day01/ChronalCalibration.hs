import Control.Monad
import Data.Char
import Data.List

-- parse the strings of signed integers

parseLines :: FilePath -> IO [String] 
parseLines = fmap lines . readFile

-- coerce those strings to integers

strToInt :: [Char] -> Int
strToInt x = case x of
             ('+':xs) -> read xs :: Int
             ('-':xs) -> negate $ (read xs :: Int)

-- do the sum in the IO monad

toSum :: FilePath -> IO Int
toSum fpath = liftM (sum . map strToInt) (parseLines fpath) 

-- first part
-- toSum "input.txt"
-- 525

toList :: FilePath -> IO [Int]
toList fpath = liftM (map strToInt) (parseLines fpath)

-- partial sums

partialSum :: [Int] -> [Int]
partialSum xs = tail $ scanl (+) 0 xs

-- idea: if we cycle the list of frequencies, the partial sums will repeat modulo 525 (total sum);
-- find the pair of elements in the list of partial sums with least distance that is exactly 
-- a multiple of total sum

-- find all pairs at distance a multiple of n

congru :: Int -> [Int] -> [(Int, Int)]
congru n xs = map flip congruList 
    where
      congruList      = [(a, b) | (a, b) <- cart2Prod xs, (a-b) `mod` n == 0, a /= b]
      cart2Prod xs    = [(snd x, snd y) | x <- zip [1..] xs, y <- zip [1..] xs, fst x /= fst y]
      flip (x, y)
          | x <= y    = (x, y)
          | otherwise = (y, x) 

-- now find those at least distance

firstRepeat :: Int -> [Int] -> (Int,Int,Int)
firstRepeat n xs = head sorted
    where pairList = congru n (partialSum xs) 
          sorted   = sortBy (\(_,_,a) (_,_,b) -> compare a b) (map addDiff pairList)
          addDiff (x, y) = (x, y, abs (x - y))   

-- finish the job in the IO monad

firstRepeatIO :: FilePath -> IO Int
firstRepeatIO fpath = liftM (get2nd . firstRepeat 525) (toList fpath)
    where get2nd (_, a, _) = a

-- second part
-- firstRepeatIO "input.txt"
-- 75749

-- DONE!
