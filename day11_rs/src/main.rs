use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn apply_rules(line: &HashMap<u64, u128> ) -> HashMap<u64, u128> {

    let mut result = HashMap::new();

    for n in line.iter() {

        let int_str = n.0.to_string();
        let int_length = int_str.chars().count();

        if n.0 == &0 {
            if result.contains_key(&1) {
                result.entry(1).and_modify(|e| *e += n.1);
            }
            else {
                result.insert(1, *n.1);
            }
        }
        else if int_length % 2 == 0 {
            let index_half = (int_length / 2) - 1;
            let half_1 = &int_str[..index_half+1];
            let half_2 = &int_str[index_half+1..];

            let i_half_1 = half_1.parse::<u64>().unwrap();
            let i_half_2 = half_2.parse::<u64>().unwrap();

            if result.contains_key(&i_half_1) {
                result.entry(i_half_1).and_modify(|e| *e += n.1);
            }
            else {
                result.insert(i_half_1, *n.1);
            }

            if result.contains_key(&i_half_2) {
                result.entry(i_half_2).and_modify(|e| *e += n.1);
            }
            else {
                result.insert(i_half_2, *n.1);
            }
        }
        else {
            if result.contains_key(&(*n.0 * 2024)) {
                result.entry(*n.0 * 2024).and_modify(|e| *e += n.1);
            }
            else {
                result.insert(*n.0 * 2024, *n.1);
            }
        }
    }
    return result;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    let mut start_nums: Vec<u64> = Vec::new();

    for line in reader.lines() {
        start_nums = line?.split_whitespace().map(|num| num.parse().expect("Failed to parse")).collect(); // Map it to each number in the line
    }

    let mut current = HashMap::new();

    for s in start_nums.iter() {
        current.insert(*s, 1 as u128);
    }

    for i in 0..75 {
        current = apply_rules(&current);
        println!("{}", i);
        println!("{:?}", current)
    }
    
    let total: u128 = current.values().copied().sum();
    
    println!("{}", total);

    Ok(())
}