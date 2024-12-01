fn cetak_negara(nama_negara: String) {
    println!("{}", nama_negara);
}

fn main() {
    let negara = String::from("Konoha");
    cetak_negara(negara.clone());
    cetak_negara(negara);
}
