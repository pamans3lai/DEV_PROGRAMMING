fn main() {
    let negara = /*String::from */"Konoha";

    let refsatu = &negara;
    let refdua = &negara;
    let reftiga = &negara;

    println!("{}, {}, {}, {}", negara, refsatu, refdua, reftiga);
}
