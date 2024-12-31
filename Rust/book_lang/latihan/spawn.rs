#![allow(unused)]

fn main() {
    use std::thread;

    let computation = thread::spawn(|| 42);

    let result = computation.join().unwrap();
    println!("{result}");
}
