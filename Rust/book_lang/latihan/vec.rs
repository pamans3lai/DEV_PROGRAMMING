fn main() {
    let v = vec![1, 2, 3, 4, 5];

    let ketiga = v[2];
    println!("element ke-tiga adalah {ketiga}");

    let ketiga = v.get(2);
    match ketiga {
        Some(ketiga) => println!("elemen ketiga adalah {ketiga}"),
        None => println!("tidak ada elemen ketiga"),
    }
}
