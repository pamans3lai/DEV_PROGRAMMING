fn main() {
    use std::collections::HashMap;

    let mut scores = HashMap::new();

    scores.insert(String::from("Biru"), 10);
    scores.insert(String::from("Kuning"), 50);

    //    let nama_tim = String::from("Blue");
    //   let score = scores.get(nama_tim).copied().unwrap_or(0);

    // println!("{skor}");

    for (key, value) in scores {
        println!("{key}: {value}");
    }
}
