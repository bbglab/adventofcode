use std::fs::File;
use core::ops::Range;
use std::io::{self, BufRead};

fn main() {
    let input = "./input.txt";
    let passwords = load_passwords(input.to_string());

    println!("Solution part one {:#?}", passwords.iter().filter(
        |x| x.policy().range().contains(&(x.value().matches(x.policy().character()).count() as i32))
    ).count());

    println!("Solution part two {:#?}", passwords.iter().filter(
        |x| {
            let a = x.value().chars().nth((x.policy().range().start - 1) as usize).unwrap();
            let b = x.value().chars().nth((x.policy().range().end - 2) as usize).unwrap();
            let c = x.policy().character().chars().nth(0).unwrap();
            (a==c || b==c) && !(a==c && b==c)
        }
    ).count());
}

fn load_passwords(input: String) -> Vec<String> {
    let file = File::open(input).expect("File not found");
    io::BufReader::new(file)
        .lines()
        .map(|x| x.unwrap())
        .collect()
}

trait Password {
    fn policy(&self) -> String;
    fn value(&self) -> String;
    fn valid(&self) -> bool;
}

trait PasswordPolicy {
    fn range(&self) -> Range<i32>;
    fn character(&self) -> &str;
}

impl PasswordPolicy for String {
    fn range(&self) -> Range<i32> {
        let parsed = self.split(' ').nth(0).unwrap().splitn(2, '-').map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>();
        Range{ start: parsed[0], end: parsed[1]+1}
    }

    fn character(&self) -> &str {
        self.split(' ').nth(1).unwrap()
    }
}

impl Password for String {
    fn policy(&self) -> String {
        self.split(':').nth(0).unwrap().to_string()
    }

    fn value(&self) -> String {
        self.split(':').nth(1).unwrap().trim().to_string()
    }

    fn valid(&self) -> bool {
        self.policy().range().contains(&(self.value().matches(self.policy().character()).count() as i32))
    }
}
