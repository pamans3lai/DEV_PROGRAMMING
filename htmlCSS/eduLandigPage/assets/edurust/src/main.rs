use actix_web::{web, App, HttpServer};

#[actix_web::main]
fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            // .route("/", web::get().to(index))
            // .route("/again", web::get().to(index2))
            // .service(index3)
            .service(web::scope("/app").route("/index.html", web::get().to(index)))
    })
    .bind("127.0.0.1:8088")?
    .run()
    .await
}
