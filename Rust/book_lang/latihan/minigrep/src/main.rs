// fn main() {
//     println!("Hello, world!");
// }
//
//
use std::{env, fs};

fn main() {
    let args: Vec<String> = env::args().collect();
    // dbg!(args);
    //
    let query = &args[1];
    let file_path = &args[2];
    println!("Mencari: {query}");
    println!("di dalam berkas: {file_path}");
    println!("di berkas: {file_path}");

    let contents = fs::read_to_string(file_path).expect("harusnya sudah bisa baca file nih");

    println!("dengan text:\n{contents}");
}
