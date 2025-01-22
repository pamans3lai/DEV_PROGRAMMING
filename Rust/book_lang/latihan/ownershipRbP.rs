fn main() {
    let x = 5;
    let y = &x;

    // println!("memory adalah {:p}, p");
    assert_eq!(5, *y);
}
