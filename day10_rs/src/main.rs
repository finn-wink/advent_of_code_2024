use std::fs::File;
use std::io::{self, BufRead};
use array2d::Array2D;
use std::collections::HashSet;

fn find_number_positions(matrix: &Array2D<i32>, max_num: i32) -> Vec<Vec<(usize,usize)>> {

    let mut all_positions: Vec<Vec<(usize, usize)>> = Vec::new();
    let mut num_positions: Vec<(usize, usize)> = Vec::new();

    for i in 0..max_num {
        
        num_positions.clear();
        
        for (r, row_iter) in matrix.rows_iter().enumerate() {
            for (c, element) in row_iter.enumerate() {
                if element == &i {
                    num_positions.push((r as usize, c as usize));
                }
            }
        }
        all_positions.push(num_positions.clone());
    }
    return all_positions
}

fn find_next(current: &Vec<(usize, usize)>, next_possible: &Vec<(usize, usize)>) -> Vec<(usize,usize)> {
    
    let mut new_positions: Vec<(usize, usize)> = Vec::new();

    for c in current.iter() {
        for n in next_possible.iter() {
            let diff1 = c.0 as isize - n.0 as isize;
            let diff2 = c.1 as isize - n.1 as isize;

            if (diff1 == 1 as isize || diff1 == -1 as isize) && diff2 == 0 {
                new_positions.push(*n);
            }
            else if (diff2 == 1 as isize || diff2 == -1 as isize) && diff1 == 0 {
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

    // println!("{:?}", array);

    let position_list = find_number_positions(&array, 10); // for loop does not include 9

    println!("{:?}", position_list);

    let mut cur_search: Vec<(usize, usize)> = Vec::new();
    let mut total_trails: i32 = 0;

    for start in position_list[0].iter() {

        for (i, _current) in position_list.iter().enumerate() {
            if i == 0 {
                cur_search = vec![start.clone()];
                println!("{:?}", cur_search);
            }
            if i < 9 {
                let new_search = find_next(&cur_search, &position_list[i+1]);
                cur_search = new_search;
            }
        }
        println!{"{}", cur_search.len()}

        // Find unique tuples
        let mut seen = HashSet::new();
    
        let unique_tops: Vec<_> = cur_search.clone()
            .into_iter()
            .filter(|t| seen.insert(*t))
            .collect();
    
        total_trails += unique_tops.len() as i32;
    }

    println!("{}", total_trails);

    Ok(())

}
