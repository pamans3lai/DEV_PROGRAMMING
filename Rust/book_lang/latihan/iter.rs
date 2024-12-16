fn main() {
    let names = vec!["Ai", "|ican", "ihsan"];

    for name in names.iter() {
        match name {
            "Ai" => println!("ada ai di sini"),
            _ => println!("Halo {}", name),
        }
    }
    println!("nama: {:?}", names);
}
