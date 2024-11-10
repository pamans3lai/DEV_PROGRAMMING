use rand::Rng;
use std::io;

fn main() {
    println!("Tebak angka!");

    let nomor_rahasia = rand::thread_rng().gen_range(1..=100);

    println!("Nomor rahasianya adalah: {nomor_rahasia}");

    println!("Silahkan input tebakan");

    let mut tebak = String::new();

    io::stdin()
        .read_line(&mut tebak)
        .expect("Baris tidak terbaca");

    println!("Tebakan anda: {tebak}");
}
