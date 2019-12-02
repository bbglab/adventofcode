-- ReposeRecord.hs

import Data.Char
import Data.List
import Data.List.Split
import qualified Data.Vector as Vector
import qualified Data.Map as Map

-- parse the strings of signed integers

parseLines :: FilePath -> IO [String]
parseLines = fmap lines . readFile

-- scan and sort the list of events

type Events = Map.Map String [Int]

--parse :: [String] -> Events
--parse xs = 


toMap :: [(Int, String)] -> Events
toMap [x] = func x Map.empty
    where func (n, a) m
              | not (a `elem` ["wakesup","fallasleep"]) = Map.insertWith (++) a [] m
              | otherwise                              = Map.insertWith (++) a [n] m

updateSleep :: Int -> Int -> [Int] -> [Int]
updateSleep a b xs = [x + 1 | x <- xs, a <= x, x <= b-1]

transform :: [Char] -> (Int, Int, String)
transform xs = (read day, read time, action)
    where v       = Vector.fromList $ splitOneOf "[]:- " xs          
          day     = foldl (++) "" $ Vector.slice 1 3 v
          time    = foldl (++) "" $ Vector.slice 4 2 v 
          action  = foldl (++) "" $ Vector.slice 7 2 v         
          n       = read (day ++ time) :: Int

toList :: [String] -> [(Int, String)]
toList xs = map secthird sorted 
    where sorted = sortBy (\(a,b,_) (a',b',_) -> compare a a' `mappend` compare b b') l
          l = map transform xs
          secthird (_,a,b) = (a,b)

