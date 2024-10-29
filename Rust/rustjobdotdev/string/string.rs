//  https://rustjobs.dev/blog/string-concatenation-in-rust/
//

fn main() {
    let s1 = "Hello";
    let s2 = "World";

// you neeed to convert &str to String before concatenating
// using .to_owned
//    let result = s1.to_owned() + " " + s2;
// or, using .to_string
//    let result = s1.to_owned() + " " + s2;
// or, using format! macro
//    let result = format!("{} {}", s1, s2);
// or, using push_str() method
      let mut result = s1.to_string();
      result.push_str(" ");
      result.push_str(s2);
      println!("{}", result);
}
