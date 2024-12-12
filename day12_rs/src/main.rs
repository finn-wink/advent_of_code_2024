use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    let mut raw_arr: Vec<Vec<i32>> = Vec::new();
    let mut num_dict: HashMap<String, i32> = HashMap::new();

    for line in reader.lines() {
        for c in line.chars() {
            if 
        }
    }
    Ok(())
}

// Convert each character to an int

// Need to calculate the number of fence sides and area

// Encoding each number for their position within the shape?
// One number for a corner, number for side, number for dead end

// Dead-end: 3
// squeezed: 2
// edge: 1
// corner: 2
// sorrounded 4

// Need a positions checked

// Need search algorithm to find all connected pieces

