use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener: TcpListener = TcpListener::bind("127.0.0.1:5050").unwrap();

    for stream: Result<TcpStream, Error> in listener.incoming() {
        let stream: TcpStream = stream.unwrap();

        // println!("Hello, world!");
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader: BufReader<&mut TcpStream> = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader lines() Lines<BufReader<&mut TcpStream>>
    .map(| result: Result<String, Error> | result.unwrap()) impl Iterator<Item = String>
    .take_while(| line: &String | !line.is_empty()) impl Iterator<Item = String>
    .collect();
} 
