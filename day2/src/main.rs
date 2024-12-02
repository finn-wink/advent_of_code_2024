// Read a line of text
// Make a new list of the differences between the numbers
// Check for lists that have values below 1 or above 3
// Check for lists that have both positive and negative values

use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> { // returns nothing on success
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    // Vector to store all numbers
    let mut diff_list: Vec<Vec<i32>> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut diff: Vec<i32> = Vec::new();

        let numbers: Vec<i32> = line.split_whitespace().map(|num| num.parse().expect("Failed to parse")).collect(); // Map it to each number in the line
        let max = numbers.len() as u32;

        for (i, v) in numbers.iter().enumerate() {
            
            if i as u32 == (max-1) { // stop one before the end
                break;
            }
            
            let sub: i32 = v - numbers[i+1];
            diff.push(sub);

        }

        diff_list.push(diff);

    }

    let mut sum = 0;

    for x in diff_list.iter() {
        if x.iter().max() > 3 { // if max is bigger than 3
            continue;
        }
        if x.iter().min() < -3 { // if min is smaller than -3
            continue;
        }
        if x.contains(&0) {
            continue;
        }

        // if there is positive and negative numbers

        sum += 1;
    }

    println!("{:?}", diff_list);

    Ok(()) // for the no-return of main
}