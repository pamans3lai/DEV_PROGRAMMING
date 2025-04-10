#[derive(Debug)]
struct Structure(i32);

#[derive(Debug)]
struct Deep(Structure);

fn main() {
    println!("now {:?} will print", Structure(5));
    println!("now {:?} will print", Deep(Structure(9)));
}
