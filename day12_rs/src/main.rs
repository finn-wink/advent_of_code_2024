use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn define_type(position: (usize, usize), array: Vec<Vec<i32>>) -> i32 {
    
    let pos_type = 1;
    
    return pos_type;
}


fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    let mut num_dict: HashMap<String, i32> = HashMap::new();
    let mut raw_arr: Vec<Vec<i32>> = Vec::new();

    let mut count = 0;

    for line in reader.lines() {
        let line = line?;
        let mut arr_line: Vec<i32> = Vec::new();

        for c in line.chars() {
            if num_dict.contains_key(&c.to_string()) {
                arr_line.push(*num_dict.get(&c.to_string()).unwrap_or(&-1));
            }
            else {
                num_dict.insert(c.to_string(), count);
                arr_line.push(count);
                count += 1;
            }
        }
        raw_arr.push(arr_line);
    }

    let mut fields: HashMap<i32, Vec<(usize, usize)>> = HashMap::new();

    for row in 0..(raw_arr.len()) {
        for col in 0..(raw_arr[0].len()){
            if fields.contains_key(&raw_arr[row][col]) {
                fields.entry(raw_arr[row][col]).or_insert_with(Vec::new).push((row,col));
            }
            else {
                fields.entry(raw_arr[row][col]).or_insert_with(Vec::new).extend(vec![(row,col)]);
            }
        }
    }

    let mut field_array: Vec<Vec<(usize, usize)>> = Vec::new()

    for (key, value) in fields.iter() {
        for v in value.iter() {
            for t in value.iter() {
                
            }
        }
    }

    println!("{:?}", fields);
    Ok(())
}

// Convert each character to an int

// Need to calculate the number of fence sides and area

// Encoding each number for their position within the shape?
// One number for a corner, number for side, number for dead end

// Make dictionary of the numbers and their positions
// Check distance between the positions to determine which belong together

// Find a way to calculate what position they hold.

// Dead-end: 3
// squeezed: 2
// edge: 1
// corner: 2
// sorrounded 4

// Need a positions checked

// Need search algorithm to find all connected pieces

