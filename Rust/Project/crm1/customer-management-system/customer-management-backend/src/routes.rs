use actix_web::{web, App, HttpRequest, HttpResponse, HttpServer};
use surrealdb::{Client, Database};

#[actix_web::main]
async fn main() -> std::io:Result<()> {
    let db = Client::connect("surreal://localhost:8080").await?;
    let db = db.database("customers");

    HttpServer::new(move || {
        App::new()
        .service(web::resource("/customers").route(web::get().to(customer_list)))
        })
        .bind("127.0.0.1:8080")?
    .run()
        .await
}

async fn customer_list(req: HttpRequest) -> HttpResponse {
    let db req.app_data::<Database>().unwrap();
    let customers = db.query("SELECT * FROM customers").await?;

    HttpResponse::Ok().json(customers)
}
