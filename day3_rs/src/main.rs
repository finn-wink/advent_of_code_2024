use regex::Regex;
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
        }
    }

    let mut step_2_strings: Vec<String> = Vec::new();

    // split the string at the first )
        for x in step_1_strings {
            let split_string: Vec<String> = x
                .split_inclusive(")")
                .map(|n| n.trim().to_string())
                .collect();
            
            step_2_strings.push(split_string[0].clone());
        } 
    
    let mut step_3_strings: Vec<String> = Vec::new();
    
    // keep only the first 12 symbols if longer than 12
        for y in step_2_strings {
            if y.len() > 12 {
                let truncated: String = y.chars().take(12).collect();
                step_3_strings.push(truncated.clone());
            }
            else {
                step_3_strings.push(y);
            }
        }
        
    // let mut step_4_strings: Vec<String> = Vec::new();

    let valid_pattern = Regex::new(r"^\d+,\d+$").unwrap();
    let mut result = 0;

        for c in step_3_strings {
            if c.contains("(") && c.contains(")") { // check if both () are present
                if let Some(start) = c.find("(") { // find the start and end
                    if let Some(end) = c.find(")") {
                        let extracted = &c[start+1..end]; // only get the center of it
                        if valid_pattern.is_match(extracted) { // match regex pattern to exclude other characters
                            let splits : Vec<String> = extracted.split(",").map(|s| s.to_string()).collect(); // split by comma
                            match (splits[0].parse::<i32>(), splits[1].parse::<i32>()) {
                                (Ok(n1), Ok(n2)) => { // multiply
                                    result += n1 * n2;
                                },
                                _ => {println!("Failed")}
                            }    
                        }
                    }
                }
            }
        }
        
    println!("{}", result);

    Ok(())
}
