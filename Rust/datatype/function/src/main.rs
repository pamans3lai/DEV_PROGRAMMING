// fn main() {
//     another_function(4);
// }
//
// fn another_function(x: i32) {
//     println!("nilainya adalah x : {x}");
// }
//
fn main() {
    let x = plus_one(5);

    println!("nilai x adalah: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
