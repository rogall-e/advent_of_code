use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;



fn main() {
    let mut sum_of_ids:i32 = 0;
    let red:i32 = 12;
    let green:i32 = 13;
    let blue:i32 = 14;
    let mut idx:i32 = 0;
    let color_pattern = Regex::new(r"(\d+)\s+(\w+)").unwrap();
    let mut sum_power:i32 = 0;

    if let Ok(lines) = read_lines("./input/input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(digit_line) = line {
                idx = idx + 1;
                let iterations = digit_line.split("; ");
                let mut max_red = 0;
                let mut max_blue = 0;
                let mut max_green = 0;

                for iteration in iterations {
                
                    for capture in color_pattern.captures_iter(iteration) {
                        if let (Some(number), Some(color)) = (capture.get(1), capture.get(2)) {
                            let number_int: i32 = number.as_str().parse().unwrap();
                            if color.as_str() == "red" && number_int > max_red {
                                max_red = number_int;
                            }
                            if color.as_str() == "blue" && number_int > max_blue {
                                max_blue = number_int;
                            }
                            if color.as_str() == "green" && number_int > max_green {
                                max_green = number_int;
                            }
                        }
                    }
                }
                if max_green <= green && max_red <= red && max_blue <= blue {
                    sum_of_ids = sum_of_ids + idx;
                }
                let power:i32 = max_green * max_blue * max_red;
                sum_power = sum_power + power;
            }
        }
    }
    println!("Solution for task 1: {sum_of_ids}");
    println!("Solution for task 2: {sum_power}");
}



// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
