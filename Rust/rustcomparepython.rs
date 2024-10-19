// Here we take a vector by reference (&).
// We are not allowed to mutate elements.
// We don't take ownership; we just borrow.
fn print_vec(numbers: &Vec<i32>) {
   for number in numbers {
       print!("{} ", number);
   }
   println!()
}


// Here we take a vector by mutable reference (&mut).
// We are now allowed to mutate elements and the vector itself.
// We still don't take ownership; we just borrow.
fn add_one(numbers: &mut Vec<i32>) {
   numbers.push(1)
}


fn main() {
   let mut numbers = vec![1,1,1];
   // We pass a reference
   print_vec(&numbers);
   // We pass a mutable reference
   add_one(&mut numbers);
   // We pass a reference again
   print_vec(&numbers);
}
