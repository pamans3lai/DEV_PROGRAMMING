fn main() {
    println!("Hello San!");
    println!(
        "{subject} {verb} {object}",
        object = "the lazy dog",
        subject = "the quick brown fox",
        verb = "jumps over"
    );

    println!("{number:>5}", number = 1);
}
