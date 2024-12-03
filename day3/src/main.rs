use std::fs::File;
use std::io::{self, Read};

fn main() -> io::Result<()> { // returns nothing on success
    let mut file = File::open("src/input.txt")?; // ? propagates error to main

    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    
    let split_strings: Vec<String> = contents // split the string by m and append m
        .split_inclusive("m")
        .map(|s| format!("m{}", s.trim()))
        .collect();

    let mut step_1_strings: Vec<String> = Vec::new();

    for s in split_strings { // make sure strings start with mul(
        if s.starts_with("mul(") {
            step_1_strings.push(s.to_string());
            println!("{}", s);
        }
    }

    let mut step_2_strings: Vec<String> = Vec::new();

    // split the string at the first )
    for i in 0..3 {
        if i > 0 {
            step_1_strings = step_2_strings.clone()
        }
        for x in step_1_strings {
            let split_string: Vec<String> = x
                .split_inclusive(")")
                .map(|n| n.trim().to_string())
                .collect();
            
            step_2_strings.push(split_string[0].clone());
            println!("{}", split_string[0]);
        } 
    }

    Ok(())
}
