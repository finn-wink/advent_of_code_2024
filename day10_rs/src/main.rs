use std::fs::File;
use std::io::{self, BufRead};
use array2d::Array2D;

fn find_number_positions(matrix: &Array2D<i32>, max_num: i32) -> Vec<Vec<(usize,usize)>> {

    let mut all_positions: Vec<Vec<(usize, usize)>> = Vec::new();
    let mut zero_positions: Vec<(usize, usize)> = Vec::new();

    for i in 0..max_num {
        for (r, row_iter) in matrix.rows_iter().enumerate() {
            for (c, element)in row_iter.enumerate() {
                if element == &i {
                    zero_positions.push((r as usize, c as usize));
                }
            }
            all_positions.push(zero_positions.clone());
        }
    }
    return all_positions
}

fn find_next(current: &Vec<(usize, usize)>, next_possible: &Vec<(usize, usize)>) -> Vec<(usize,usize)> {
    
    let mut new_positions: Vec<(usize, usize)> = Vec::new();

    for c in current.iter() {
        for n in next_possible.iter() {
            let diff1 = c.0 as isize - n.0 as isize;
            let diff2 = c.1 as isize - n.1 as isize;
            println!("{}", diff1);
            println!("{}", diff2);
            if (diff1 == 1 as isize || diff1 == -1 as isize) && diff2 == 0 {
                new_positions.push(*n);
            }
            else if (diff2 == 1 as isize|| diff1 == -1 as isize) && diff1 == 0 {
                new_positions.push(*n);
            }
        }
    }
    println!("{:?}", new_positions);
    return new_positions;
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    
    let file = File::open("src/input.txt")?; // ? propagates error to main
    let reader = io::BufReader::new(file);

    let mut raw_arr: Vec<Vec<i32>> = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut line_arr: Vec<i32> = Vec::new();

        for char in line.chars() {
            let char_int = char.to_string().parse::<i32>().unwrap();
            line_arr.push(char_int);
        }
        raw_arr.push(line_arr);
    }

    // Make list of lists into 2D array
    let array = Array2D::from_rows(&raw_arr)?;

    let position_list = find_number_positions(&array, 9);

    println!("{:?}", position_list);

    let mut cur_search: Vec<(usize, usize)> = Vec::new();

    for (i, current) in position_list.iter().enumerate() {
        if i == 0 {
            cur_search = current.clone();
        }
        if i < 8 {
            let new_search = find_next(&cur_search, &position_list[i+1]);
            cur_search = new_search;
        }
    }

    println!("{:?}", cur_search);
    
    // current positions -> next positions 

    // trailheads are at position list[0]
    // check_list -> first all 0s then all numbers found
    // Check distance between all combinations
    // If total distance is 1 or -1 add it to the new list to be checked
    // Need to find all the total iterations that are run somehow

    Ok(())

}
