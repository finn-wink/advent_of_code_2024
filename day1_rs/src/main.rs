use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> { // returns nothing on success
    let file = File::open("src/numbers.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    // Vector to store all numbers
    let mut numbers_1: Vec<u64> = Vec::new();
    let mut numbers_2: Vec<u64> = Vec::new();

    for line in reader.lines() {
        let line = line?;

        let line_numbers: Vec<&str> = line.split_whitespace().collect();
        numbers_1.push(line_numbers[0].parse().expect("Failed to parse"));
        numbers_2.push(line_numbers[1].parse().expect("Failed to parse"));        

        numbers_1.sort();
        numbers_2.sort();
    }

    let mut sum = 0;

    for (index, value_1) in numbers_1.iter().enumerate() {
        // let value_2 = numbers_2[index];
        // let diff = std::cmp::max(value_1, &value_2) - std::cmp::min(value_1, &value_2);
        // sum += diff;
        let count = numbers_2.iter().filter(|&x| x == value_1).count();
        // filter gets a reference to x in the iterator, which is also a reference
        // Can compare two references to variables in iterator, as above.
        sum += *value_1 * count as u64;
    }

    println!("{}", sum);

    Ok(()) // for the no-return of main
}