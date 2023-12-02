use std::char;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    part_one();
    part_two();
}   


fn part_two() {
    let mut solution = 0;
    if let Ok(lines) = read_lines("./input/input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(digit_line) = line {
                
                let replaced = digit_line.replace("one", "one1one");
                let replaced = replaced.replace("two", "two2two");
                let replaced = replaced.replace("three", "three3three");
                let replaced = replaced.replace("four", "four4four");
                let replaced = replaced.replace("five", "five5five");
                let replaced = replaced.replace("six", "six6six");
                let replaced = replaced.replace("seven", "seven7seven");
                let replaced = replaced.replace("eight", "eight8eight");
                let replaced = replaced.replace("nine", "nine9nine");
                    
                let numbers = finding_digits(replaced);
                solution = calc_solution(numbers, solution);
            }
        }
    }
    println!("Solution for task 2: {solution}");
}

fn part_one() {
  let mut solution = 0;
   if let Ok(lines) = read_lines("./input/input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(digit_line) = line {  
                let numbers = finding_digits(digit_line);
                solution = calc_solution(numbers, solution);               
            }
        }
    }
    println!("Solution for task 1: {solution}")
}

fn finding_digits(lines:String) -> Vec<char> {
    let mut numbers: Vec<char> = Vec::new();
    for element in lines.chars() {
        if element.is_numeric() {
            numbers.push(element)
        }
    }
    return numbers;
}

fn calc_solution(digit_vec:Vec<char>,  solution:i32) -> i32 {
    let first_digit = digit_vec[0];
    let last_digit = digit_vec[digit_vec.len()-1];
    let mut digit = String::from("");
    digit.push(first_digit);
    digit.push(last_digit);
    let number: i32 = digit.parse::<i32>().unwrap();
    let solution = solution + number;
    return solution;
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
