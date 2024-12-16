fn main() {
    let mut names = vec!["Ai", "|ican", "ihsan"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ai" => "ada ai di sini",
            _ => "Halo",
        }
    }
    println!("nama: {:?}", names);
}
