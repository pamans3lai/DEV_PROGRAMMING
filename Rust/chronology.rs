// # starting at Oct7, 2024 on play.rust-lang.org

fn main() {
    println!("Hello, world!");
}

command:

. $HOME/.cargo/env

cargo new hello-rust  // bikin program rust berisi hello-rust

source $HOME/.cargo/env  // bikin rust kebaca di semua environment

cargo add ferris-says // menambahkan dependencies di cargo.toml, bisa juga pake tulis manual di
// file cargo.toml berisi [dependencies] ferris-says ="0.3.1" 

cargo build // install dependencies yang telah di-add
