fn main() {
    let judul = "BERITA HARI INI";
    println!("{:-^30}", judul);
    let bar = "|";
    println!("{: <15}{: >15}", bar, bar);
    let a = "JAKARTA";
    let b = "BOGOR";
    println!("{kota1:-15}{kota2:->15}", kota1 = a, kota2 = b);
}
