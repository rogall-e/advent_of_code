use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;



fn main() {
    let mut times:Vec<i32> = Vec::new();
    let mut distances:Vec<i32> = Vec::new();
    let mut combined_time:i64 = 0;
    let mut combined_distance:i64 = 0;

    if let Ok(lines) = read_lines("./input/input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(digit_line) = line {
                if digit_line.starts_with("Time:"){
                    let times_temp:Vec<&str> = digit_line
                        .split_whitespace()
                        .skip(1)
                        .filter(|x| x.parse::<i32>().is_ok())
                        .collect();

                    combined_time = times_temp.join("").parse().unwrap();
                    for time in times_temp {
                        times.push(time.parse().unwrap());
                        }

                    } else {

                    let distances_temp:Vec<&str> = digit_line
                        .split_whitespace()
                        .skip(1)
                        .filter(|x| x.parse::<i32>().is_ok())
                        .collect();
    
                    combined_distance =  distances_temp.join("").parse().unwrap();

                    for distance in distances_temp {
                        distances.push(distance.parse().unwrap());
                                       }
                }
            }
        }
    }
   part_one(times, distances);
   part_two(combined_time, combined_distance);
}

fn part_two(combined_time:i64, combined_distance:i64) {
    let mut winning_distance:i64 = 0;
    for ms in 14..combined_time {
        let distance_travelled:i64 = (combined_time-ms)*ms;
        if distance_travelled > combined_distance {
            winning_distance = winning_distance + 1;
        }
    }
    println!("Solution task 2: {winning_distance}")   
}

fn part_one(times:Vec<i32>, distances:Vec<i32>) {    
    let mut winning_distance_vec:Vec<i32> = Vec::new();
    for (idx, time) in times.into_iter().enumerate() {
        let mut winning_distance:i32 = 0;
        for ms in 1..time {
            let distance_travelled = (time-ms) * ms;
            if distance_travelled > distances[idx] {
                winning_distance = winning_distance + 1;
            }
        }
        winning_distance_vec.push(winning_distance);
    }

    let solution_one:i32 = winning_distance_vec.iter().copied().reduce(|a, b| a*b).unwrap();   
    println!("Solution task 1: {}", solution_one);

}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
