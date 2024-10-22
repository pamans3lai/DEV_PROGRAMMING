struct Pizza {
    name: String,
    price: i32,
}

fn main() {
    let pizza = Pizza {
        name: String::from("my pizza"),
        price: 10
    };
    println!("Nama pizzaku adalah >{}< dan harganya adalah {}", pizza.name, pizza.price);
}
