import Control.Monad
import Data.Char
import Data.List

-- parse the strings of signed integers

parseLines :: FilePath -> IO [String] 
parseLines = fmap lines . readFile

-- coerce those strings to integers

strToInt :: [Char] -> Int
strToInt ('+':xs) = decInt xs
strToInt ('-':xs) = negate $ decInt xs

decInt :: [Char] -> Int
decInt xs = foldl (\x y -> 10*x + y) 0 (map digitToInt xs)

-- do the sum

toSum :: FilePath -> IO Int
toSum fpath = liftM (sum . map strToInt) (parseLines fpath) 

-- first part
-- toSum "input.txt"
-- 525

toList :: FilePath -> IO [Int]
toList fpath = liftM (map strToInt) (parseLines fpath)

-- simple partial sum

partialSum :: [Int] -> [Int]
partialSum xs = scanl (+) 0 xs

-- if we cycle the list of frequencies, the partial sums will keep repeating modulo 525 (total sum)
-- we must find the pair of elements a < b in the list of partial sums at the least distance that 
-- is exactly a multiple of 525 (total sum)

-- find all pairs in partial sums at distance multiple of total sum

congru :: Int -> [Int] -> [(Int, Int)]
congru n xs = congruList 
    where
      congruList = [(a, b) | (i, j) <- index, let a=xs!!(i-1), let b=xs!!(j-1), (a-b) `mod` n == 0, a <= b]
      index = [(i, j) | (i, j) <- cartProd [1..length xs] [1..length xs], i < j]
      cartProd = (<*>) . fmap (,) -- just the Cartesian product

-- find those that have least distance modulo the total sum
-- we take care to remove the trivial cases

minModDist :: [(Int, Int)] -> Int
minModDist xs = get2nd headElem
    where headElem = head $ removeTrivial $ sortBy (\(_,_,a) (_,_,b) -> compare a b) (map addDiff xs)
          addDiff (x, y) = (x, y, y - x)
          removeTrivial ys = filter (\(a,b,c) -> (a /= 0) || (b == 0)) ys
          get2nd (_,z,_) = z

-- do the job in the IO monad

firstRepeatIO :: FilePath -> IO Int
firstRepeatIO fpath = liftM minModDist (liftM (congru 525) (liftM partialSum (toList fpath)))

-- second part
-- firstRepeatIO "input.txt"
-- 75749

-- DONE!
