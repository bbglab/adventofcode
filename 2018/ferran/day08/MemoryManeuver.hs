import Control.Monad
import Data.Char
import Data.List.Split
 
-- parse strings
 
parse :: FilePath -> IO [Int]
parse fn = liftM (map read) $ liftM (splitOn " " . head) $ parseLines fn
    where parseLines = fmap lines . readFile

sumMeta :: [Int] -> Int
sumMeta xs = process 1 xs
    where process k (n:m:ys)
              | k == 1 = (sum $ takeLast m ys) + process n (dropLast m ys)
              | n == 0 = (sum $ take m ys) + process l k-1
              | l == [] = process 
        where dropLast n = reverse . drop n . reverse
              takeLast n = take n . reverse

