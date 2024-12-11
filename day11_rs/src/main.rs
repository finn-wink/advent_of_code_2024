use std::fs::File;
use std::io::{self, BufRead};

fn apply_rules(line: &Vec<i32>) -> Vec<i32> {
    
    let mut next_nums: Vec<i32> = Vec::new();

    for n in line.iter() {

        let int_length = n.to_string().chars().count();
        println!("{}", int_length);

        if *n == 0 { // If 0 it becomes 1
            next_nums.push(1 as i32);
        }
    }
    
    
    // If even number of digits (ie length) split into two (by length)
    // No leading 0s kept
    // If no rules apply new stone is * by 2024
    // Order is always preserved
    return next_nums;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    let mut start_nums: Vec<i32> = Vec::new();

    for line in reader.lines() {
        start_nums = line?.split_whitespace().map(|num| num.parse().expect("Failed to parse")).collect(); // Map it to each number in the line
    }

    let mut current: Vec<i32> = Vec::new();

    for i in 0..3 {
        if i == 0 {
            current = start_nums.clone();
        }
        let new_nums = apply_rules(&current);
        current = new_nums.clone();
    }

    Ok(())
}