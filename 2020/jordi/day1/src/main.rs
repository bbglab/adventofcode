use itertools::Itertools;
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> Result<(), std::io::Error> {
    let input = "./input.txt";

    let solution_one = find_solution(input.to_string(), 2);
    println!("Solution part one {}", solution_one.expect("invalid list of numbers"));

    let solution_two = find_solution(input.to_string(), 3);
    println!("Solution part two {}", solution_two.expect("invalid list of numbers"));

    Ok(())
}

fn find_solution(input: String, n: usize) -> Option<i32> {
    let file = File::open(input).expect("File not found");
    io::BufReader::new(file)
        .lines()
        .map(|x| x.unwrap().parse::<i32>().unwrap())
        .combinations(n)
        .filter(|x| x.iter().sum::<i32>() == 2020)
        .map(|x| x.iter().product::<i32>())
        .next()
}


