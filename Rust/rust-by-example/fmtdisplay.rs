use std::fmt;

#[derive(Debug)]
struct MinMax(i64, i64);

impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}, {}", self.0, self.1)
    }
}

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Bandingkan struktur:");
    println!("Display: {}", minmax);
    println!("Debug: {:?},", minmax);

    let big_range = MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!(
        "range besar adalah {big} dan yang kecil adalah {small}",
        small = small_range,
        big = big_range
    );

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Bandingkan struktur:");
    println!("Display: {}", point);
    println!("Debug: {:?},", point);
}
