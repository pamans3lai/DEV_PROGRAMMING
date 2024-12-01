fn return_str() -> String {
    let country = String::from("Austria");

    country
}

fn main() {
    let country_name = return_str();
    println!("{}", country_name);
}
