use std::fs::File;
use ndarray::Array2;
use std::io::{self, Read};

fn main() -> io::Result<()> { // returns nothing on success
    let mut file = File::open("src/input.txt")?; // ? propagates error to main

    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut array1: Vec<i32> = Vec::new();

    for c in contents.chars() {
        if c == 'X' {
            array1.push(1);
        }
        if c == 'M' {
            array1.push(2);
        }
        if c == 'A' {
            array1.push(3);
        }
        if c == 'S' {
            array1.push(4);
        }
        else {
            println!("Couldn't match letter");
        }
    }

    // Initialize an array with the first row
    // Append the rest of the rows to the matrix

    // Write function to count the number of occurrences in a row
        // Recognize both forward and backward occurrences
    // Write loops to extract the slices and send to function

    // make a vector with all numbers in 1 row
    // make shape = (row, columns)
    // let array = Array2::from_shape_vec(shape, data).expect("Shape not right.")

    Ok(())
}



