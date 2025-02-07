use actix_web::{web, App, HttpRequest, HttpResponse, HttpServer};
use surrealdb::{Client, Database};

#[actix_web::main]

async fn main() -> std::io::Result<()> {
    // ....

    HttpServer::new(move || {
        App::new()
            .service(web::resource("/customers").route(web::get().to(get_customers)))
            .service(web::resource("/customers").route(web::post().to(create_customers)))
            .service(web::resource("/customers/{id}").route(web::get().to(get_customers)))
            .service(web::resource("/customers/{id}").route(web::put().to(update_customers)))
            .service(web::resource("/customers/{id}").route(web::delete().to(delete_customers)))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}

async fn get_customers(req: HttpRequest) -> HttpResponse {
    let db = req.app_data::<Database>().unwrap();
    let customers = db.query("SELECT * FROM customers").await?;

    HttpResponse::Ok().json(customers)
}

async fn create_customers(req: HttpRequest) -> HttpResponse {
    let db = req.app_data::<Database>().unwrap();
    let customers = req.json::<Customer>().await?;

    db.insert("customers", customer).await?;

    HttpResponse::Created().body("Customer created")
}
