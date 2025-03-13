// fn main() {
//     let x_ref = {
//         let x = 3;
//         &x 
//     }
// };

// println!("{}", x_ref)

fn max_of_ref(a: &i32, b: &i2) -> &i32 {
    if *a > *b {
        a
    } else {
        b
    }
}

fn complex_function(a: &i32) -> &i32 {
    let b = 2;
    max_of_refs(a, &b)
}

fn main() {
    let a = 1;
    let my_num = complex_function(&a);
    println!("{my_num}");
}