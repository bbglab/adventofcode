import Control.Monad
import Data.Char
import Data.List

-- parse the strings

parseLines :: FilePath -> IO [String] 
parseLines = fmap lines . readFile

-- command in the IO monad

--checkSumIO :: FilePath -> IO Int
--checkSumIO fpath = liftM checkSum (parseLines fpath) 

-- checkSumIO "input.txt"
-- 8820
-- first part done!

-- command in the IO monad

--findPairIO :: FilePath -> IO String
--findPairIO fpath = liftM findPair (parseLines fpath)

-- findPairIO "input.txt" 
-- bpacnmglhizqygfsjixtkwudr
-- second part done!
