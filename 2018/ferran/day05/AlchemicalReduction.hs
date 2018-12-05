import Data.Char
import Control.Monad
import Data.List.Split

-- parse the strings of signed integers
 
parseLines :: FilePath -> IO [[Char]]
parseLines = fmap lines . readFile

-- one scan of the String removing reactive pairs

oneStep :: [Char] -> [Char]
oneStep = foldl react ""
    where react acc x
              | acc == ""                    = [x]
              | (x /= l) && (x == toLower l) = init acc
              | (x /= l) && (x == toUpper l) = init acc
              | otherwise                    = acc ++ [x]
              where l = last acc

-- scan as many times as necessary so that 
-- length reduction is no longer accomplished

reaction :: [Char] -> [Char]
reaction xs = develop xs 1
    where develop ys 0 = ys
          develop ys _ = develop zs n
              where zs = oneStep ys 
                    n  = (length ys) - (length zs)

-- do the job in the IO monad

reactionIO :: FilePath -> IO [Char] 
reactionIO fpath = fmap reaction (fmap head (parseLines fpath))

-- Part 1
-- a = reactionIO "input.txt"
-- liftM length a
-- 9462
-- done!

bestReduction :: [Char] -> Int
bestReduction xs = minimum [length $ reaction (remove c xs) | c <- ['a'..'z']]
    where remove c ys = concat $ splitOneOf [c, toUpper c] ys 

-- do the job in the IO monad

bestReductionIO :: FilePath -> IO Int
bestReductionIO fpath = fmap bestReduction (fmap head (parseLines fpath))

-- Part 2
-- bestReductionIO "input.txt"
-- 4952
-- done!
