use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    //   println!("{}", a[3]);

    println!("input index array dong:");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Gak kebaca woyyyy!!!");

    let index: usize = index.trim().parse().expect("Bukan nomor Coyyy!!!");

    let element = a[index];

    println!("Nilai elemen pada index {index} adalah: {element}");
}
